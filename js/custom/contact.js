

function clearField(thisField){
    thisField.placeholder = "";
}



function checkFieldText(thisField){
    if(thisField.id == "contact_name" && thisField.placeholder == ""){
        thisField.placeholder = "Your name...";
    }else if(thisField.id == "contact_phone_number" && thisField.placeholder == ""){
        thisField.placeholder = "Your Phone Number...";
    }else if(thisField.id == "contact_email" && thisField.placeholder == ""){
        thisField.placeholder = "Your Email...";
    }else if(thisField.id == "contact_message" && thisField.placeholder == ""){
        thisField.placeholder = "Your message...";
    }else if(thisField.id == "get_email_id" && thisField.placeholder == ""){
        thisField.placeholder = "Email goes here...";
    }


}



function sendMessage(){
    var contact_name = document.getElementById("contact_name").value;
    var contact_phone_number = document.getElementById("contact_phone_number").value;
    var contact_email = document.getElementById("contact_email").value;
    var contact_message = document.getElementById("contact_message").value;

    var reqString = "contact_name="+contact_name+"&contact_phone_number="+contact_phone_number
            +"&contact_email="+contact_email+"&contact_message="+contact_message;

    sendToServer("sendUsMessage", reqString);
}


function updateContactResult(){
    var resultText = "<div class=\"contact_form_holder\">Thanks for your interest. Our support team will soon contact you.<br>"
    resultText += "Click <a href = '/contact'>here</a> to go back to form</div>"

    document.getElementById('contact_form_holder').innerHTML = resultText;
    //document.getElementById('contact_result').innerHTML = resultText;
}



function sendEmailId(){
    var email_id = document.getElementById("get_email_id").value;
    var reqString = "email_id="+email_id;
    sendToServer("getEmailId", reqString);
}


function sendEmailIdResult(){
    var resultText = "Thanks for your interest. Our support team will soon contact you."
    document.getElementById('sendEmailIdResultDiv').innerHTML = resultText;
}

function requestDemo(){

    var email = document.getElementById("request_demo_email").value;
    var name = document.getElementById("request_demo_name").value;
    var phone = document.getElementById("request_demo_phone").value;

    var requestString = "email="+email+"&name="+name+"&phone="+phone;

    sendToServer("requestDemo", requestString);


}

function requestDemoResult(){

}