function sendMessage() {
    console.log("Sending message");
    console.log("Message: "+$("#chat_text").val());
    $.ajax({
        type: 'POST',
        url: '/sendMessage',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify({"message":$("#chat_text").val()}),
        dataType: 'json',
        success: function(response) {
            console.log("Sent data");
            console.log(response);
            $("#chathistory").append("<div>"+JSON.stringify(response.result)+"</div>");
        }
    });
}