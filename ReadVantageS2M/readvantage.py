import numpy as np
import pandas as pd
import statistics
import math
import csv

df = pd.read_csv('C:/Users/Yash/PycharmProjects/ReadVantageS2M/input/TFIfast2.csv')
groupby_school_PA_Score = df['PA_Score'].groupby(df['School'])
groupby_school_P_Score = df['P_Score'].groupby(df['School'])
groupby_school_RC_Score= df['C_Score'].groupby(df['School'])
# groupby_school_WUF_Score= df['WUF_Score'].groupby(df['School'])
groupby_school_Overall= df['OverAllTotal Score'].groupby(df['School'])
				# PA_Score_1	PA_Score_2	PA_Score_3	PA_Score_4	C_Score_1	C_Score_2	C_Score_3	C_Score_4	C_Score_5

groupby_school = df.groupby(df['School'])
for group in groupby_school:
    # print(groupby_school.describe())
    groupby_school_Overall_max = groupby_school_Overall.max()
    groupby_school_Overall_min = groupby_school_Overall.min()
    groupby_school_Overall_av = groupby_school_Overall.mean()
    groupby_school_PA_Score_max = groupby_school_PA_Score.max()
    groupby_school_PA_Score_min = groupby_school_PA_Score.min()
    groupby_school_PA_Score_av = groupby_school_PA_Score.mean()
    groupby_school_P_Score_max = groupby_school_P_Score.max()
    groupby_school_P_Score_min = groupby_school_P_Score.min()
    groupby_school_P_Score_av = groupby_school_P_Score.mean()
    groupby_school_RC_Score_max = groupby_school_RC_Score.max()
    groupby_school_RC_Score_min = groupby_school_RC_Score.min()
    groupby_school_RC_Score_av = groupby_school_RC_Score.mean()
    # groupby_school_WUF_Score_max = groupby_school_WUF_Score.max()
    # groupby_school_WUF_Score_min = groupby_school_WUF_Score.min()
    # groupby_school_WUF_Score_av = groupby_school_WUF_Score.mean()
    print(groupby_school_Overall_max)
    print(groupby_school_Overall_min)
    print(groupby_school_Overall_av)
    print(groupby_school_PA_Score_max)
    print(groupby_school_PA_Score_min)
    print(groupby_school_PA_Score_av)
    print(groupby_school_P_Score_max)
    print(groupby_school_P_Score_min)
    print(groupby_school_P_Score_av)
    print(groupby_school_RC_Score_max)
    print(groupby_school_RC_Score_min)
    print(groupby_school_RC_Score_av)
    # print(groupby_school_WUF_Score_max)
    # print(groupby_school_WUF_Score_min)
    # print(groupby_school_WUF_Score_av)



