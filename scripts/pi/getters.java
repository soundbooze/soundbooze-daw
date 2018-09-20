	/**
	 * The array with constant q coefficients. If you for
	 * example are interested in coefficients between 256 and 1024 Hz
	 * (2^8 and 2^10 Hz) and you requested 12 bins per octave, you
	 * will need 12 bins/octave * 2 octaves * 2 entries/bin = 48
	 * places in the output buffer. The coefficient needs two entries
	 * in the output buffer since they are complex numbers.
	 */

	/**
	 * The output buffer with constant q magnitudes. If you for example are
	 * interested in coefficients between 256 and 1024 Hz (2^8 and 2^10 Hz) and
	 * you requested 12 bins per octave, you will need 12 bins/octave * 2
	 * octaves = 24 places in the output buffer.
	 */

	public float[] getFreqencies() {
		return frequencies;
	}
	
	/**
	 * Returns the Constant Q magnitudes calculated for the previous audio
	 * buffer. Beware: the array is reused for performance reasons. If your need
	 * to cache your results, please copy the array.
	 * @return The output buffer with constant q magnitudes. If you for example are
	 * interested in coefficients between 256 and 1024 Hz (2^8 and 2^10 Hz) and
	 * you requested 12 bins per octave, you will need 12 bins/octave * 2
	 * octaves = 24 places in the output buffer.
	 */
	public float[] getMagnitudes() {
		return magnitudes;
	}

	
	/**
	 * Return the Constant Q coefficients calculated for the previous audio
	 * buffer. Beware: the array is reused for performance reasons. If your need
	 * to cache your results, please copy the array.
	 * 
	 * @return The array with constant q coefficients. If you for example are
	 *         interested in coefficients between 256 and 1024 Hz (2^8 and 2^10
	 *         Hz) and you requested 12 bins per octave, you will need 12
	 *         bins/octave * 2 octaves * 2 entries/bin = 48 places in the output
	 *         buffer. The coefficient needs two entries in the output buffer
	 *         since they are complex numbers.
	 */
	public float[] getCoefficients() {
		return coefficients;
	}

	/**
	 * @return The number of coefficients, output bands.
	 */
	public int getNumberOfOutputBands() {
		return frequencies.length;
	}

	/**
	 * @return The required length the FFT.
	 */
	public int getFFTlength() {
		return fftLength;
	}
