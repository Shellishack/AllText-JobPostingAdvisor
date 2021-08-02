function parse_sentence(astr){
    var sentences=[];
    var cursentence="";
    for(var x=0;x<astr.length;++x){
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
    if(cursentence.length!=0){
        sentences.push(cursentence);
    }
    // console.log(sentences);
    return sentences;
}

export {parse_sentence};