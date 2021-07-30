import * as endpoints from "endpoints_handleserver"
import parse_sentence from "parse_sentence"

    
//process_data(o1.content,o2.content)
function process_data(comname,jobreq){
// 1. read text from both "Company name" and "job requirement"
// Well, we can pass them from html


//2. Parse
//Parse function is already in "parse_sentence.js"
sentencelist=[]
sentencelist = parse_sentence(jobreq);


//3. Call endpoints
//endpoint call functions are in "endpoints_handleserver"

result=[]
for (x=0; x<sentencelist.length; ++x){
    onegroup=getgroup(jobreq);
    onebias=getbias(jobreq);
    result.push([sentencelist[x],onebias,onegroup])
}

//4. Append output to a unique json file ("result_"+comapnyname+".json")

var file = JSON.parse(result);

}