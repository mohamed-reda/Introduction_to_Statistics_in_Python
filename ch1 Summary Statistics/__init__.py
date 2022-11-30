"""
Summary statistics:
import numpy as np
np.mean(car_speeds['speed_mph'])

Measures of center: median
msleep['sleep_total'].sort_values()
np.median(msleep['sleep_total']) = msleep['sleep_total'].sort_values().iloc[{#the medal index}]


Measures of center: mode( the most frequent value)
statistics.mode(msleep['vore']) #vore is the name of the column


Adding an outlier:
msleep[msleep['vore'] == "insecti"]['sleep_total'].agg([np.mean, np.median])

-------------------------------------------------------------------------------------------

Calculating variance: (Average distance from each data point to the data's mean):
1. Subtract mean from each data point:
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])

2. Square each distance:
sq_dists = dists ** 2

3. Sum squared distances:
sum_sq_dists = np.sum(sq_dists)

4.Divide by number of data points - 1:
variance = sum_sq_dists / (83 - 1)

or: (Without ddof=1 , population variance is calculated instead of sample variance)
np.var(msleep['sleep_total'], ddof=1)

---
Standard deviation
np.sqrt(np.var(msleep['sleep_total'], ddof=1))
=:
np.std(msleep['sleep_total'], ddof=1)
---

Mean absolute deviation (the average distance between each data point and the mean.
                            It gives us an idea about the variability in a dataset.)
# let's say that mean(msleep$sleep_total) is the np.mean:
dists = msleep['sleep_total'] - mean(msleep$sleep_total)
np.mean(np.abs(dists))

# Note, Standard deviation vs. mean absolute deviation:
- Standard deviation squares distances, penalizing longer distances more than shorter ones.
- Mean absolute deviation penalizes each distance equally.
- One isn't better than the other, but SD is more common than MAD.

---
Quantiles
np.quantile(msleep['sleep_total'], 0.5)

Boxplots use quartiles:
# import matplotlib.pyplot as plt
plt.boxplot(msleep['sleep_total'])
plt.show()

Quantiles using np.linspace():
# Quantiles are the set of values/points that divides the dataset into groups of equal size.
Quantiles askkkkkkkkkkkkkkkkkkkkk
np.quantile(msleep['sleep_total'], 0.5)
# 0.5 quantile = median
np.quantile(msleep['sleep_total'], [0, 0.2, 0.4, 0.6, 0.8, 1])

np.linspace(start, stop, num)
np.quantile(msleep['sleep_total'], np.linspace(0, 1, 5))

Interquartile range (IQR)
Height of the box in a boxplot
np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25)
from scipy.stats import iqr

iqr(msleep['sleep_total'])

Finding outliers
from scipy.stats import iqr
iqr = iqr(msleep['bodywt'])
lower_threshold = np.quantile(msleep['bodywt'], 0.25) - 1.5 * iqr
upper_threshold = np.quantile(msleep['bodywt'], 0.75) + 1.5 * iqr
msleep[(msleep['bodywt'] < lower_threshold) | (msleep['bodywt'] > upper_threshold)]

All in one go
msleep['bodywt'].describe()

















"""
