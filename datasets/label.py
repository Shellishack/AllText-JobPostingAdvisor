import pandas


#-------------------------------------------------
#Read file
# fl = pandas.read_csv('data job posts.csv')#can use lambda here
fl=pandas.read_csv('data job posts.csv',usecols=['jobpost','Title','Eligibility','Audience','JobDescription','JobRequirment','RequiredQual'])

#-------------------------------------------------
#Processing data
exclusionlst=[]

for i in range(len(fl)):
    curcell=fl.loc[i].jobpost
    if isinstance(curcell,str):
        if "physical" not in curcell.lower():
            exclusionlst.append(i)
    else:
        exclusionlst.append(i)
    # print(fl.loc[i].Eligibility)
    # print(type(fl.loc[i].Eligibility))

newfl=fl.drop(exclusionlst)

#-------------------------------------------------
#Write a new file

newfl.to_csv(path_or_buf='processed_data_jobposts.csv',columns=['jobpost','Title','Eligibility','Audience','JobDescription','JobRequirment','RequiredQual'],index=False)
