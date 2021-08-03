function print_sessionstorage(){
    var len=sessionStorage.getItem("len");
    
    for(var x=0;x<len;++x){
        console.log(sessionStorage.getItem("sentence"+x.toString()+"_sentence"));
        console.log(sessionStorage.getItem("sentence"+x.toString()+"_bias"));
        console.log(sessionStorage.getItem("sentence"+x.toString()+"_group"));

    }

}

function shownext(id){
    /* Pass the DOM id to show result in that DOM
    */
    var ptr=parseInt(sessionStorage.getItem("ptr"))+1;
    var len=sessionStorage.getItem("len");

    if(ptr<len){
        var text=sessionStorage.getItem("sentence"+ptr.toString()+"_sentence")+'\n'+
                 sessionStorage.getItem("sentence"+ptr.toString()+"_bias")+'\n'+
                 sessionStorage.getItem("sentence"+ptr.toString()+"_group");
        document.getElementById(id).innerHTML=text;
        console.log("ptr is",ptr);
        sessionStorage.setItem("ptr",ptr);
    }
    else if(ptr==len){
        document.getElementById(id).innerHTML="You have reached end of file";
        sessionStorage.setItem("ptr",ptr);
    }
    else{
        document.getElementById(id).innerHTML="You have reached end of file";
    }
    return;
}

function showprevious(id){
    var ptr=parseInt(sessionStorage.getItem("ptr"))-1;
    var len=sessionStorage.getItem("len");

    if(ptr>-1){
        var text=sessionStorage.getItem("sentence"+ptr.toString()+"_sentence")+'\n'+
                 sessionStorage.getItem("sentence"+ptr.toString()+"_bias")+'\n'+
                 sessionStorage.getItem("sentence"+ptr.toString()+"_group");
        document.getElementById(id).innerHTML=text;
        console.log("ptr is",ptr);
        sessionStorage.setItem("ptr",ptr);
    }
    else if(ptr==-1){
        document.getElementById(id).innerHTML="You have reached start of file";
        sessionStorage.setItem("ptr",ptr);
    }
    else{
        document.getElementById(id).innerHTML="You have reached start of file";
    }
    return;
}

export {print_sessionstorage, shownext, showprevious}