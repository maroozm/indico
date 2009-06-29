{ 
    checkParams : function () {
        return {
            "permission": ["radio", false, function(option, values){
                var errors = [];
                if (!exists(values["permission"])) {
                    errors.push("Please answer if all the speakers given permission to have their talks recorded.");
                }
                return errors;
            }],
            "lectureOptions": ["text", true, function(option, values){
                var errors = [];
                if (option == 'chooseOne') {
                    errors.push("Please choose if slides and/or chalkboards will be used.");
                }
                return errors;
            }],
            "lectureStyle": ["text", true, function(option, values){
                var errors = [];
                if (option == 'chooseOne') {
                    errors.push("Please choose a type of event.");
                }
                return errors;
            }]
        }
    },
    
    errorHandler: function(event, error) {
        if (error.operation == "create") {
            CSErrorPopup("Could not send email to responsible",
                         [Html.span("", "There was a problem when sending the notification email to the Recording responsible:", Html.br(), error.inner)])
        }
        if (error.operation == "edit") {
            CSErrorPopup("Could not send email to responsible",
                         [Html.span("", "There was a problem when sending the notification email to the Recording responsible:", Html.br(), error.inner)])
        }
        if (error.operation == "remove") {
            CSErrorPopup("Could not send email to responsible",
                        [Html.span("", "There was a problem when sending the notification email to the Recording responsible:", Html.br(), error.inner)])
        }
    },
    
    customText : function(booking) {
        if (booking.statusMessage == "Request rejected by responsible" && trim(booking.rejectionReason)) {
            return "Rejection reason: " + trim(booking.rejectionReason);
        }
    },
    
    clearForm : function () {
        var formNodes = IndicoUtil.findFormFields($E('RecordingRequestForm'));
        IndicoUtil.setFormValues(formNodes, {'talkSelectionComments':'', 'numRemoteViewers':'', 'numAttendees':'', 'otherComments':''})
        $E('allTalksRB').dom.checked = true;
        IndicoUI.Effect.disappear($E('contributionsDiv'));
        $E('permissionYesRB').dom.checked = false;
        $E('permissionNoRB').dom.checked = false;
        $E('lectureOptions').dom.value = "chooseOne";
        $E('lectureStyle').dom.value = "chooseOne";
        $E('postingUrgency').dom.value = "withinWeek";
    },
    
    onLoad : function() {
        if (singleBookings['RecordingRequest'] && singleBookings['RecordingRequest'].bookingParams.talks == 'choose') {
            IndicoUI.Effect.appear($E('contributionsDiv'));
            window.contributionsLoaded = true;
        } else {
            $E('contributionsRow').append(Html.td("RRContributionsColumn",Html.ul({id:'contributionList1', className:'RROptionList'})));
            $E('contributionsRow').append(Html.td("RRContributionsColumn",Html.ul({id:'contributionList2', className:'RROptionList'})));
        }
        
        if(!singleBookings['RecordingRequest']) {
            callFunction('RecordingRequest','clearForm');
        }
    }
}