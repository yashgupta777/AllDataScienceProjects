import numpy as np
import pandas as pd
import statistics
import math
import csv

df = pd.read_csv('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/ab.csv')
groupby_school_Compre = df['Compre'].groupby(df['School'])
groupby_school_Vocab = df['Vocab'].groupby(df['School'])
groupby_school_TotalTime= df['TotalTime'].groupby(df['School'])
groupby_school_FINAL= df['Final Score'].groupby(df['School'])


groupby_school = df.groupby(df['School'])
for group in groupby_school:
    # print(groupby_school.describe())
    groupby_school_Compre_av = groupby_school_Compre.mean()
    groupby_school_Vocab_av = groupby_school_Vocab.mean()
    groupby_school_TotalTime_av = groupby_school_TotalTime.mean() / 60
    school_min_compre = groupby_school_Compre.min()
    school_max_compre = groupby_school_Compre.max()
    school_min_Vocab = groupby_school_Vocab.min()
    school_max_Vocab = groupby_school_Vocab.max()
    groupby_school_FINAL_av = groupby_school_FINAL.mean()
    print(groupby_school_FINAL_av)
    print(groupby_school_TotalTime_av)
    print(groupby_school_Compre_av)
    print(groupby_school_Vocab_av)
    print(school_min_compre)
    print(school_max_compre)
    print(school_min_Vocab)
    print(school_max_Vocab)

    # # print(groupby_school_TotalTime_av)
    # print(df.groupby(df['School']).groups)

# groupby_school_TotalTime_av.to_csv('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/text.txt', index=False)
# print('Done')
# with open('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/fastresultblank.csv','w',newline='') as f:
#     thewriter =csv.writer(f)
#     thewriter.writerow(['Average time taken in mins'])
#     for i in range(1,500):
#         thewriter.writerow([groupby_school_TotalTime_av])
# # groupby_school_np = np.array(groupby_school)
# # print(groupby_school_np)
#
#
#
# with open('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/fastwrite11.csv','w',newline='') as f:
#     thewriter =csv.writer(f)
#     thewriter.writerow(['groupby_school_TotalTime_av','School average score:Compre',
#                         'School average score:Vocab',
#                         'School minimum score:Compre',
#                         'School maximum score:Compre',
#                         'School minimum score:Vocab',
#                         'School maximum score:Vocab','groupby_school_FINAL_av'])
#     for i in range(1,100000):
#         thewriter.writerow([groupby_school_TotalTime_av,groupby_school_Compre_av,groupby_school_Vocab_av,school_min_compre,school_max_compre,school_min_Vocab,school_max_Vocab,groupby_school_FINAL_av])
# #     print(groupby_school_TotalTime_av)
#     print(groupby_school_Compre_av)
#     print(groupby_school_Vocab_av)
#     print(school_min_compre)
#     print(school_max_compre)
#     print(groupby_school_Compre_av)
#     print(school_min_Vocab)
#     print(school_max_Vocab)
# # # print(groupby_school_np)
