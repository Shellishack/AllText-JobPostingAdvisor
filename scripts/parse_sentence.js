function parse_sentence(astr){
    var sentences=[];
    var cursentence="";
    for(var x=0;x<astr.length;++x){
        if(cursentence=="" && (astr[x]==' ' || astr[x]=='\n')){
            continue;
        }
        else if(cursentence!="" && astr[x]=='.'){
            cursentence+=astr[x];
            sentences.push(cursentence);
            cursentence="";
        }
        else if(cursentence!="" &&  (astr[x]=='\n' || astr[x]==';')){
            cursentence+='.';
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