var timeoutId = {};

function inlineSave () {
    var id = $(this).parent()[0].id;
    $('#status').addClass('label-danger').removeClass('label-success').html('changes pending <i class="fa fa-cog fa-spin"></i>');

    // If a timer was already started, clear it.
    if (timeoutId[id]) clearTimeout(timeoutId[id]);

    // Set timer that will save comment when it fires.
    timeoutId[id] = setTimeout(function () {
        // Make ajax call to save data.
        var data = {'field': id, 'fieldValue': $('td#' + id + ' input').val()};
        var q = $.post(inlineSaveURL, data);
        q.done(function(){
        	$('#status').addClass('label-success').removeClass('label-danger').html('changes saved');
        	console.log(data);
        });
        q.fail(function(err){
        	alert('Something went wrong while saving your data: ' + JSON.stringify(err));
        	$('#status').addClass('label-success').removeClass('label-danger').html('unsaved changes <i class="fa fa-exclamation-triangle"></i>');
        	console.log(data);
        });
        
    }, 1000);
};

$(document).on('input change keypress propertychange', '.editable input', inlineSave);
$(document).on('click', '.editable', function(){ 
	var input = $($(this).children()[0]); 
	var tmp = input.val(); input.focus().val("").blur().focus().val(tmp);
});
