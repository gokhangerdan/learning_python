$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];
    var numbers_received2 = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log(msg)
        console.log("Received number" + msg.number1);
        console.log("Received number2" + msg.number2);
        //maintain a list of ten numbers
        if (numbers_received.length >= 1){
            numbers_received.shift()
        }
        if (numbers_received2.length >= 1){
            numbers_received2.shift()
        }
        numbers_received.push(msg.number1);
        numbers_received2.push(msg.number2);
        numbers_string = '';
        numbers_string2 = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        }
        for (var i = 0; i < numbers_received2.length; i++){
            numbers_string2 = numbers_string2 + '<p>' + numbers_received2[i].toString() + '</p>';
        }
        $('#log').html(numbers_string);
        $('#log2').html(numbers_string2);
    });

});