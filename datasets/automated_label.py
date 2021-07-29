# Things that need attention
# Upper/lower case


import pandas
import nltk
import time
import multiprocessing
from nltk.corpus import wordnet
from nltk import WordNetLemmatizer as wnl

disabilitytypes=['intellectual','mental','physical','sensory']

fl_keyword=pandas.read_csv('./handlabelled_data/keywords_final.csv')
fl_data1=pandas.read_csv('filtered_data_1.csv')
fl_data2=pandas.read_csv('filtered_data_2.csv')
fl_data_merged=fl_data1.append(fl_data2).reset_index(drop=True)

def get_nulldisabilitytypes_bitmap():
    type_bitmap_str=""
    for y in range(len(disabilitytypes)):
        type_bitmap_str+='0'
    return type_bitmap_str


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



def dec_to_binstr(n):
    result=""
    length=len(get_nulldisabilitytypes_bitmap())
    while len(result)!=length:
        result=str(n%2)+result
        n=n//2
    
    return result

def binstr_to_dec(astr):
    result=0
    for x in astr:
        result=result*2+int(x)
    return result

def tokenize(astr):
    # This time we only want lowercase
    lst=[]
    aword=""
    for x in astr:
        if ('a'<=x and x<='z') or ('A'<=x and x<='Z') or x=="'" or x=='-':
            if x=='-' and aword=="":
                continue
            aword+=x
        else:
            if aword=="":
                continue
            else:
                lst.append(aword.lower())
                aword=""
    if aword!="":
        lst.append(aword.lower())
    return lst

def label(location,patchsize,coreid):
    keywordlist=list(fl_keyword['keyword'])

    outputfile="processed_data_core"+coreid+".csv"

    # fl_data_merged.insert(loc=len(list(fl_data_merged)),column='bias',value=None)
    # fl_data_merged.insert(loc=len(list(fl_data_merged)),column='againstgroup',value=None)
    fl_result=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
    timestamp=time.time()
    for x in range(location,location+patchsize):
        if (x-location)%(patchsize//100*5)==0:
            newtime=time.time()
            print("Process "+str(coreid)+": "+str((x-location)//(patchsize//100))+"% done \t","Time elapsed:"+str(round(newtime-timestamp,2))+"s\ton entry:",x)
            fl_result.to_csv(path_or_buf=outputfile,index=False)
            timestamp=newtime
        onesentence=tokenize(fl_data_merged.at[x,'jobrequirements'])
        result_againstgroup=0
        result_bias=0
        for y in onesentence:
            for z in range(len(keywordlist)):
                if get_lemma(y)==keywordlist[z]:
                    # biased
                    result_againstgroup=result_againstgroup | binstr_to_dec(str(fl_keyword.at[z,'againstgroup']))

        if result_againstgroup!=0:
            result_bias=2
        
        result_againstgroup=dec_to_binstr(result_againstgroup)
        newrow=[{'jobrequirements':fl_data_merged.at[x,'jobrequirements'],'bias':result_bias,'againstgroup':result_againstgroup}]
        fl_result=fl_result.append(newrow,ignore_index=True)

    newtime=time.time()
    print("Process "+str(coreid)+": "+"100% done \t","Time elapsed:"+str(round(newtime-timestamp,2))+"s\ton entry:",location+patchsize)
    fl_result.to_csv(path_or_buf=outputfile,index=False)

if __name__=='__main__':
    nprocess=16
    numperprocess=len(fl_data_merged)//nprocess
    # numperprocess=100
    para=[]
    for x in range(nprocess):
        para.append((x*numperprocess,numperprocess,str(x)))
    with multiprocessing.Pool(nprocess) as p:
        p.starmap(label,para)

# label(0,100,"1")
# label(200,100,"2")