# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:58:39 2018

@author: Mithra
"""
import datetime
from stackapi import StackAPI
import pandas as pd

def getData(tag):
    SITE = StackAPI('stackoverflow')
    SITE.max_pages=80
    questions = SITE.fetch('questions', fromdate=datetime.datetime(2017,1,1), todate=datetime.datetime(2018,1,1), tagged=tag, sort='votes')
    return questions['items']

def parseData(tagged_list):
    output=[]
    print(tagged_list[0][0])
    for tagged in tagged_list:
        tag_name=tagged[0]
        tag_list=tagged[1]
        print(tag_name)
        for item in tag_list:
            t=[item['tags'], item['question_id'], item['score']]
            output.append(t)
    return output

def finalData():
    t=[]
    tag_names=['python','apache']
    for tag in tag_names:
        t.append([tag,getData(tag)])
        print(t[0])
    final_list=pd.DataFrame(parseData(t))
    final_list.columns=['tags','question_id','score']
    final_list.to_csv('C:\\Users\\admin\\Desktop\\PythonPrep\\LDA with NMF\\output_getstack.csv')
    del t
