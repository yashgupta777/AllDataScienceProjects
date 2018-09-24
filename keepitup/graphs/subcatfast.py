import numpy as np
import pandas as pd
import statistics
import math
import csv

df = pd.read_csv('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/Fast3Score.csv')
groupby_school_PhonicsSubSkill = df['PhonicsSubSkill'].groupby(df['School'])
groupby_school_PhonemicAwareRhyming = df['PhonemicAwareRhyming'].groupby(df['School'])
# groupby_school_PhonemicCreatingWord = df['PhonemicCreatingWord'].groupby(df['School'])
# groupby_school_PhonemicSupplying = df['PhonemicSupplying'].groupby(df['School'])
# groupby_school_PhonemicUsingKnowledge = df['PhonemicUsingKnowledge'].groupby(df['School'])
groupby_school_RCAnsQA = df['RCAnsQA'].groupby(df['School'])
groupby_school_RCAnsStoryElements = df['RCAnsStoryElements'].groupby(df['School'])
groupby_school_RCEvaluatingText = df['RCEvaluatingText'].groupby(df['School'])
groupby_school_RCRelatingNewInfo = df['RCRelatingNewInfo'].groupby(df['School'])
groupby_school_RCMultipleStep = df['RCMultipleStep'].groupby(df['School'])
groupby_school_RCAnsInQA = df['RCAnsInQA'].groupby(df['School'])
groupby_school_RCIdea = df['RCIdea'].groupby(df['School'])
groupby_school_WUFOnlyUnknown = df['WUFOnlyUnknown'].groupby(df['School'])
groupby_school_WUFBoth = df['WUFBoth'].groupby(df['School'])
groupby_school_WUFknown = df['WUFknown'].groupby(df['School'])

