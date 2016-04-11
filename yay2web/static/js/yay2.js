var statusUpdateTimer;
var deltaTime = 0;
var statusUpdateCounter = 0;
var lastStatusUpdate = 0;

function statusUpdate() {
    clearTimeout(statusUpdateTimer);

    statusUpdateCounter += 1;
    if(statusUpdateCounter == 50) {
        statusUpdateCounter = 0;
        $.getJSON("/studio/status", function(response) {

            t = parseFloat(response.t) * 1000.0;

            studioTime = new Date(t);
            localTime = new Date();

            deltaTime = studioTime - localTime;
            console.log("deltaTime: "+deltaTime);

            $("#studiotime").html(studioTime.toString());
            $("#localtime").html(localTime.toString());
            $("#lastupdated").html("0");

            lastStatusUpdate = localTime.valueOf();
        }); 
    } else {
            localTime = new Date();
            studioTimeStr = "-";
            last = "-";

            if(lastStatusUpdate!=0) {
                studioTime = new Date(localTime.valueOf() + deltaTime);
                studioTimeStr = studioTime.toString();
                last = localTime.valueOf() - lastStatusUpdate;
            }

            $("#lastupdated").html(last);
            $("#studiotime").html(studioTimeStr);
            $("#localtime").html(localTime.toString());

            
    }

    setTimeout(statusUpdate, 100);
}

$(document).ready(function() {

    statusUpdate();

});
