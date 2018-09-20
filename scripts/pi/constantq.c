
//  gcc fftw.c -o fftw -lfftw3 -lm
//  https://github.com/JorenSix/TarsosDSP/blob/c26e5004e203ee79be1ec25c2603b1f11b69d276/src/core/be/tarsos/dsp/ConstantQ.java

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

void
fftw3 (double *originalSignal, long originalLen)
{
  const int frameSize = originalLen;
  double *frameSignal = (double *) calloc (frameSize, sizeof (double));

  double *out, *mag, *phase;
  double real, imag;

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
  }

  fftw_destroy_plan(fft);
  fftw_free(out_cpx);
  fftw_free(mod_cpx);
  free(out);
  free(mag);
  free(phase);
  free(frameSignal);
}


/* assign list -> free */

	int fftLength;

  /*  malloc */
	double[] frequencies;
	double[][] qKernel;
	int[][] qKernel_indexes;
	
	float[] coefficients;
	float[] magnitudes;

  /*  fft */
	FFT fft;


void 
ConstantQ (unsigned int sampleRate, double minFreq, double maxFreq, unsigned short int binsPerOctave) 
{

  unsigned int i = 0, j = 0;

  double threshold = 0.001f;
  double spread = 1.0f;

  double q = 1.0 / (pow(2, 1.0 / binsPerOctave) - 1.0) / spread;
  int numberOfBins = (int) ceil(binsPerOctave * log(maximumFreqency / minimumFrequency) / log(2));

  /* malloc  */
  coefficients = new float[numberOfBins*2];
  magnitudes = new float[numberOfBins];

  double calc_fftlen = (float) ceil(q * sampleRate / minimumFrequency);
  
  /* fft  */
  fftLength = (int) calc_fftlen; 
  fftLength = (int) pow(2, ceil(log(calc_fftlen) / log(2)));
  
  /* fft *malloc  */
  fft = new FFT(fftLength);
  qKernel = new float[numberOfBins][];
  qKernel_indexes = new int[numberOfBins][];
  frequencies = new float[numberOfBins];

   float[] temp = new float[fftLength*2];
   float[] ctemp = new float[fftLength*2];
   int[] cindexes = new int[fftLength];
      for (i = 0; i < numberOfBins; i++) {
        float[] sKernel = temp;
        frequencies[i] = (float) (minimumFrequency * pow(2, i/binsPerOctave ));
        /* MACRO  MIN */
        int len = (int)min(ceil( q * sampleRate / frequencies[i]), fftLength);
        
        for (j = 0; j < len; j++) {
          
          double window = -.5*cos(2.*M_PI*(double)j/(double)len)+.5;; // Hanning Window

          window /= len;
        
          double x = 2*Math.PI * q * (double)j/(double)len;
          sKernel[j*2] = (float) (window * cos(x));
          sKernel[j*2+1] = (float) (window * sin(x));	
      }
        for (j = len*2; j < fftLength*2; j++) {
          sKernel[j] = 0;
        }

        /* FFT  */
    fft.complexForwardTransform(sKernel);

    /* arr copy */
    float[] cKernel = ctemp;

    int k = 0;
    for (j = 0, j2 = sKernel.length - 2; j < sKernel.length/2; j+=2,j2-=2) {
      double absval = sqrt(sKernel[j]*sKernel[j] + sKernel[j+1]*sKernel[j+1]);
      absval += sqrt(sKernel[j2]*sKernel[j2] + sKernel[j2+1]*sKernel[j2+1]);	    	    
      if(absval > threshold) {
        cindexes[k] = j;
        cKernel[2*k] = sKernel[j] + sKernel[j2];
        cKernel[2*k + 1] = sKernel[j + 1] + sKernel[j2 + 1];
        k++;
      }	    		
    }

    /* realloc   || new */
    sKernel = new float[k * 2];
    int[] indexes = new int[k];

    for (j = 0; j < k * 2; j++)
      sKernel[j] = cKernel[j];
    for (j = 0; j < k; j++)
      indexes[j] = cindexes[j];

    // Normalize fft output
    for (j = 0; j < sKernel.length; j++)
      sKernel[j] /= fftLength;

    // Perform complex conjugate on sKernel
    for (j = 1; j < sKernel.length; j += 2)
      sKernel[j] = -sKernel[j];
    
    for (j = 0; j < sKernel.length; j ++)
      sKernel[j] = -sKernel[j];

    qKernel_indexes[i] = indexes;
    qKernel[i] = sKernel;
  }
}

void calculate(double *inputBuffer) {

  /*  fft */
  fft.forwardTransform(inputBuffer);

  int i = 0, j = 0;
  int qKernelLen = sizeof(qKernel) / sizeof(double);

  for (i = 0; i < qKernelLen; i++) {

    /*  append */
    double[] kernel = qKernel[i];

    int[] indexes = qKernel_indexes[i];
    float t_r = 0;
    float t_i = 0;
    for (j = 0, l = 0; j < sizeof(kernel) / sizeof(double); j += 2, l++) {
      int jj = indexes[l];
      double b_r = inputBuffer[jj];
      double b_i = inputBuffer[jj + 1];
      double k_r = kernel[j];
      double k_i = kernel[j + 1];
      t_r += b_r * k_r - b_i * k_i;
      t_i += b_r * k_i + b_i * k_r;
    }
    coefficients[i * 2] = t_r;
    coefficients[i * 2 + 1] = t_i;
  }
}

/**
 * Take an input buffer with audio and calculate the constant Q magnitudes.
 * @param inputBuffer The input buffer with audio.
 */
public void calculateMagnitudes(float[] inputBuffer) {
  calculate(inputBuffer);
  for(int i = 0 ; i < magnitudes.length ; i++){
    magnitudes[i] = (float) Math.sqrt(coefficients[i*2] * coefficients[i*2] + coefficients[i*2+1] * coefficients[i*2+1]); 
  }
}

@Override
public boolean process(AudioEvent audioEvent) {
  float[] audioBuffer = audioEvent.getFloatBuffer().clone();
  if(audioBuffer.length != getFFTlength()){
    throw new IllegalArgumentException(String.format("The length of the fft (%d) should be the same as the length of the audio buffer (%d)",getFFTlength(),audioBuffer.length));
  }
  calculateMagnitudes(audioBuffer);
  return true;
}


}
