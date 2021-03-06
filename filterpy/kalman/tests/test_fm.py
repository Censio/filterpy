# -*- coding: utf-8 -*-
"""Copyright 2015 Roger R Labbe Jr.

FilterPy library.
http://github.com/rlabbe/filterpy

Documentation at:
https://filterpy.readthedocs.org

Supporting book at:
https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python

This is licensed under an MIT license. See the readme.MD file
for more information.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy.random as random
import numpy as np
import warnings
from filterpy.kalman import FadingKalmanFilter

def test_noisy_1d():
    f = FadingKalmanFilter (5., dim_x=2, dim_z=1)

    f.X = np.array([[2.],
                    [0.]])       # initial state (location and velocity)

    f.F = np.array([[1.,1.],
                    [0.,1.]])    # state transition matrix

    f.H = np.array([[1.,0.]])    # Measurement function
    f.P *= 1000.                  # covariance matrix
    f.R = 5                       # state uncertainty
    f.Q = 0.0001                 # process uncertainty

    measurements = []
    results = []

    zs = []
    for t in range (100):
        # create measurement = t plus white noise
        z = t + random.randn()*20
        zs.append(z)

        # perform kalman filtering
        f.update(z)
        f.predict()

        # save data
        results.append (f.X[0,0])
        measurements.append(z)


    # now do a batch run with the stored z values so we can test that
    # it is working the same as the recursive implementation.
    # give slightly different P so result is slightly different
    f.X = np.array([[2.,0]]).T
    f.P = np.eye(2)*100.
    m,c,_,_ = f.batch_filter(zs,update_first=False)
