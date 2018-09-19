//  gcc fftw.c -o fftw -lfftw3 -lm

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

void
fftw3 (double *originalSignal, long originalLen)
{
  const int frameSize = originalLen;
  double *frameSignal = (double *) calloc (frameSize, sizeof (double));

  double *out,*mag,*phase;
  double real,imag;

  for (int i = 0; i < frameSize; i++) {
    frameSignal[i] = originalSignal[i];
  }

  fftw_complex *out_cpx, *mod_cpx;
  fftw_plan fft; 

  out_cpx = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*(frameSize/2+1));
  mod_cpx = (fftw_complex*) fftw_malloc(sizeof(fftw_complex)*(frameSize/2+1));
  out = (double *) malloc(frameSize*sizeof(double));
  mag = (double *) malloc(frameSize*sizeof(double));
  phase = (double *) malloc(frameSize*sizeof(double));

  fft = fftw_plan_dft_r2c_1d(frameSize, frameSignal, out_cpx, FFTW_ESTIMATE);
  fftw_execute(fft);
  
  for (int j = 0; j < frameSize/2 + 1; j++) {
    real = out_cpx[j][0];
    imag = out_cpx[j][1];
    mag[j] = sqrt((real*real)+(imag*imag));
    phase[j] = atan2(imag,real);
    printf("%.16f %.16f %.16f %.16f\n", real, imag, mag[j], phase[j]);
  }

  fftw_destroy_plan(fft);
  fftw_free(out_cpx);
  fftw_free(mod_cpx);
  free(out);
  free(mag);
  free(phase);
  free(frameSignal);
}

int
main()
{
  double s[4] = {2.0, 0.2, 4.9, 1.1};
  fftw3(s, 4);
}
