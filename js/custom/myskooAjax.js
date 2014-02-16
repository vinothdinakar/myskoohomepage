


function loadXMLDoc(reqId, url){
    console.log("loadXMLDoc "+reqId);
    console.log("loadXMLDoc "+url);
    var xmlhttp;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            processResponse(reqId, xmlhttp.responseText);
        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}



function sendToServer(reqId, reqString){
    switch(reqId){
        case 'sendUsMessage':
            var url = '/sendusmessage';
            url += "?"+reqString;
            console.log(url);
            loadXMLDoc(reqId, url);
            break;
        case 'getEmailId':
            var url = '/getemailid';
            url += "?"+reqString;
            console.log(url);
            loadXMLDoc(reqId, url);
            break;
        case 'requestDemo':
            var url = '/requestDemo';
            url += "?"+reqString;
            console.log(url);
            loadXMLDoc(reqId, url);
            break;

        default:

    }
}



function processResponse(reqId, responseText){
    console.log(responseText);
    var responseJson = JSON.parse(responseText);
    switch(reqId){
        case 'sendUsMessage':
            if(responseJson.status === "success"){
                console.log("success");
                updateContactResult();
            }
            break;
        case 'getEmailId':
            if(responseJson.status === "success"){
                console.log("success");
                sendEmailIdResult();
            }
            break;
        case 'requestDemo':
            if(responseJson.status === "success"){
                console.log("success");
                requestDemoResult();
            }
            break;

        default:
    }
}

