function print_sessionstorage(){
    var len=sessionStorage.getItem("len");
    
    for(var x=0;x<len;++x){
        console.log(sessionStorage.getItem("sentence"+x.toString()+"_sentence"));
        console.log(sessionStorage.getItem("sentence"+x.toString()+"_group"));

    }

}

function shownext(id){
    /* Pass the DOM id to show result in that DOM
       Return a ptr that indicates index of the item
    */
    var ptr=parseInt(sessionStorage.getItem("ptr"))+1;
    var len=sessionStorage.getItem("len");

    if(ptr<len){
        var sentence=sessionStorage.getItem("sentence"+ptr.toString()+"_sentence");
        var group=sessionStorage.getItem("sentence"+ptr.toString()+"_group");
        //padding
        while(group.length!=4){
            group='0'+group;
        }
        // console.log(group);

        // if biased, synthesize output
        var text=sentence+'\n';
        if(group[0]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>intellectual</b> disabilities.';
        }
        if(group[1]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>mental</b> disabilities.';
        }
        if(group[2]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>physical</b> disabilities.';
        }
        if(group[3]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>sensory</b> disabilities.';
        }

        document.getElementById(id).innerHTML=text;
        console.log("ptr is",ptr);
        sessionStorage.setItem("ptr",ptr);
    }
    // otherwise, do nothing.
    else{
        return ptr-1;
    }
    
    return ptr;
}

function showprevious(id){
    /* Pass the DOM id to show result in that DOM
       Return a ptr that indicates index of the item
    */
    var ptr=parseInt(sessionStorage.getItem("ptr"))-1;
    var len=sessionStorage.getItem("len");

    if(ptr>-1){
        var sentence=sessionStorage.getItem("sentence"+ptr.toString()+"_sentence");
        var group=sessionStorage.getItem("sentence"+ptr.toString()+"_group");
        

        // if biased, synthesize output
        var text=sentence+'\n';
        if(group[0]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>intellectual</b> disabilities.';
        }
        if(group[1]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>mental</b> disabilities.';
        }
        if(group[2]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>physical</b> disabilities.';
        }
        if(group[3]=='1'){
            text+='<br><br>This sentence might contain bias against workers with <b>sensory</b> disabilities.';
        }

        document.getElementById(id).innerHTML=text;
        console.log("ptr is",ptr);
        sessionStorage.setItem("ptr",ptr);
    }
    // otherwise, do nothing
    else{
        return ptr+1;
    }
    return ptr;
}

export {print_sessionstorage, shownext, showprevious}