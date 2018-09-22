#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <signal.h>
#include <alsa/asoundlib.h>

#include <pthread.h>
#include <xtract/libxtract.h>

#include <SDL.h>

#define WIDTH  800
#define HEIGHT 200

#define TRUE                1

#define ALSA_DEVICE     "hw:2"
#define ALSA_CHANNEL        1

#define AMPLIFY_CONTRAST    10

pthread_t id;

SDL_Window* window = NULL;
SDL_Renderer* renderer = NULL;

snd_pcm_t *capture_handle;
snd_pcm_hw_params_t *hw_params;

double bark_coeff[XTRACT_BARK_BANDS];

unsigned int rate = 48000;
int err;

void * loop(void *args);

/* --------------- FLUID */

#include <fluidsynth.h>

#define SOUNDFONT "example.sf2"

fluid_synth_t *synth;
fluid_settings_t *settings;
fluid_audio_driver_t *adriver;
int sfont_id;

void
fluid_init(void)
{
  settings = new_fluid_settings();
  synth = new_fluid_synth(settings);
  adriver = new_fluid_audio_driver(settings, synth);
  sfont_id = fluid_synth_sfload(synth, SOUNDFONT, 1);
}

void
fluid_trigger(void)
{
  fluid_synth_noteon(synth, 0, 42, 124);
  fluid_synth_noteoff(synth, 0, 42);
}

void
fluid_cleanup(void)
{
  delete_fluid_audio_driver(adriver);
  delete_fluid_synth(synth);
  delete_fluid_settings(settings);
}

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
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  SDL_Quit();
  pthread_exit(&id);
  fluid_cleanup();
  snd_pcm_close(capture_handle);
}

void  
exit_handler (int s)
{
  cleanup();
  exit(0);
}

double naiveSum = 0.0;

time_t t1=0, t2=0, t3 = 0;

double band1sumMax = 0.0;
double band1sumMin = 100.0;

void
thresholdFinding(double band1sum, double band2sum)
{
  /* TODO: auto threshold /min/max -via ts*/

  if (band1sum > band1sumMax)
    band1sumMax = band1sum;

  if (band1sum < band1sumMin)
    band1sumMin = band1sum;

  printf("%.8f %.8f\n", band1sumMax, band1sumMin);

  /* [[156 . 0.6]] [[-2 -0.2]] [[-]] ra ono sing ero
  if (band1sum > band1sumMax/2) {
    naiveSum += band1sum;

    if (naiveSum > 8.05) {

      t1 = time(&t1);
      t2 = time(&t2);
      int subt = (int)(t2 - t3);
      if (subt)
        fluid_trigger();
      printf("%d %d\n", t1, t2);
      printf("Sub : %d - Sum: %.8f\n", subt ? 1 : 0, naiveSum);
      t3 = t1;

      fluid_trigger();


      naiveSum = 0;
    }
  }
  */
}

void 
bootstrap (void)
{

  fluid_init();

  if (open_capture_device() == -1) {
    exit_handler(SIGINT);
  }

   int ret;
  
  ret = pthread_create(&id,NULL, &loop, NULL);
  if (ret != 0){
    printf("Thread not created.\n");
  }

  if (SDL_Init(SDL_INIT_VIDEO) == 0) {

    window = SDL_CreateWindow("Prepared For Pi", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_OPENGL);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);

    SDL_bool done = SDL_FALSE;

    int x = 0;
    int y = 100;

    while (!done) {
      SDL_Event event;

      double band1sum = 0.0;
      for (int i = 1; i < XTRACT_BARK_BANDS / 2; i++) {
        band1sum += bark_coeff[i];
      }

      double band2sum = 0.0;
      for (int i = (XTRACT_BARK_BANDS / 2) + 1; i < XTRACT_BARK_BANDS; i++) {
        band2sum += bark_coeff[i];
      }

      // band1
      
      SDL_SetRenderDrawColor(renderer, 255 * band1sum * AMPLIFY_CONTRAST, 255 * band1sum * AMPLIFY_CONTRAST, 0, 255);
      SDL_Rect rh1;
      rh1.x = x;
      rh1.y = 0;
      rh1.w = 1;
      rh1.h = 50;
      SDL_RenderFillRect(renderer, &rh1);

      SDL_SetRenderDrawColor(renderer, 255 * band1sum, 255 * band1sum, 0, 255);
      SDL_Rect rv1;
      rv1.x = 0;
      rv1.y = y - 50;
      rv1.w = WIDTH;
      rv1.h = 1;
      SDL_RenderFillRect(renderer, &rv1);

      // band2

      SDL_SetRenderDrawColor(renderer, 255 * band2sum * AMPLIFY_CONTRAST, 255 * band2sum * AMPLIFY_CONTRAST, 255 * band2sum * AMPLIFY_CONTRAST, 255);
      SDL_Rect rh2;
      rh2.x = x;
      rh2.y = 51;
      rh2.w = 1;
      rh2.h = 50;
      SDL_RenderFillRect(renderer, &rh2);

      SDL_SetRenderDrawColor(renderer, 255 * band2sum, 255 * band2sum, 255 * band2sum, 255);
      SDL_Rect rv2;
      rv2.x = 0;
      rv2.y = y;
      rv2.w = WIDTH;
      rv2.h = 1;
      SDL_RenderFillRect(renderer, &rv2);

      thresholdFinding(band1sum, band2sum);

      x++;
      y--;

      // clear

      SDL_RenderPresent(renderer);

      if (x == WIDTH) {
        x ^= x;
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
        SDL_RenderClear(renderer);
      }

      if (y == 50) {
        y = 100;
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
        SDL_RenderClear(renderer);
      }

      while (SDL_PollEvent(&event)) {
        if (event.type == SDL_QUIT) {
          done = SDL_TRUE;
        }
      }

    }

  }

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

void *
loop (void *args) 
{
  int frames_t = 1024;
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

    double *spectrum = NULL, argf[2];
    spectrum = (double *)malloc(frames_t * sizeof(double));
    argf[0] = rate;
    argf[1] = XTRACT_MAGNITUDE_SPECTRUM;
    xtract_spectrum(buffer_d, frames_t, argf, spectrum);

    double spectral_mean, spectral_variance, spectral_stdev;
    xtract_spectral_mean(spectrum, frames_t, NULL, &spectral_mean);
    xtract_spectral_variance(spectrum, frames_t, &spectral_mean, &spectral_variance);	
    xtract_spectral_standard_deviation(spectrum, frames_t, &spectral_variance, &spectral_stdev);

    int band_limits[XTRACT_BARK_BANDS];
    xtract_init_bark(frames_t, 48000.0, band_limits);
    
    xtract_bark_coefficients(spectrum, frames_t, &band_limits, bark_coeff);
  }

}

int
main (int argc, char *argv[])
{
  signal(SIGINT, exit_handler);
  bootstrap(); 
  exit (0);
}
