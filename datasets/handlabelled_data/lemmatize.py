import pandas
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer as wnl
import nltk

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


fl=pandas.read_csv('keywords_final.csv')

for x in range(len(fl)):
    fl.at[x,'keyword']=get_lemma(fl.at[x,'keyword'])

fl.to_csv(path_or_buf='keywords_final.csv',index=False)