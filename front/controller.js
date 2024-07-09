$(document).ready(function () {
    
    // display speak message

    eel.expose(DisplayMessage)
    function DisplayMessage(message){

        $(".siri-message li:first").text(message);      // fetching the query from take command part
        $('.siri-message').textillate('start');         // restarting the textillate effects
    }

    // display hood again after executing once

    eel.expose(ShowHood)
    function ShowHood(){
        $("#Oval").attr("hidden",false);
        $("#SiriWave").attr("hidden",true);
    }

});