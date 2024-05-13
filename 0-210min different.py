import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Assuming data has been correctly loaded into a DataFrame
data = {
    "Time": np.arange(0, 215, 5),  # Time interval of 5 minutes, from 0 to 210 minutes
    "Average": [10.76, 10.71, 10.70, 10.61, 10.56, 10.46, 10.26, 10.10, 9.88, 9.61, 9.44, 9.24, 9.10, 9.02, 8.89, 8.70, 8.61, 8.50, 8.39, 8.23, 8.14, 8.13, 8.08, 8.08, 8.11, 8.13, 8.18, 8.15, 8.15, 8.20, 8.16, 8.15, 8.17, 8.18, 8.15, 8.25, 8.30, 8.40, 8.53, 8.65, 8.81, 9.15, 9.31],
    "Resistance": [9.95, 9.90, 9.82, 9.67, 9.51, 9.38, 9.15, 8.98, 8.83, 8.71, 8.60, 8.51, 8.44, 8.30, 8.24, 8.13, 8.02, 7.95, 7.84, 7.72, 7.72, 7.66, 7.60, 7.49, 7.35, 7.32, 7.30, 7.31, 7.30, 7.29, 7.39, 7.51, 7.64, 7.81, 7.97, 8.07, 8.17, 8.33, 8.39, 8.55, 8.65, 8.69, 8.73],
    "Mixed": [10.37, 10.41, 10.39, 10.33, 10.34, 10.33, 10.22, 10.17, 10.05, 9.95, 9.81, 9.70, 9.57, 9.45, 9.31, 9.23, 9.14, 9.05, 8.96, 8.90, 8.79, 8.70, 8.59, 8.58, 8.51, 8.43, 8.39, 8.33, 8.25, 8.12, 8.01, 8.01, 8.02, 7.97, 7.90, 7.79, 7.80, 7.78, 7.88, 8.00, 8.12, 8.25, 8.47]
}

df = pd.DataFrame(data)

# Find the time of the lowest blood sugar value for each group
min_time_avg = df["Time"][df["Average"].idxmin()]
min_time_resistance = df["Time"][df["Resistance"].idxmin()]
min_time_mixed = df["Time"][df["Mixed"].idxmin()]

# Prepare data for ANOVA analysis
min_times = [min_time_avg] * len(df[df["Average"] == df["Average"].min()]) + \
            [min_time_resistance] * len(df[df["Resistance"] == df["Resistance"].min()]) + \
            [min_time_mixed] * len(df[df["Mixed"] == df["Mixed"].min()])
groups = ['Average'] * len(df[df["Average"] == df["Average"].min()]) + \
         ['Resistance'] * len(df[df["Resistance"] == df["Resistance"].min()]) + \
         ['Mixed'] * len(df[df["Mixed"] == df["Mixed"].min()])

# ANOVA test
anova_result = stats.f_oneway(df["Time"][df["Average"] == df["Average"].min()],
                              df["Time"][df["Resistance"] == df["Resistance"].min()],
                              df["Time"][df["Mixed"] == df["Mixed"].min()])

print("ANOVA result:", anova_result)

# If ANOVA shows significant differences, perform Tukey HSD test
if anova_result.pvalue < 0.05:
    tukey_result = pairwise_tukeyhsd(endog=min_times, groups=groups, alpha=0.05)
    print(tukey_result.summary())
