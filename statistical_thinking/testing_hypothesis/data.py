from numpy import array

rain_july = array([66.2, 39.7, 76.4, 26.5, 11.2, 61.8, 6.1, 48.4,
                   89.2, 104., 34., 60.6, 57.1, 79.1, 90.9, 32.3,
                   63.8, 78.2, 27.5, 43.4, 30.1, 17.3, 77.5, 44.9,
                   92.2, 39.6, 79.4, 66.1, 53.5, 98.5, 20.8, 55.5,
                   39.6, 56., 65.1, 14.8, 13.2, 88.1, 8.4, 32.1,
                   19.6, 40.4, 2.2, 77.5, 105.4, 77.2, 38., 27.1,
                   111.8, 17.2, 26.7, 23.3, 77.2, 87.2, 27.7, 50.6,
                   60.3, 15.1, 6., 29.4, 39.3, 56.3, 80.4, 85.3,
                   68.4, 72.5, 13.3, 28.4, 14.7, 37.4, 49.5, 57.2,
                   85.9, 82.1, 31.8, 126.6, 30.7, 41.4, 33.9, 13.5,
                   99.1, 70.2, 91.8, 61.3, 13.7, 54.9, 62.5, 24.2,
                   69.4, 83.1, 44., 48.5, 11.9, 16.6, 66.4, 90.,
                   34.9, 132.8, 33.4, 225., 7.6, 40.9, 76.5, 48.,
                   140., 55.9, 54.1, 46.4, 68.6, 52.2, 108.3, 14.6,
                   11.3, 29.8, 130.9, 152.4, 61., 46.6, 43.9, 30.9,
                   111.1, 68.5, 42.2, 9.8, 285.6, 56.7, 168.2, 41.2,
                   47.8, 166.6, 37.8, 45.4, 43.2])

rain_november = array([83.6, 30.9, 62.2, 37., 41., 160.2, 18.2, 122.4,
                       71.3, 44.2, 49.1, 37.6, 114.5, 28.8, 82.5, 71.9,
                       50.7, 67.7, 112., 63.6, 42.8, 57.2, 99.1, 86.4,
                       84.4, 38.1, 17.7, 102.2, 101.3, 58., 82., 101.4,
                       81.4, 100.1, 54.6, 39.6, 57.5, 29.2, 48.8, 37.3,
                       115.4, 55.6, 62., 95., 84.2, 118.1, 153.2, 83.4,
                       104.7, 59., 46.4, 50., 147.6, 76.8, 59.9, 101.8,
                       136.6, 173., 92.5, 37., 59.8, 142.1, 9.9, 158.2,
                       72.6, 28., 112.9, 119.3, 199.2, 50.7, 44., 170.7,
                       67.2, 21.4, 61.3, 15.6, 106., 116.2, 42.3, 38.5,
                       132.5, 40.8, 147.5, 93.9, 71.4, 87.3, 163.7, 141.4,
                       62.6, 84.9, 28.8, 121.1, 28.6, 32.4, 112., 50.,
                       96.9, 81.8, 70.4, 117.5, 41.2, 124.9, 78.2, 93.,
                       53.5, 50.5, 42.6, 47.9, 73.1, 129.1, 56.9, 103.3,
                       60.5, 134.3, 93.1, 49.5, 48.2, 167.9, 27., 111.1,
                       55.4, 36.2, 57.4, 66.8, 58.3, 60., 161.6, 112.7,
                       37.4, 110.6, 56.6, 95.8, 126.8])

frog_data = {'ID': {20: 'A',
                    21: 'A',
                    22: 'A',
                    23: 'A',
                    24: 'A',
                    25: 'A',
                    26: 'A',
                    27: 'A',
                    28: 'A',
                    29: 'A',
                    30: 'A',
                    31: 'A',
                    32: 'A',
                    33: 'A',
                    34: 'A',
                    35: 'A',
                    36: 'A',
                    37: 'A',
                    38: 'A',
                    39: 'A',
                    60: 'B',
                    61: 'B',
                    62: 'B',
                    63: 'B',
                    64: 'B',
                    65: 'B',
                    66: 'B',
                    67: 'B',
                    68: 'B',
                    69: 'B',
                    70: 'B',
                    71: 'B',
                    72: 'B',
                    73: 'B',
                    74: 'B',
                    75: 'B',
                    76: 'B',
                    77: 'B',
                    78: 'B',
                    79: 'B'},
             'impact_force': {20: 1.6120000000000001,
                              21: 0.60499999999999998,
                              22: 0.32700000000000001,
                              23: 0.94599999999999995,
                              24: 0.54100000000000004,
                              25: 1.5389999999999999,
                              26: 0.52900000000000003,
                              27: 0.628,
                              28: 1.4530000000000001,
                              29: 0.29699999999999999,
                              30: 0.70299999999999996,
                              31: 0.26900000000000002,
                              32: 0.751,
                              33: 0.245,
                              34: 1.1819999999999999,
                              35: 0.51500000000000001,
                              36: 0.435,
                              37: 0.38300000000000001,
                              38: 0.45700000000000002,
                              39: 0.72999999999999998,
                              60: 0.17199999999999999,
                              61: 0.14199999999999999,
                              62: 0.036999999999999998,
                              63: 0.45300000000000001,
                              64: 0.35499999999999998,
                              65: 0.021999999999999999,
                              66: 0.502,
                              67: 0.27300000000000002,
                              68: 0.71999999999999997,
                              69: 0.58199999999999996,
                              70: 0.19800000000000001,
                              71: 0.19800000000000001,
                              72: 0.59699999999999998,
                              73: 0.51600000000000001,
                              74: 0.81499999999999995,
                              75: 0.40200000000000002,
                              76: 0.60499999999999998,
                              77: 0.71099999999999997,
                              78: 0.61399999999999999,
                              79: 0.46800000000000003}}

# frog_df = pd.DataFrame.from_dict(frog_data)
# print(frog_df.head())
# print(np.mean(rain_november))
