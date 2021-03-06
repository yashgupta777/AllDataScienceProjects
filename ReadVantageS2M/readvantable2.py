import numpy as np
import pandas as pd
import statistics
import math
import csv
# PA_Score_rhym	PA_Score_sub	RC_Score_Factual_QA	Inf_QA	RCIdea	RCRelatingNewInfo

df = pd.read_csv('C:/Users/Yash/PycharmProjects/ReadVantageS2M/input/TestFast2.csv')
groupby_school_PA_Score = df['PA_Score_1'].groupby(df['School'])
groupby_school_P_Score = df['PA_Score_2'].groupby(df['School'])
groupby_school_RC_Score_RC_Score_Factual_QA= df['PA_Score_3'].groupby(df['School'])
groupby_school_RC_Score_RC_Score_Inf_QA= df['PA_Score_4'].groupby(df['School'])
groupby_school_RC_Score_RC_Score_RCAnsStoryElements= df['C_Score_1'].groupby(df['School'])
groupby_school_RC_Score_RC_Score_RCIdea= df['C_Score_2'].groupby(df['School'])
# groupby_school_RC_Score_RC_Score_RCEvaluatingText= df['C_Score_3'].groupby(df['School'])
# groupby_school_RC_Score_RC_Score_RCMultipleStep= df['C_Score_4'].groupby(df['School'])
# groupby_school_RC_Score_RC_Score_RCRelatingNewInfo= df['C_Score_5'].groupby(df['School'])
# groupby_school_WUF_Score_WUF_Unknown= df['WUF_Unknown'].groupby(df['School'])
# groupby_school_WUF_Score_WUF_Both= df['WUF_Both'].groupby(df['School'])
# groupby_school_WUF_Score_WUF_Known= df['WUF_Known'].groupby(df['School'])
groupby_school = df.groupby(df['School'])
for group in groupby_school:
    # print(groupby_school.describe())
    groupby_school_PA_Score_max = groupby_school_PA_Score.max()
    groupby_school_PA_Score_min = groupby_school_PA_Score.min()
    groupby_school_PA_Score_av = groupby_school_PA_Score.mean()
    groupby_school_P_Score_max = groupby_school_P_Score.max()
    groupby_school_P_Score_min = groupby_school_P_Score.min()
    groupby_school_P_Score_av = groupby_school_P_Score.mean()
    groupby_school_RC_Score_RC_Score_Factual_QA_max = groupby_school_RC_Score_RC_Score_Factual_QA.max()
    groupby_school_RC_Score_RC_Score_Factual_QA_min = groupby_school_RC_Score_RC_Score_Factual_QA.min()
    groupby_school_RC_Score_RC_Score_Factual_QA_av = groupby_school_RC_Score_RC_Score_Factual_QA.mean()
    groupby_school_RC_Score_RC_Score_Inf_QA_max = groupby_school_RC_Score_RC_Score_Inf_QA.max()
    groupby_school_RC_Score_RC_Score_Inf_QA_min = groupby_school_RC_Score_RC_Score_Inf_QA.min()
    groupby_school_RC_Score_RC_Score_Inf_QA_av = groupby_school_RC_Score_RC_Score_Inf_QA.mean()
    groupby_school_RC_Score_RC_Score_RCAnsStoryElements_max = groupby_school_RC_Score_RC_Score_RCAnsStoryElements.max()
    groupby_school_RC_Score_RC_Score_RCAnsStoryElements_min = groupby_school_RC_Score_RC_Score_RCAnsStoryElements.min()
    groupby_school_RC_Score_RC_Score_RCAnsStoryElements_av = groupby_school_RC_Score_RC_Score_RCAnsStoryElements.mean()
    groupby_school_RC_Score_RC_Score_RCIdea_max = groupby_school_RC_Score_RC_Score_RCIdea.max()
    groupby_school_RC_Score_RC_Score_RCIdea_min = groupby_school_RC_Score_RC_Score_RCIdea.min()
    groupby_school_RC_Score_RC_Score_RCIdea_av = groupby_school_RC_Score_RC_Score_RCIdea.mean()
    # groupby_school_RC_Score_RC_Score_RCEvaluatingText_max = groupby_school_RC_Score_RC_Score_RCEvaluatingText.max()
    # groupby_school_RC_Score_RC_Score_RCEvaluatingText_min = groupby_school_RC_Score_RC_Score_RCEvaluatingText.min()
    # groupby_school_RC_Score_RC_Score_RCEvaluatingText_av = groupby_school_RC_Score_RC_Score_RCEvaluatingText.mean()
    # groupby_school_RC_Score_RC_Score_RCMultipleStep_max = groupby_school_RC_Score_RC_Score_RCMultipleStep.max()
    # groupby_school_RC_Score_RC_Score_RCMultipleStep_min = groupby_school_RC_Score_RC_Score_RCMultipleStep.min()
    # groupby_school_RC_Score_RC_Score_RCMultipleStep_av = groupby_school_RC_Score_RC_Score_RCMultipleStep.mean()
    # groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_max = groupby_school_RC_Score_RC_Score_RCRelatingNewInfo.max()
    # groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_min = groupby_school_RC_Score_RC_Score_RCRelatingNewInfo.min()
    # groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_av = groupby_school_RC_Score_RC_Score_RCRelatingNewInfo.mean()
    # groupby_school_WUF_Score_WUF_Unknown_max = groupby_school_WUF_Score_WUF_Unknown.max()
    # groupby_school_WUF_Score_WUF_Unknown_min = groupby_school_WUF_Score_WUF_Unknown.min()
    # groupby_school_WUF_Score_WUF_Unknown_av = groupby_school_WUF_Score_WUF_Unknown.mean()
    # groupby_school_WUF_Score_WUF_Both_max = groupby_school_WUF_Score_WUF_Both.max()
    # groupby_school_WUF_Score_WUF_Both_min = groupby_school_WUF_Score_WUF_Both.min()
    # groupby_school_WUF_Score_WUF_Both_av = groupby_school_WUF_Score_WUF_Both.mean()
    # groupby_school_WUF_Score_WUF_Known_max = groupby_school_WUF_Score_WUF_Known.max()
    # groupby_school_WUF_Score_WUF_Known_min = groupby_school_WUF_Score_WUF_Known.min()
    # groupby_school_WUF_Score_WUF_Known_av = groupby_school_WUF_Score_WUF_Known.mean()
    print(groupby_school_PA_Score_max)
    print(groupby_school_PA_Score_min)
    print(groupby_school_PA_Score_av)
    print(groupby_school_P_Score_max)
    print(groupby_school_P_Score_min)
    print(groupby_school_P_Score_av)
    print(groupby_school_RC_Score_RC_Score_Factual_QA_max)
    print(groupby_school_RC_Score_RC_Score_Factual_QA_min)
    print(groupby_school_RC_Score_RC_Score_Factual_QA_av)
    print(groupby_school_RC_Score_RC_Score_Inf_QA_max)
    print(groupby_school_RC_Score_RC_Score_Inf_QA_min)
    print(groupby_school_RC_Score_RC_Score_Inf_QA_av)
    print(groupby_school_RC_Score_RC_Score_RCAnsStoryElements_max)
    print(groupby_school_RC_Score_RC_Score_RCAnsStoryElements_min)
    print(groupby_school_RC_Score_RC_Score_RCAnsStoryElements_av)
    print(groupby_school_RC_Score_RC_Score_RCIdea_max)
    print(groupby_school_RC_Score_RC_Score_RCIdea_min)
    print(groupby_school_RC_Score_RC_Score_RCIdea_av)
    # print(groupby_school_RC_Score_RC_Score_RCEvaluatingText_max)
    # print(groupby_school_RC_Score_RC_Score_RCEvaluatingText_min)
    # print(groupby_school_RC_Score_RC_Score_RCEvaluatingText_av)
    # print(groupby_school_RC_Score_RC_Score_RCMultipleStep_max)
    # print(groupby_school_RC_Score_RC_Score_RCMultipleStep_min)
    # print(groupby_school_RC_Score_RC_Score_RCMultipleStep_av)
    # print(groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_max)
    # print(groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_min)
    # print(groupby_school_RC_Score_RC_Score_RCRelatingNewInfo_av)
    # print(groupby_school_WUF_Score_WUF_Unknown_max)
    # print(groupby_school_WUF_Score_WUF_Unknown_min)
    # print(groupby_school_WUF_Score_WUF_Unknown_av)
    # print(groupby_school_WUF_Score_WUF_Both_max)
    # print(groupby_school_WUF_Score_WUF_Both_min)
    # print(groupby_school_WUF_Score_WUF_Both_av)
    # print(groupby_school_WUF_Score_WUF_Known_max)
    # print(groupby_school_WUF_Score_WUF_Known_min)
    # print(groupby_school_WUF_Score_WUF_Known_av)





