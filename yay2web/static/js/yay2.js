var statusUpdateTimer;
var deltaTime = 0;
var statusUpdateCounter = 49;
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

            $("#studiotime .time").html(studioTime.toTimeString().substr(0,8));
            $("#studiotime .timezone").html(studioTime.toTimeString().substr(9));
            $("#studiotime .date").html(studioTime.toDateString());

            $("#localtime .time").html(localTime.toTimeString().substr(0,8));
            $("#localtime .timezone").html(localTime.toTimeString().substr(9));
            $("#localtime .date").html(localTime.toDateString());

            $("#lastupdated .value").html("0");

            lastStatusUpdate = localTime.valueOf();
        }); 
    } else {
            localTime = new Date();

            if(lastStatusUpdate!=0) {
                studioTime = new Date(localTime.valueOf() + deltaTime);
                last = localTime.valueOf() - lastStatusUpdate;

                $("#studiotime .time").html(studioTime.toTimeString().substr(0,8));
                $("#studiotime .timezone").html(studioTime.toTimeString().substr(9));
                $("#studiotime .date").html(studioTime.toDateString());

                $("#localtime .time").html(localTime.toTimeString().substr(0,8));
                $("#localtime .timezone").html(localTime.toTimeString().substr(9));
                $("#localtime .date").html(localTime.toDateString());

                $("#lastupdated .value").html(last);
            } else {
                $("#studiotime .time").html("-");
                $("#studiotime .timezone").html("-");
                $("#studiotime .date").html("-");

                $("#localtime .time").html(localTime.toTimeString().substr(0,8));
                $("#localtime .timezone").html(localTime.toTimeString().substr(9));
                $("#localtime .date").html(localTime.toDateString());

                $("#lastupdated .value").html("-");
            }
    }

    setTimeout(statusUpdate, 100);
}

$(document).ready(function() {

    statusUpdate();

});
