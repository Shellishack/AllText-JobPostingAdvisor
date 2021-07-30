function parse_sentence(astr){
    sentences=[];
    cursentence="";
    for(x=0;x<astr.length;++x){
        if(astr[x]==' ' && cursentence==""){
            continue;
        }
        else if(astr[x]=='.' || astr[x]==';'){
            cursentence+=astr[x];
            sentences.push(cursentence);
            cursentence="";
        }
        else{
            cursentence+=astr[x];
        }
    }
    console.log(sentences);
    return sentences;
}