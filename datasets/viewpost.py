import pandas

fl=pandas.read_csv('data_jobpost2.csv',usecols=['Job Description'])

for x in range(len(fl)):
    page=open("view_jobpost.html",'w')

    page.write("<body>")
    page.write(fl.loc[x][0])
    page.write("</body>")
    page.close()
    
    print("Write page",x)
    input()