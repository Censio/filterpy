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
from filterpy.kalman import SquareRootKalmanFilter, KalmanFilter

def test_noisy_1d():
    f = KalmanFilter (dim_x=2, dim_z=1)

    f.x = np.array([[2.],
                    [0.]])       # initial state (location and velocity)

    f.F = np.array([[1.,1.],
                    [0.,1.]])    # state transition matrix

    f.H = np.array([[1.,0.]])    # Measurement function
    f.P *= 1000.                  # covariance matrix
    f.R = 5                       # state uncertainty
    f.Q = 0.0001                 # process uncertainty

    fsq = SquareRootKalmanFilter (dim_x=2, dim_z=1)

    fsq.x = np.array([[2.],
                      [0.]])     # initial state (location and velocity)

    fsq.F = np.array([[1.,1.],
                      [0.,1.]])  # state transition matrix

    fsq.H = np.array([[1.,0.]])  # Measurement function
    fsq.P = np.eye(2) * 1000.    # covariance matrix
    fsq.R = 5                    # state uncertainty
    fsq.Q = 0.0001               # process uncertainty

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

        fsq.update(z)
        fsq.predict()

        assert abs(f.x[0,0] - fsq.x[0,0]) < 1.e-12
        assert abs(f.x[1,0] - fsq.x[1,0]) < 1.e-12

        # save data
        results.append (f.x[0,0])
        measurements.append(z)


    p = f.P - fsq.P
    print(f.P)
    print(fsq.P)

    for i in range(f.P.shape[0]):
        assert abs(f.P[i,i] - fsq.P[i,i]) < 0.01


    # now do a batch run with the stored z values so we can test that
    # it is working the same as the recursive implementation.
    # give slightly different P so result is slightly different
    f.x = np.array([[2.,0]]).T
    f.P = np.eye(2)*100.
    m,c,_,_ = f.batch_filter(zs,update_first=False)

