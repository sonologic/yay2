
// status update related

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

    statusUpdateTimer = setTimeout(statusUpdate, 100);
}

// logfile related

var logfile_id;
var logfile_interval = 3000;
var logfile_timer;
var logfile_lastseen=-2;
var logfile_maxentries=120;

function updateLog() {
    clearTimeout(logfile_timer);

    $.getJSON('/studio/logentries/'+logfile_id+'/'+(logfile_lastseen+1), function(response) {
        for(var idx in response) {
            entry = response[idx];

            $("#logfileentries").append('<div class="logentry">' +
                                        '<span class="id">' + entry.id + '</span> ' +
                                        '<span class="datetime">' + entry.datetime + '</span> ' +
                                        '<span class="message">' + entry.message + '</span></div>');

            if(entry.id>logfile_lastseen)
                logfile_lastseen = entry.id;
        }

        entries = $("#logfileentries div");
        n_entries = entries.length;

        if(n_entries>logfile_maxentries) {
            entries.slice(0, n_entries-logfile_maxentries).remove();
        }

        $("#logfileentries").animate({ scrollTop: $('#logfileentries').prop("scrollHeight")}, 1000);
    });

    logfile_timer = setTimeout(updateLog, logfile_interval);
}

$(document).ready(function() {
    if($("#globalstatus").length == 1) {
        statusUpdate();
    }

    // activate logentry fetcher if logfileentries node is present
    if($("#logfileentries").length == 1) {
        logfile_id = $("#logfileentries").attr("data-logfile");
        console.log("logfile: "+logfile_id);
        updateLog();
    }
});
