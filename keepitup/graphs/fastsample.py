import numpy as np
import pandas as pd
import statistics
import math
import csv

df = pd.read_csv('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/Fast3Score.csv')
# #print(df.School)
# groupBySchool = df.groupby(['School']).groups
# # groupBySchoolStudent = groupBySchool(['WOW_Teacher'])
# for group in groupBySchool:
#     # df_totalScore = group['totalScore'].max
#     groupeddf_max = df.groupby(['School'])['TotalScore'].max()
#     groupeddf_mean = df.groupby(['School'])['TotalScore'].mean()
#     groupeddf_min = df.groupby(['School'])['TotalScore'].min()
#     groupeddf_teacher = df.groupby(['School'])['WOW_Teacher'].
#     groupeddf_max_per = (groupeddf_max / 61) * 100
#     groupeddf_min_per = (groupeddf_min / 61) * 100
#     groupeddf_mean_per = (groupeddf_mean / 61) * 100
#     print(group,groupeddf_max,groupeddf_max_per,groupeddf_mean,groupeddf_mean_per,groupeddf_min_per, groupeddf_min)
#
#     print(groupeddf_teacher.sort(True))
# Create a groupby variable that groups preTestScores by regiment
groupby_school_WordUseTotal = df['WordUseTotal'].groupby(df['School'])
groupby_school_RC = df['RCTotal'].groupby(df['School'])
# for ChildFirstName, group in groupby_school_RC:
#     print(groupby_school_RC.describe())
#     print(groupby_school_RC.max()/61*100)
#     print(groupby_school_RC.min()/61*100)
#     print(groupby_school_RC .mean()/61*100)
groupby_school_PhonicsTotal= df['PhonicsTotal'].groupby(df['School'])
groupby_school_PhonemicTotal= df['PhonemicTotal'].groupby(df['School'])
groupby_school = df['TotalScore'].groupby(df['School'])
for group in groupby_school:
    # print(groupby_school.describe())
    groupby_school_max =groupby_school.max()/50 *100
    groupby_school_min = groupby_school.min() / 50 * 100
    groupby_school_mean= groupby_school.mean() / 50 * 100
    groupby_school_PhonemicTotal_max = groupby_school_PhonemicTotal.max() / 10 * 100
    groupby_school_PhonemicTotal_min = groupby_school_PhonemicTotal.min() / 10 * 100
    groupby_school_PhonemicTotal_mean = groupby_school_PhonemicTotal.mean() / 10 * 100
    groupby_school_PhonicsTotal_max =groupby_school_PhonicsTotal.max() / 10 * 100
    groupby_school_PhonicsTotal_min = groupby_school_PhonicsTotal.min() / 10 * 100
    groupby_school_PhonicsTotal_mean = groupby_school_PhonicsTotal.mean() / 10 * 100
    groupby_school_RC_max = groupby_school_RC.max() / 20 * 100
    groupby_school_RC_min = groupby_school_RC.min() / 20 * 100
    groupby_school_RC_mean = groupby_school_RC.mean() / 20 * 100
    groupby_school_WordUseTotal_max = groupby_school_WordUseTotal.max() / 10 * 100
    groupby_school_WordUseTotal_min = groupby_school_WordUseTotal.min() / 10 * 100
    groupby_school_WordUseTotal_mean = groupby_school_WordUseTotal.mean() / 10 * 100
# print(groupby_school_min)
# with open ('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/blank.csv' , 'w',newline='')as f:
#     writecsv = csv.writer(f)
#     for i in range(1, 100):
#         writecsv.writerow([groupby_school_min])
#
#     print(groupby_school.max()/61*100)
#     print(groupby_school.min()/61*100)
#     print(groupby_school.mean()/61*100)
#     print(groupby_school_PhonemicTotal.describe())
#     print(groupby_school_PhonemicTotal.max() / 33 * 100)
#     print(groupby_school_PhonemicTotal.min() / 33 * 100)
#     print(groupby_school_PhonemicTotal.mean() / 33 * 100)
#     print(groupby_school_PhonicsTotal.describe())
#     print(groupby_school_PhonicsTotal.max() / 12 * 100)
#     print(groupby_school_PhonicsTotal.min() / 12 * 100)
#     print(groupby_school_PhonicsTotal.mean() / 12 * 100)
#     print(groupby_school_RC.describe())
#     print(groupby_school_RC.max() / 16 * 100)
#     print(groupby_school_RC.min() / 16 * 100)
#     print(groupby_school_RC.mean() / 16 * 100)
#
# # print(list(df['TotalScore'].groupby(df['School'])))
#
with open('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/fastwrite4.csv','w',newline='') as f:
    thewriter =csv.writer(f)
    thewriter.writerow(['Max','Min','Mean','MaxPhonemic','MinPhonemic','MeanPhonemic','MaxPhonics','MinPhonics','MeanPhonics', 'MaxRC','MinRC','MeanRC','MaxWUF','MinWUF','MeanWUF'])
    for i in range(1,1000000000000000):
        thewriter.writerow([groupby_school_max,groupby_school_min, groupby_school_mean,groupby_school_PhonemicTotal_max ,groupby_school_PhonemicTotal_min,groupby_school_PhonemicTotal_mean,groupby_school_PhonicsTotal_max,groupby_school_PhonicsTotal_min,groupby_school_PhonicsTotal_mean,groupby_school_RC_max,groupby_school_RC_min ,groupby_school_RC_mean,groupby_school_WordUseTotal_max,groupby_school_WordUseTotal_min,groupby_school_WordUseTotal_mean ])
# # groupby_school_np = np.array(groupby_school)
# # print(groupby_school_np)
