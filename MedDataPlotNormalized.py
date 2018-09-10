# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:28:40 2018

@author: Nita
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if(len(sys.argv) == 1):
    print("Please enter the complete path of the csv file. Ex: C:/your/folder/name/filename.csv")
    sys.exit
else:
    #Set up Fonts for the text on the plot
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 24}
    plt.rc('font', **font)

    medData=pd.read_csv(sys.argv[1])
    medDataDf = pd.DataFrame(medData)
    print(medDataDf)

    #add a new column identifying rows with RestBP >200
    medDataDf['HighRestBP']=medDataDf['RestBP'].apply(lambda x: x > 120)

    binLabels=['T.Angina/Normal BP', 'T.Angina/High BP', 'AT.Angina/Normal BP', 'AT.Angina/High BP', 'Non Angina/Normal BP', 'Non Angina/High BP', 'Asymptomatic/Normal BP' , 'Asymptomatic/High BP']
    #group data by patients with/without chest pain and normal/high resting BP
    procData=medDataDf.groupby(['ChestPain','HighRestBP']).size().reset_index(name='patient_count')
    val_cts = medDataDf.ChestPain.value_counts()
    #normalize the data
    norm_data= procData['patient_count'].div(procData['ChestPain'].map(val_cts)/100)
    #plot the data as a bar graph
    barPlot = norm_data.plot.bar(rot=0, color="b", figsize=(20,15))
    barPlot.set_xticklabels(binLabels, rotation=40, ha='right')
    barPlot.set_ylabel('Normalized Patient Set', labelpad=10)
    barPlot.set_xlabel('Chest Pain, Resting BP', labelpad=10)
    barPlot.set_title('Normalized Patient Count')