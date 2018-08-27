## Genre Classification 

Tools, libraries, utilities 

- https://github.com/MTG/gaia

apt-get install build-essential libqt4-dev libyaml-dev swig python-dev pkg-config

```
# root
./waf configure --with-tests --with-python-bindings
./waf
./waf install
```

export PYTHONPATH=/usr/local/lib/python2.7/dist-packages/

#### run unittest (to build dataset_small.db)

```
python tests.py && python test_parser.py && python testdata.py
```
___

- https://github.com/MTG/essentia

```
# root
./waf configure --build-static --with-python --with-cpptests --with-examples --with-vamp --with-gaia
./waf
./waf install
```

# Misc

```
# apt-get install libsox-dev
# pip install sox python_speech_features pydub
```

## Data Z

- http://marsyas.info/downloads/datasets.html
- http://www.ifs.tuwien.ac.at/mir/msd/download.html
- https://labrosa.ee.columbia.edu/millionsong/

(classifier.py cv = ShuffleSplit(len(X), 1, 0.3)
++(instrument {rock, blues, metal, prog, alt)...

- https://github.com/jazdev/genreXpose

- https://github.com/danz1ka19/Music-Emotion-Recognition

## suggest tone /etc

http://scikit-learn.org/stable/modules/feature_selection.html
https://mpatacchiola.github.io/blog/2016/11/12/the-simplest-classifier-histogram-intersection.html

## tmp
https://machinelearningmastery.com/moving-average-smoothing-for-time-series-forecasting-python/
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
http://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html#sphx-glr-auto-examples-linear-model-plot-robust-fit-py
https://www.scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html
- https://github.com/raulsoutelo/Music-genre-classification-with-the-Million-Song-Dataset

http://essentia.upf.edu/documentation/essentia_python_examples.html
http://thomas-cokelaer.info/software/spectrum/html/user/ref_others.html#id4
http://essentia.upf.edu/documentation/reference/streaming_Spectrum.html

https://machinelearningmastery.com/effect-size-measures-in-python/
https://machinelearningmastery.com/how-to-make-classification-and-regression-predictions-for-deep-learning-models-in-keras/
http://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#sphx-glr-auto-examples-neighbors-plot-kde-1d-py

https://github.com/briandwendt/Arduino-Python-4-Axis-Servo

https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html

- isSinging()
- isShreding()
- sceneChange..
...
