# This combines data labelled manually by human.
# It should also deal with lemmatization and synonyms

import pandas
import os
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer as wnl
import nltk


def dec_to_binstr(n):
    result=""
    while n!=0:
        result=str(n%2)+result
        n=n//2
    return result

def binstr_to_dec(astr):
    result=0
    for x in astr:
        result=result*2+int(x)
    return result

def get_pos(astr):
    tag=nltk.pos_tag([astr])[0][1]
    if tag[0]=='J':
        return wordnet.ADJ
    elif tag[0]=='V':
        return wordnet.VERB
    elif tag[0]=='N':
        return wordnet.NOUN
    elif tag[0]=='R':
        return wordnet.ADV   
    return wordnet.NOUN

def get_lemma(astr):
    return wnl().lemmatize(astr,pos=get_pos(astr))

def check_lemma(a,b):
    a=get_lemma(a)
    b=get_lemma(b)
    if a==b:
        return True
    return False
#---------------------------------------------------------
# Combine keywords
fl_keywords=pandas.DataFrame(columns=['bias','keyword','againstgroup'])

filelist=[]
for x in os.listdir():
    if "keywords" in x:
        if x!="keywords_final.csv":
            filelist.append(x)


for x in filelist:
    tempfl=pandas.read_csv(x)
    #deal with duplicates
    exclusionlist=[]
    for y in range(len(tempfl)):
        for z in range(len(fl_keywords)):
            if check_lemma(tempfl.at[y,'keyword'],fl_keywords.at[z,'keyword']):
                fl_keywords.at[z,'againstgroup']=dec_to_binstr(binstr_to_dec(str(fl_keywords.at[z,'againstgroup'])) | binstr_to_dec(str(tempfl.at[y,'againstgroup'])))
                exclusionlist.append(y)
            fl_keywords.at[z,'keyword']=get_lemma(fl_keywords.at[z,'keyword'])

    tempfl=tempfl.drop(exclusionlist).reset_index(drop=True)
    fl_keywords=fl_keywords.append(tempfl,ignore_index=True)

#---------------------------------------------------------
# Combine hand labelled data
fl_handlabelled=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])

filelist=[]
for x in os.listdir():
    if "handlabelled_data" in x:
        if x!="handlabelled_data_final.csv":
            filelist.append(x)

for x in filelist:
    tempfl=pandas.read_csv(x)
    #deal with duplicates
    exclusionlist=[]
    for y in range(len(tempfl)):
        for z in range(len(fl_handlabelled)):
            if tempfl.at[y,'jobrequirements']==fl_handlabelled.at[z,'jobrequirements']:
                fl_handlabelled.at[z,'againstgroup']=dec_to_binstr(binstr_to_dec(str(fl_handlabelled.at[z,'againstgroup'])) | binstr_to_dec(str(tempfl.at[y,'againstgroup'])))
                fl_handlabelled.at[z,'bias']=str(max(int(fl_handlabelled.at[z,'bias']), int(tempfl.at[y,'bias'])))
                exclusionlist.append(y)
    
    tempfl=tempfl.drop(exclusionlist).reset_index(drop=True)
    fl_handlabelled=fl_handlabelled.append(tempfl,ignore_index=True)


fl_keywords.to_csv(path_or_buf='keywords_final.csv',index=False)
fl_handlabelled.to_csv(path_or_buf='handlabelled_data_final.csv',index=False)