groupby_school = df['TotalScore'].groupby(df['School'])
for group in groupby_school:
    # print(groupby_school.describe())
    # groupby_school_max =groupby_school.max()/61*100
    # groupby_school_min = groupby_school.min() / 61 * 100
    # groupby_school_mean= groupby_school.mean() / 61 * 100
    groupby_school_PhonemicAwareRhyming_max = groupby_school_PhonemicAwareRhyming.max() / 10 * 100
    groupby_school_PhonemicAwareRhyming_min = groupby_school_PhonemicAwareRhyming.min() / 10 * 100
    groupby_school_PhonemicAwareRhyming_mean = groupby_school_PhonemicAwareRhyming.mean() / 10 * 100
    # groupby_school_PhonemicCreatingWord_max =groupby_school_PhonemicCreatingWord.max() / 5 * 100
    # groupby_school_PhonemicCreatingWord_min = groupby_school_PhonemicCreatingWord.min() / 5 * 100
    # groupby_school_PhonemicCreatingWord_mean = groupby_school_PhonemicCreatingWord.mean() / 5 * 100
    # groupby_school_PhonemicSupplying_max = groupby_school_PhonemicSupplying.max() / 10 * 100
    # groupby_school_PhonemicSupplying_min = groupby_school_PhonemicSupplying.min() / 10 * 100
    # groupby_school_PhonemicSupplying_mean = groupby_school_PhonemicSupplying.mean() / 10 * 100
    # groupby_school_PhonemicUsingKnowledge_max = groupby_school_PhonemicUsingKnowledge.max() / 8 * 100
    # groupby_school_PhonemicUsingKnowledge_min = groupby_school_PhonemicUsingKnowledge.min() / 8 * 100
    # groupby_school_PhonemicUsingKnowledge_mean = groupby_school_PhonemicUsingKnowledge.mean() / 8 * 100
    groupby_school_PhonicsSubSkill_max = groupby_school_PhonicsSubSkill.max() / 10 * 100
    groupby_school_PhonicsSubSkill_min = groupby_school_PhonicsSubSkill.min() / 10 * 100
    groupby_school_PhonicsSubSkill_mean = groupby_school_PhonicsSubSkill.mean() / 10 * 100
    groupby_school_RCAnsQA_max = groupby_school_RCAnsQA.max() / 5 * 100
    groupby_school_RCAnsQA_min = groupby_school_RCAnsQA.min() / 5 * 100
    groupby_school_RCAnsQA_mean = groupby_school_RCAnsQA.mean() / 5 * 100
    groupby_school_RCAnsInQA_max = groupby_school_RCAnsInQA.max() / 1 * 100
    groupby_school_RCAnsInQA_min = groupby_school_RCAnsInQA.min() / 1 * 100
    groupby_school_RCAnsInQA_mean = groupby_school_RCAnsInQA.mean() / 1 * 100
    groupby_school_RCAnsStoryElements_max = groupby_school_RCAnsStoryElements.max() / 5 * 100
    groupby_school_RCAnsStoryElements_min = groupby_school_RCAnsStoryElements.min() / 5 * 100
    groupby_school_RCAnsStoryElements_mean = groupby_school_RCAnsStoryElements.mean() / 5 * 100
    groupby_school_RCIdea_max = groupby_school_RCIdea.max() / 1 * 100
    groupby_school_RCIdea_min = groupby_school_RCIdea.min() / 1 * 100
    groupby_school_RCIdea_mean = groupby_school_RCIdea.mean() / 1 * 100
    groupby_school_RCEvaluatingText_max = groupby_school_RCEvaluatingText.max() / 2 * 100
    groupby_school_RCEvaluatingText_min = groupby_school_RCEvaluatingText.min() / 2 * 100
    groupby_school_RCEvaluatingText_mean = groupby_school_RCEvaluatingText.mean() / 2 * 100
    groupby_school_RCMultipleStep_max = groupby_school_RCMultipleStep.max() / 1 * 100
    groupby_school_RCMultipleStep_min = groupby_school_RCMultipleStep.min() / 1 * 100
    groupby_school_RCMultipleStep_mean = groupby_school_RCMultipleStep.mean() / 1 * 100
    groupby_school_RCRelatingNewInfo_max = groupby_school_RCRelatingNewInfo.max() / 5 * 100
    groupby_school_RCRelatingNewInfo_min = groupby_school_RCRelatingNewInfo.min() / 5 * 100
    groupby_school_RCRelatingNewInfo_mean = groupby_school_RCRelatingNewInfo.mean() / 5 * 100
    groupby_school_WUFOnlyUnknown_max = groupby_school_WUFOnlyUnknown.max() / 4 * 100
    groupby_school_WUFOnlyUnknown_min = groupby_school_WUFOnlyUnknown.min() / 4 * 100
    groupby_school_WUFOnlyUnknown_mean = groupby_school_WUFOnlyUnknown.mean() / 4 * 100
    groupby_school_WUFBoth_max = groupby_school_WUFBoth.max() / 3 * 100
    groupby_school_WUFBoth_min = groupby_school_WUFBoth.min() / 3 * 100
    groupby_school_WUFBoth_mean = groupby_school_WUFBoth.mean() / 3 * 100
    groupby_school_WUFknown_max = groupby_school_WUFknown.max() / 3 * 100
    groupby_school_WUFknown_min = groupby_school_WUFknown.min() / 3 * 100
    groupby_school_WUFknown_mean = groupby_school_WUFknown.mean() / 3 * 100

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
# with open('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/fastwrite1.csv','w',newline='') as f:
#     thewriter =csv.writer(f)
#     thewriter.writerow(['groupby_school_PhonemicAwareRhyming_max','groupby_school_PhonemicAwareRhyming_Min',
#                         'groupby_school_PhonemicAwareRhyming_Mean','groupby_school_PhonemicCreatingWord',
#                         'groupby_school_PhonemicCreatingWord','groupby_school_PhonemicCreatingWord',
#                         'groupby_school_PhonemicSupplying','groupby_school_PhonemicSupplying',
#                         'groupby_school_PhonemicSupplying', 'groupby_school_PhonemicUsingKnowledge',
#                         'groupby_school_PhonemicUsingKnowledge','groupby_school_PhonemicUsingKnowledge',
#                         'groupby_school_PhonicsSubSkill','groupby_school_PhonicsSubSkill','groupby_school_PhonicsSubSkill',
#                         'groupby_school_RCAnsQA','groupby_school_RCAnsQA','groupby_school_RCAnsQA',
#                         'groupby_school_RCAnsInQA','groupby_school_RCAnsInQA','groupby_school_RCAnsInQA',
#                         'groupby_school_RCIdea','groupby_school_RCIdea','groupby_school_RCIdea',
#                         'groupby_school_RCOrganising','groupby_school_RCOrganising','groupby_school_RCOrganising',
#                         'groupby_school_RCRelatingNewInfo','groupby_school_RCRelatingNewInfo','groupby_school_RCRelatingNewInfo'
#
#
#                         ])
#     for i in range(1,1000000000000000):
#         thewriter.writerow([groupby_school_PhonemicAwareRhyming_max,groupby_school_PhonemicAwareRhyming_min,
#                             groupby_school_PhonemicAwareRhyming_mean,groupby_school_PhonemicCreatingWord_max ,
#                             groupby_school_PhonemicCreatingWord_min,groupby_school_PhonemicCreatingWord_mean,
#                             groupby_school_PhonemicSupplying_max,groupby_school_PhonemicSupplying_min,
#                             groupby_school_PhonemicSupplying_mean,groupby_school_PhonemicUsingKnowledge_max,
#                             groupby_school_PhonemicUsingKnowledge_min ,groupby_school_PhonemicUsingKnowledge_mean,
#                             groupby_school_PhonicsSubSkill_max,groupby_school_PhonicsSubSkill_min,
#                             groupby_school_PhonicsSubSkill_mean,groupby_school_RCAnsQA_max,groupby_school_RCAnsQA_min,
#                             groupby_school_RCAnsQA_mean,groupby_school_RCAnsInQA_max,groupby_school_RCAnsInQA_min,
#                             groupby_school_RCAnsInQA_mean,groupby_school_RCIdea_max,groupby_school_RCIdea_min,
#                             groupby_school_RCIdea_mean,groupby_school_RCOrganising_max, groupby_school_RCOrganising_min,
#                             groupby_school_RCOrganising_mean,groupby_school_RCRelatingNewInfo_max,groupby_school_RCRelatingNewInfo_min,
#                             groupby_school_RCRelatingNewInfo_mean])
# # groupby_school_np = np.array(groupby_school)
# # print(groupby_school_np)
with open('C:/Users/Yash/PycharmProjects/keepitup/graphs/input/fastwrite5.csv','w',newline='') as f:
    thewriter =csv.writer(f)
    thewriter.writerow(['groupby_school_PhonemicAwareRhyming_max','groupby_school_PhonemicAwareRhyming_Min',
                        'groupby_school_PhonemicAwareRhyming_Mean',
                        'groupby_school_PhonicsSubSkill','groupby_school_PhonicsSubSkill','groupby_school_PhonicsSubSkill',
                        'groupby_school_RCAnsQA','groupby_school_RCAnsQA','groupby_school_RCAnsQA',
                        'groupby_school_RCAnsInQA','groupby_school_RCAnsInQA','groupby_school_RCAnsInQA',
                        'groupby_school_RCAnsStoryElements_max', 'groupby_school_RCAnsStoryElements_min', 'groupby_school_RCAnsStoryElements_mean',
                        'groupby_school_RCIdea','groupby_school_RCIdea','groupby_school_RCIdea',
                         'groupby_school_RCEvaluatingText_max','groupby_school_RCEvaluatingText_min','groupby_school_RCEvaluatingText_mean',
                        'groupby_school_RCMultipleStep_max','groupby_school_RCMultipleStep_min','groupby_school_RCMultipleStep_mean',
                        'groupby_school_RCRelatingNewInfo','groupby_school_RCRelatingNewInfo','groupby_school_RCRelatingNewInfo',
                        'groupby_school_WUFOnlyUnknown_max','groupby_school_WUFOnlyUnknown_min','groupby_school_WUFOnlyUnknown_mean',
                        'groupby_school_WUFBoth_max','groupby_school_WUFBoth_min','groupby_school_WUFBoth_mean','groupby_school_WUFknown_max',
                        'groupby_school_WUFknown_min','groupby_school_WUFknown_mean'

                        ])
    for i in range(1,1000000000000000):
        thewriter.writerow([groupby_school_PhonemicAwareRhyming_max,groupby_school_PhonemicAwareRhyming_min,
                            groupby_school_PhonemicAwareRhyming_mean,
                            groupby_school_PhonicsSubSkill_max,groupby_school_PhonicsSubSkill_min,
                            groupby_school_PhonicsSubSkill_mean,groupby_school_RCAnsQA_max,groupby_school_RCAnsQA_min,
                            groupby_school_RCAnsQA_mean,groupby_school_RCAnsInQA_max,groupby_school_RCAnsInQA_min,
                            groupby_school_RCAnsInQA_mean,
                            groupby_school_RCAnsStoryElements_max,groupby_school_RCAnsStoryElements_min,groupby_school_RCAnsStoryElements_mean,
                            groupby_school_RCIdea_max,groupby_school_RCIdea_min,
                            groupby_school_RCIdea_mean,
                            groupby_school_RCEvaluatingText_max,groupby_school_RCEvaluatingText_min,groupby_school_RCEvaluatingText_mean,
                            groupby_school_RCMultipleStep_max,groupby_school_RCMultipleStep_min,groupby_school_RCMultipleStep_mean,
                            groupby_school_RCRelatingNewInfo_max,groupby_school_RCRelatingNewInfo_min,
                            groupby_school_RCRelatingNewInfo_mean,groupby_school_WUFOnlyUnknown_max,groupby_school_WUFOnlyUnknown_min,
                            groupby_school_WUFOnlyUnknown_mean,groupby_school_WUFBoth_max,groupby_school_WUFBoth_min,
                            groupby_school_WUFBoth_mean,groupby_school_WUFknown_max,groupby_school_WUFknown_min,groupby_school_WUFknown_mean])
