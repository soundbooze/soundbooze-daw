/* 
 * real-time alsa stream [uduk.org]
 * lightweight prepared for pi wiv cheap usb mic
 *
 * *deps: libxtract, alsa-lib
 *        usb cable guitar -> jack
 *
 * gcc -Wall -O3 pi-bark.c -o pi-bark -lm `pkg-config --cflags --libs alsa` -I/usr/local/include -L/usr/local/lib -lxtract
 *
 * */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <signal.h>
#include <alsa/asoundlib.h>

#include <xtract/libxtract.h>

#define TRUE                1

#define ALSA_DEVICE     "hw:2"
#define ALSA_CHANNEL        1

snd_pcm_t *capture_handle;
snd_pcm_hw_params_t *hw_params;

unsigned int rate = 48000;
int err;

void loop(void);

/* --------------- ALSA */

int
open_capture_device (void) 
{
  snd_pcm_format_t format = SND_PCM_FORMAT_S16_LE;
  snd_pcm_uframes_t buffer_size = 1024;
  snd_pcm_uframes_t period_size = 2;

  if ((err = snd_pcm_open (&capture_handle, ALSA_DEVICE, SND_PCM_STREAM_CAPTURE, 0)) < 0) {
    fprintf (stderr, "cannot open audio device %s (%s)\n", ALSA_DEVICE, snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_malloc (&hw_params)) < 0) {
    fprintf (stderr, "cannot allocate hardware parameter structure (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_any (capture_handle, hw_params)) < 0) {
    fprintf (stderr, "cannot initialize hardware parameter structure (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_set_access (capture_handle, hw_params, SND_PCM_ACCESS_MMAP_INTERLEAVED)) < 0) {
    fprintf (stderr, "cannot set access type (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_set_format (capture_handle, hw_params, format)) < 0) {
    fprintf (stderr, "cannot set sample format (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_set_rate_near (capture_handle, hw_params, &rate, 0)) < 0) {
    fprintf (stderr, "cannot set sample rate (%s)\n", snd_strerror (err));
    return -1;
  }
	
  if ((err = snd_pcm_hw_params_set_channels (capture_handle, hw_params, ALSA_CHANNEL)) < 0) {
    fprintf (stderr, "cannot set channel count (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_set_buffer_size_near (capture_handle, hw_params, &buffer_size)) < 0) {
    fprintf (stderr, "cannot set buffer size (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params_set_period_size_near (capture_handle, hw_params, &period_size, NULL)) < 0) {
    fprintf (stderr, "cannot set period size (%s)\n", snd_strerror (err));
    return -1;
  }

  if ((err = snd_pcm_hw_params (capture_handle, hw_params)) < 0) {
    fprintf (stderr, "cannot set parameters (%s)\n", snd_strerror (err));
    return -1;
  }

  snd_pcm_hw_params_free (hw_params);

  if ((err = snd_pcm_prepare (capture_handle)) < 0) {
    fprintf (stderr, "cannot prepare audio interface for use (%s)\n", snd_strerror (err));
    return -1;
  }

  return 0;
}

snd_pcm_uframes_t
get_buffer_size (void) {
  snd_pcm_uframes_t frames; 
  snd_pcm_hw_params_get_buffer_size	(hw_params, &frames);
  return frames;
}

/* --------------- UTILS */

void cleanup (void)
{
  snd_pcm_close(capture_handle);
}

void  
exit_handler (int s)
{
  cleanup();
  exit(0);
}

void 
bootstrap (void)
{
  if (open_capture_device() == -1) {
    exit_handler(SIGINT);
  }
  loop();
}

/* --------------- FEATURES (libxtract) */

void
pcm_to_double (const int16_t *buffer, double *buf_d, int N)
{
  short int i = 0;
  for (; i < N; i++) {
    double d = buffer[i] / 32768.0;
    *(buf_d + i) = d;
  }
}

double getDb(const double rms) 
{
  return (double) 20.0 * (log(rms) / M_LN10);
};

double getRMS(const double *buffer, int N) 
{

  double rms = 0.0;
  short int i = 0;

  for (i = 0; i < N; i++) {
    rms += pow(buffer[i], 2.0);
  }

  rms = rms / N;
  rms = sqrt(rms);

  return rms; 
};

/* --------------- LOOP */

void
loop (void) 
{
  int frames_t = (int) get_buffer_size();
  int buf_sz = frames_t * ALSA_CHANNEL * 2;
  int16_t buffer[buf_sz];
  double buffer_d[buf_sz];

  xtract_init_fft(frames_t, XTRACT_SPECTRUM);

  while(TRUE) {

    if ((err = snd_pcm_mmap_readi (capture_handle, buffer, frames_t)) != frames_t) {
      fprintf (stderr, "read from audio interface failed (%s)\n", snd_strerror (err));
      cleanup();
      bootstrap();
    }

    pcm_to_double(buffer, buffer_d, frames_t);

    double r = getRMS(buffer_d, frames_t);
    double d = getDb(r);

    // manual threshold
    //if (d > -8)
    printf("RMS = %.2f dB = %.2f\n", r, d);

    // libxtract
    //

    double *spectrum = NULL, argf[2];
    spectrum = (double *)malloc(frames_t * sizeof(double));
    argf[0] = 48000.0;
    argf[1] = XTRACT_MAGNITUDE_SPECTRUM;
    xtract_spectrum(buffer_d, frames_t, argf, spectrum);

    double spectral_mean, spectral_variance, spectral_stdev;
    xtract_spectral_mean(spectrum, frames_t, NULL, &spectral_mean);
    xtract_spectral_variance(spectrum, frames_t, &spectral_mean, &spectral_variance);	
    xtract_spectral_standard_deviation(spectrum, frames_t, &spectral_variance, &spectral_stdev);

    // printf ("%.4f %.4f %.4f\n", spectral_mean, spectral_variance, spectral_stdev);
    //
    // isnan checker
    // spectrum frames_t/2
    
    int band_limits[XTRACT_BARK_BANDS];
    xtract_init_bark(frames_t, 48000.0, band_limits);
    
    double bark_coeff[XTRACT_BARK_BANDS];
    xtract_bark_coefficients(spectrum, frames_t, &band_limits, bark_coeff);

    int i = 0;
    for (i = 0; i < XTRACT_BARK_BANDS; i++) {
      printf("Bark[%d] = %.6f\n", i, bark_coeff[i]);
    }

    double loudness;
    xtract_loudness(bark_coeff, XTRACT_BARK_BANDS, NULL, &loudness);
    printf("Loudness = %.6f\n", loudness);

    double result;
    xtract_spectral_centroid(spectrum, frames_t, NULL, &result);
    printf("Spectral Centroid = %.6f\n", result);

    double skurtosis;
    double argv[2];
    argv[0] = spectral_mean;
    argv[1] = spectral_stdev;
    xtract_spectral_kurtosis(spectrum, frames_t, argv, &skurtosis);
    printf("Spectral Kurtosis = %.6f\n", skurtosis);

    double ssharpness;
    xtract_sharpness(spectrum, frames_t, NULL, &ssharpness);
    printf("Spectral Sharpness = %.10e\n", ssharpness);

    double srolloff;
    double argz[2];
    argz[0] = 48000.0/2.0;
    argz[1] = 0.85;
    xtract_rolloff(spectrum, frames_t, argz, &srolloff);
    printf("Rolloff = %.10e\n", srolloff);

  }

  // high resolution timer ...
}

int
main (int argc, char *argv[])
{
  signal(SIGINT, exit_handler);
  bootstrap(); 
  exit (0);
}
