import pandas
from htmlparse import MyHTMLParser


def parse_fl1(astr):
    flag1=False # whether to start parse
    result=[]

    oneentry=""
    for x in astr:
        if flag1:
            if x==';' or x=='.':
                flag1=False
                result.append(oneentry.strip())
                oneentry=""

            elif x=='\n':
                oneentry=oneentry+' '

            elif x!='\r':
                oneentry=oneentry+x
            
        else:
            if x=='-':
                flag1=True
    return result



#fl2 contains xml file.
keytoken=['skill','demand','qualification','requirement','experience','abilit','criteria','responsibilit']
def parse_fl2(astr):
    parse=MyHTMLParser(keytoken)
    parse.feed(astr)
    return parse.filtered_result

def main():
    filtered_data_1=[]
    filtered_data_2=[]


    # #filter dataset 1
    fl1=pandas.read_csv('data_jobposts_1.csv',skiprows=range(1,13000),usecols=['JobRequirment','RequiredQual'])

    for x in range(len(fl1)):
        if isinstance(fl1.loc[x][0],str):
            filtered_data_1.extend(parse_fl1(fl1.loc[x][0]))

        if isinstance(fl1.loc[x][1],str):
            filtered_data_1.extend(parse_fl1(fl1.loc[x][1]))

    filtered_fl_1=pandas.DataFrame(filtered_data_1,columns=['jobrequirements'])
    filtered_fl_1.to_csv(path_or_buf='filtered_data_1.csv',index=False)

    # print(filtered_fl_1.loc[1][0])

    #filter dataset 2
    fl2=pandas.read_csv('data_jobposts_2.csv',usecols=['Job Description'])
    # fl2=pandas.read_csv('data_jobpost2.csv',skiprows=range(1,22),nrows=2,usecols=['Job Description'])
    
    for x in range(len(fl2)):
        if isinstance(fl2.loc[x][0],str):
            filtered_data_2.extend(parse_fl2(fl2.loc[x][0]))
    filtered_fl_2=pandas.DataFrame(filtered_data_2,columns=['jobrequirements'])
    filtered_fl_2.to_csv(path_or_buf='filtered_data_2.csv',index=False)

main()