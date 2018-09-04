/* 
 * real-time alsa stream [uduk.org]
 *
 * https://aubio.org/doc/latest/examples.html
 * gcc -Wall -O3 realtime.c -o realtime -lm `pkg-config --cflags --libs alsa aubio`
 *
 * */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <signal.h>

#include <aubio/aubio.h>
#include <alsa/asoundlib.h>

#define TRUE          1

#define ALSA_DEVICE   "hw:2"
#define ALSA_CHANNEL       1

#define AUBIO_WINSIZE 1024

snd_pcm_t *capture_handle;
snd_pcm_hw_params_t *hw_params;

unsigned int rate = 48000;
int err;

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

void  
exit_handler (int s)
{
  aubio_cleanup ();
  snd_pcm_close (capture_handle);
  exit(0);
}

void
pcm_to_double (const int16_t *buffer, double *buf_d, int N)
{
  short int i = 0;
  for (; i < N; i++) {
    double d = buffer[i] / 32768.0;
    *(buf_d + i) = d;
  }
}

double getDb(const double rms) {
  return (double) 20.0 * (log(rms) / M_LN10);
};

double getRMS(const double *buffer, int N) {

  double rms = 0.0;
  short int i = 0;

  for (i = 0; i < N; i++) {
    rms += pow(buffer[i], 2.0);
  }

  rms = rms / N;
  rms = sqrt(rms);

  return rms; 
};

cvec_t *
aubio_fft (const double *buffer)
{
  uint_t i;

  /*
      **** sliding window if != frame size - hopsize (pow of 2)
  */
  
  fvec_t * in = new_fvec (AUBIO_WINSIZE);
  cvec_t * fftgrain = new_cvec (AUBIO_WINSIZE); // fft norm and phase

  aubio_fft_t * fft = new_aubio_fft(AUBIO_WINSIZE);
  if (!fft) {
    return NULL;
  }

  for (i = 0; i < AUBIO_WINSIZE; i++) {
    in->data[i] = buffer[i];
  }

  aubio_fft_do (fft,in,fftgrain);
  //cvec_print(fftgrain);

  del_fvec(in);
  del_aubio_fft(fft);

  return fftgrain;
}

int 
aubio_mfcc (cvec_t *fftgrain)
{
  uint_t n_filters = 40; // number of filters
  uint_t n_coefs = 13; // number of coefficients
  smpl_t samplerate = rate;

  fvec_t *out = new_fvec (n_coefs);

  aubio_mfcc_t *o = new_aubio_mfcc (AUBIO_WINSIZE, n_filters, n_coefs, samplerate);

  cvec_norm_set_all (fftgrain, 1.);
  aubio_mfcc_do (o, fftgrain, out);
  fvec_print (out);

  cvec_norm_set_all (fftgrain, .5);
  aubio_mfcc_do (o, fftgrain, out);
  fvec_print (out);

  del_aubio_mfcc (o);
  del_fvec (out);

  return 0;
}

void
loop (void) 
{
  int frames = (int) get_buffer_size();
  int buf_sz = frames * ALSA_CHANNEL * 2;
  int16_t buffer[buf_sz];
  double buffer_d[buf_sz];

  while(TRUE) {

    if ((err = snd_pcm_mmap_readi (capture_handle, buffer, frames)) != frames) {
      fprintf (stderr, "read from audio interface failed (%s)\n", snd_strerror (err));
      exit_handler(SIGINT);
    }

    pcm_to_double(buffer, buffer_d, frames);

    double r = getRMS(buffer_d, frames);
    double d = getDb(r);

    // manual threshold
    if (d > -8)
      printf("RMS = %.2f dB = %.2f\n", r, d);

    cvec_t *fftgrain = aubio_fft(buffer_d);
    aubio_mfcc(fftgrain);
    del_cvec(fftgrain);

  }
}

int
main (int argc, char *argv[])
{
  signal(SIGINT, exit_handler);

  if (open_capture_device() == -1) {
    exit_handler(SIGINT);
  }

  loop();

  exit (0);
}
