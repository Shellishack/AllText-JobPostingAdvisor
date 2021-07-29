import pandas
import random

targetnum=200
disabilitytypes=['developmental','intellectual','mental','physical','sensory']

def get_nulldisabilitytypes_bitmap():
    type_bitmap_str=""
    for y in range(len(disabilitytypes)):
        type_bitmap_str+='0'
    return type_bitmap_str

def tokenize(astr):
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
                lst.append(aword)
                aword=""
    if aword!="":
        lst.append(aword)
    return lst
    
#-------------------------------------------------
#Read files

fl1=pandas.read_csv('filtered_data_1.csv',usecols=['jobrequirements'])
fl2=pandas.read_csv('filtered_data_2.csv',usecols=['jobrequirements'])

fl=fl1.append(fl2,ignore_index=True)

#-------------------------------------------------
#Processing data
# length_fl1=len(fl1)
# length_fl2=len(fl2)
length_fl=len(fl)
keywords=[]
handlablledfl=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
keywordfl=pandas.DataFrame(columns=['bias','keyword','againstgroup'])

x=0
i=random.randrange(length_fl)

newrows_handlabelled=pandas.DataFrame()
while x <targetnum:
    exclusionlist=[]
    newrows_keywords=[]
    print("---------------------------------------------------------------")
    print(str(x)+" entries labelled ("+str(x)+"/"+str(targetnum)+")")
    print("Dataset size:",length_fl)

    
    cursentence=fl.iloc[i][0]
    print('\n***'+cursentence+'***\n')
    print("Is this requirement biased?")
    print("Rate from 0-2 (0 if neutral; 1 if non-neutral but more context is needed; 2 if biased).")
    print("Enter x to skip this sentence.")
    answer_bias=input()

    if answer_bias=='x':
        i=random.randrange(length_fl)
        continue


    try:
        answer_bias=int(answer_bias)
    except ValueError:
        print("Please enter a valid value.\n")
        continue

    if answer_bias==0:
        
        #add this entry to new file
        type_bitmap_str=get_nulldisabilitytypes_bitmap()
        exclusionlist.append(i)
        newrows_handlabelled=pandas.DataFrame([[cursentence,0,type_bitmap_str]],columns=['jobrequiements','bias','againstgroup'])
        

    elif answer_bias==1:

        print("Which disability type is this sentence against?")
        for y in range(len(disabilitytypes)):
            print(y+1,'\t',disabilitytypes[y])
        
        while True:
            try:
                answer_type=input().split()
                type_bitmap_arr=[]
                for y in range(len(disabilitytypes)):
                    type_bitmap_arr.append(0)
                if len(answer_type)!=0:
                    flag_reinput=False
                    for y in answer_type:
                        if int(y)-1>=len(disabilitytypes):
                            print("Please enter a valid value.")
                            flag_reinput=True
                            break
                        type_bitmap_arr[int(y)-1]=1
                    if flag_reinput==True:
                        continue
                #to string
                type_bitmap_str=""
                for y in type_bitmap_arr:
                    type_bitmap_str+=str(y)
                
                break
            except ValueError:
                print("Please enter a valid value.")
        exclusionlist.append(i)
        newrows_handlabelled=pandas.DataFrame([[cursentence,1,type_bitmap_str]],columns=['jobrequiements','bias','againstgroup'])
        

    elif answer_bias==2:
        print("Which word(s) make you believe that this sentence is biased?")
        print("Enter the corresponding index number(s) of these word(s), separated by a single space.")
        print("For example, '1 2 3' to select all words in 'I love coding'.")
        parsed_cursentence=tokenize(cursentence)
        for y in range(len(parsed_cursentence)):
            print(y+1,"\t",parsed_cursentence[y])

        #get the list of keywords
        while True:
            try:
                answer_keyword=input().split()
                keywords=[]
                if len(answer_keyword)!=0:
                    flag_reinput=False
                    for y in answer_keyword:
                        if int(y)-1>=len(parsed_cursentence):
                            print("Please enter a valid value.")
                            flag_reinput=True
                            break
                        keywords.append(parsed_cursentence[int(y)-1].lower())
                    if flag_reinput:
                        continue
                else:
                    print("You must enter at least one keyword if you think this sentence is biased.")
                    print("If you aren't confident of your decision, please enter a random answer and restart.")
                    print("Please enter 1 for 'non-neutral but more context is needed' when you are asked to label this sentence.")
                    continue
                break
            except ValueError:
                print("Please enter a valid value.")
            
        #ask for bias type for the whole sentence
        print("Which disability type is this sentence against?")
        for y in range(len(disabilitytypes)):
            print(y+1,'\t',disabilitytypes[y])
        
        while True:
            try:
                answer_type=input().split()
                type_bitmap_arr=[]
                for y in range(len(disabilitytypes)):
                    type_bitmap_arr.append(0)
                if len(answer_type)!=0:
                    flag_reinput=False
                    for y in answer_type:
                        if int(y)-1>=len(disabilitytypes):
                            print("Please enter a valid value.")
                            flag_reinput=True
                            break
                        type_bitmap_arr[int(y)-1]=1
                    if flag_reinput==True:
                        continue
                else:
                    print("You must enter at least one type if you think this sentence is biased.")
                    print("If you aren't confident of your decision, please enter a random answer and restart.")
                    print("Please enter 1 for 'non-neutral but more context is needed' when you are asked to label this sentence.")
                    continue
                
                #to string
                type_bitmap_str=""
                for y in type_bitmap_arr:
                    type_bitmap_str+=str(y)
                
                break
            except ValueError:
                print("Please enter a valid value.")
                
        for y in keywords:
            newrows_keywords.append([2,y,type_bitmap_str])
        

        newrows_handlabelled=pandas.DataFrame([[cursentence,2,type_bitmap_str]],columns=['jobrequiements','bias','againstgroup'])
        
        
    else:
        print("Please enter a valid value.")
        continue
    
    print("Please confirm your answer.")
    print("Enter r to restart labelling this sentence; enter any other key to continue.")
    answer_check=input()
    if answer_check=='r':
        keywords=[]
        continue
    

    # write labelled data to new file


    # drop entries that contain labelled keywords
    print("keywords:",keywords)
    
    for i in keywords:
        for y in range(length_fl):
            onesentence=fl.iloc[y][0]
            if i in onesentence.lower():
                exclusionlist.append(y)
                
    # print(exclusionlist)
    fl=fl.drop(exclusionlist).reset_index(drop=True)
    length_fl=len(fl)
    i=random.randrange(length_fl)
    x+=1
    keywords=[]
    #-------------------------------------------------
    #Write a new file

    # print(handlablledfl)
    handlablledfl=handlablledfl.append(newrows_handlabelled,ignore_index=True)
    keywordfl=keywordfl.append(pandas.DataFrame(newrows_keywords,columns=['bias','keyword','againstgroup']),ignore_index=True)
    handlablledfl.to_csv(path_or_buf='handlabelled_data_jobposts.csv',index=False)
    keywordfl.to_csv(path_or_buf='keywords.csv',index=False)

    