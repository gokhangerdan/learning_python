$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();
        console.log(message);
        $.ajax({
            url: "http://localhost:5000/api/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"message": message}),
            dataType: "json"
        }).done(function(data) {
            console.log(data);
        });
    });
});
