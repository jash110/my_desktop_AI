$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 700,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.25",
        autostart: true
      });

    // Siri Message animation
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // Mic Button click event

    $("#MicBtn").click(function () { 
        eel.playIntro();
        $("#Oval").attr("hidden",true);
        $("#SiriWave").attr("hidden",false);
        eel.allCommands()()

    });

});