import pandas
import os
import random

DATASIZE_TRAINING=300000
DATASIZE_VALIDATION=5000

fl_data_merged=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])

# Combine data 
filelist=os.listdir()
for x in filelist:
    if "processed_data" in x:
        if x!="processed_data_training.csv" and x!="processed_data_validation.csv":
            fl_temp=pandas.read_csv(x,usecols=['jobrequirements','bias','againstgroup'])
            print(x,'has length:',len(fl_temp))
            fl_data_merged=fl_data_merged.append(fl_temp).reset_index(drop=True)


# select traning data
fl_training=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
locations=random.sample(range(len(fl_data_merged)),k=DATASIZE_TRAINING)
fl_training=fl_training.append(fl_data_merged.iloc[locations],ignore_index=True)
fl_data_merged=fl_data_merged.drop(locations).reset_index(drop=True)
fl_training.to_csv(path_or_buf="processed_data_training.csv",index=False)

# select validation data
fl_validation=pandas.DataFrame(columns=['jobrequirements','bias','againstgroup'])
locations=random.sample(range(len(fl_data_merged)),k=DATASIZE_VALIDATION)
fl_validation=fl_validation.append(fl_data_merged.iloc[locations],ignore_index=True)
fl_data_merged=fl_data_merged.drop(locations).reset_index(drop=True)
fl_validation.to_csv(path_or_buf="processed_data_validation.csv",index=False)
