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
        // getgroup(sentencelist[x])
        //     .then(response=>response.json())
        //     .then(result=>{
        //         temp['group']=JSON.parse(result)["result"];
        //         // console.log(result)
        //         // console.log(JSON.parse(result).result);
        //     });
        // getbias(sentencelist[x])
        //     .then(response=>response.json())
        //     .then(result=>{
        //         temp['bias']=JSON.parse(result)["result"];
        //         // console.log(result)
        //         // console.log(JSON.parse(result).result);
        //     });
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
    
    // 3. Put result into storage
    sessionStorage.setItem("ptr",-1);
    sessionStorage.setItem("len",output.data.length);
    for(var x=0;x<output.data.length;++x){
        // Treat storage as a queue
        sessionStorage.setItem("sentence"+x.toString()+"_sentence",output.data[x].sentence);
        sessionStorage.setItem("sentence"+x.toString()+"_bias",output.data[x].bias);
        sessionStorage.setItem("sentence"+x.toString()+"_group",output.data[x].group);
        // console.log("sentence"+x.toString()+"_sentence");
        // console.log(output.data[x].sentence);
        // console.log(output.data[x].bias);
        // console.log(output.data[x].group);
    }
    console.log(output);
    return output;
    
    
}


export {process_stream};