from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self,keytoken,entrysize_max,entrysize_min):
        self.p=False
        self.ul=False
        self.li=False
        self.flag_found=False

        self.abort=False
        self.cur_section_result=[]

        self.keytoken=keytoken
        self.filtered_result=[]
        self.entrysize_max=entrysize_max
        self.entrysize_min=entrysize_min
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag=='p':
            if self.p or self.li:
                self.abort=True
            else:
                self.p=True
        elif tag=='ul':
            if self.ul or self.li:
                self.abort=True
            else:
                self.ul=True
        elif tag=='li':
            self.li=True

        elif tag!='b':
            self.abort=True
        
        return super().handle_starttag(tag, attrs)
    
    def handle_data(self, data):

        if self.p:
            self.flag_found=False
            if len(data)<50:
                i=0
                while not self.flag_found and i<len(self.keytoken):
                    if self.keytoken[i] in data.lower():
                        self.flag_found=True
                    else:
                        i+=1
                
                # if self.flag_found:
                #     print(data)

        elif self.ul and self.li:
            newsentence=data.strip().strip('\n').strip('\r')
            length=len(newsentence)
            if length!=0:
                
                #about if unicode>256
                for x in newsentence:
                    if ord(x)>256 or ord(x)==233:
                        # newsentence=newsentence[0:x]+newsentence[x+1:length]
                        # length-=1
                        newsentence=""
                        break


                if newsentence!="" and self.entrysize_max>=len(newsentence) and self.entrysize_min<=len(newsentence):
                    self.cur_section_result.append(newsentence.strip())
                
        

        
        return super().handle_data(data)

    def handle_endtag(self, tag):
        if self.abort:
            self.cur_section_result=[]
            self.abort=False
            self.p=False
            self.ul=False
            self.li=False
            self.flag_found=False
        else:
            if tag=='p':
                self.p=False
            elif tag=='ul':
                self.ul=False
                self.flag_found=False
                # if len(self.cur_section_result)!=0:
                self.filtered_result.extend(self.cur_section_result)
                # print(self.cur_section_result)
                self.cur_section_result=[]
                
            elif tag=='li':
                self.li=False
            
        
        # print(tag,self.filtered_result)
        return super().handle_endtag(tag)


# parser=MyHTMLParser(['skill','demand','qualification','requirement','experience','abilit','criteria','responsibilit'])

# fl=open('view_jobpost.html','r')
# astr=fl.read()
# # print(astr)
# parser.feed(astr)
# print(parser.filtered_result)