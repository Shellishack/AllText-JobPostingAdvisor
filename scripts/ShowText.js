function showText(id,txt){
    var obj = document.createElement("p");
    var content = document.createTextNode(txt);
    obj.appendChild(content);
    var element=document.getElementById(id);
    element.appendChild(obj);
    return;
}