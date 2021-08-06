import pandas
import os
import random

DATASIZE_TRAINING=0.75
DATASIZE_VALIDATION=0.25

fl_data_merged=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])

# Combine data 
filelist=os.listdir()
for x in filelist:
    if "processed_data" in x:
        if x!="processed_data_training.csv" and x!="processed_data_validation.csv":
            fl_temp=pandas.read_csv(x,usecols=['jobrequirements','bias','againstgroup'])
            print(x,'has length:',len(fl_temp))
            fl_data_merged=fl_data_merged.append(fl_temp).reset_index(drop=True)

dplst=fl_data_merged.duplicated()
exclusionlst=[]
for x in range(len(dplst)):
    if dplst[x]==True:
        exclusionlst.append(x)

fl_data_merged=fl_data_merged.drop(exclusionlst).reset_index(drop=True)
print("Total number of entries",len(fl_data_merged))

# count biasd and unbiased entries
lst_biased=[]
lst_unbiased=[]
for x in range(len(fl_data_merged)):
    if int(fl_data_merged.at[x,'bias'])==0:
        lst_unbiased.append(x)
    else:
        lst_biased.append(x)

print("Before balancing, biased-unbiased: "+str(len(lst_biased))+'-'+str(len(lst_unbiased)))

# balance data
target_n_unbiased=round(len(lst_biased)/7)
exclude_n_unbiased=len(lst_unbiased)-target_n_unbiased
exclude_loc_unbiased=random.sample(range(len(lst_unbiased)),k=exclude_n_unbiased)
exclusionlst=[]
isbiased=False
for x in exclude_loc_unbiased:
    exclusionlst.append(lst_unbiased[x])
fl_data_merged=fl_data_merged.drop(exclusionlst).reset_index(drop=True)

lst_biased=[]
lst_unbiased=[]
for x in range(len(fl_data_merged)):
    if int(fl_data_merged.at[x,'bias'])==0:
        lst_unbiased.append(x)
    else:
        lst_biased.append(x)
print("After balancing, biased-unbiased: "+str(len(lst_biased))+'-'+str(len(lst_unbiased)))
print("After balancing, total number of entries:",len(fl_data_merged))


# select traning data
target_validation_size=round(DATASIZE_VALIDATION*len(fl_data_merged))-1
target_training_size=round(DATASIZE_TRAINING*len(fl_data_merged))

fl_training=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
locations=random.sample(range(len(fl_data_merged)),k=target_training_size)
fl_training=fl_training.append(fl_data_merged.iloc[locations],ignore_index=True)
fl_data_merged=fl_data_merged.drop(locations).reset_index(drop=True)
fl_training.to_csv(path_or_buf="processed_data_training.csv",index=False)
# select testing data
fl_validation=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
# locations=random.sample(range(len(fl_data_merged)),k=target_validation_size)
fl_validation=fl_validation.append(fl_data_merged,ignore_index=True)
# fl_data_merged=fl_data_merged.drop(locations).reset_index(drop=True)
fl_validation.to_csv(path_or_buf="processed_data_validation.csv",index=False)

print("Target training data size:",target_training_size)
print("Target testing data size:",target_validation_size)

print("Real training data size:",len(fl_training))
print("Real testing data size:",len(fl_validation))
