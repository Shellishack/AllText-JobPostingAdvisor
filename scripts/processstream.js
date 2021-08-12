import { getbias, getgroup } from './endpointsAPI.js';
import {parse_sentence} from './parse_sentence.js'



async function process_stream(jobreq){
    //1. Parse
    //Parse function is already in "parse_sentence.js"
    var sentencelist=[];
    sentencelist = parse_sentence(jobreq);
    // console.log(sentencelist[0]);

    //2. Call endpoints
    //endpoint call functions are in "endpoints_handleserver"

    var output={
        "data":[
        ]
    };

    for (var x=0; x<sentencelist.length; ++x){
        var temp={'sentence':sentencelist[x]};

        let response_group=await getgroup(sentencelist[x]);
        let group=await response_group.json();
        group=JSON.parse(group)['result'];

        let response_bias=await getbias(sentencelist[x]);
        let bias=await response_bias.json();
        bias=JSON.parse(bias)['result'];
        temp['bias']=bias;
        temp['group']=group;
        output.data.push(temp);
    }
    
    // 3. Put sentences labelled biased into storage along with its group
    sessionStorage.setItem("ptr",-1);
    
    sessionStorage.setItem("fulltext",jobreq);
    var nbiased=0;
    for(var x=0;x<output.data.length;++x){
        // console.log(typeof(output.data[x].bias[0]));
        // console.log(output.data[x].bias[0]);
        if(output.data[x].bias=='2'){
            console.log(x,"biased");
            // Treat storage as a dictionary
            sessionStorage.setItem("sentence"+nbiased.toString()+"_sentence",output.data[x].sentence);
            sessionStorage.setItem("sentence"+nbiased.toString()+"_group",output.data[x].group);
            nbiased+=1;
            // console.log("sentence"+x.toString()+"_sentence");
            // console.log(output.data[x].sentence);
            // console.log(output.data[x].bias);
            // console.log(output.data[x].group);
        }
    }
    sessionStorage.setItem("len",nbiased);
    console.log(output);
    return output;
    
    
}


export {process_stream};