var inputEnabled = true;

/* Helpers */
//add a message to UI, who is 'human' or 'bot'
function messageAdd(who, message){
	var chat = $('#chat-message-wrapper');
	chat.append('<div class="chat-message '+ who +'">'+ message +'</div>');
	chat.scrollTop(chat.prop("scrollHeight"));
}
//submit message in input
function messageSubmit(){
	var message = $('#chat-input').val();
	if(!inputEnabled || message.length == 0) return; //Don't let the user submit a message while a request is in progress
	inputEnabled =- false;
	$('#chat-input').val(''); //Clear the input
	$('#chat-input').focus();
	messageAdd('human', message);
	messageSend(message);
}
//add tile to UI
function tileAdd(tile){
	var tileBody = ['<div class="tile col-sm-12 col-md-12 col-lg-12">',
			'<h4 class="tile-title">', tile.title, '</h4>',
			'<div class="tile-body">', tile.body , '</div></div>'];
	tileBody = tileBody.join('');
	$('#tile-wrapper').append(tileBody);
}
//clear tiles
function tilesRemove(){
	$('.tile').remove();
}

//add buttons to UI
function buttonsAdd(buttons){
	var buttonBodyTemplate = ['<div class="chat-message chat-button">' ,'</div>'];
	var buttonBody = [];
	for(var i = 0; i<buttons.length; i++){
		buttonBody.push(buttonBodyTemplate[0]);
		buttonBody.push(buttons[i]);
		buttonBody.push(buttonBodyTemplate[1]);
	}
	$('#chat-button-wrapper').append(buttonBody.join(''));
	var h = $('#chat-button-wrapper').css('height');
	$('#chat-button-wrapper').css('margin-top', '-'+h)
	var chat = $('#chat-message-wrapper');
	chat.css('padding-bottom', h);
	chat.scrollTop(chat.prop("scrollHeight"));

}
//clear buttons
function buttonsRemove(){
	$('#chat-button-wrapper').css('margin-top', '0px')
	$('#chat-message-wrapper').css('padding-bottom', '0px');
	$('#chat-button-wrapper .chat-button').remove();
}

//click button
function buttonClick(d){
	var val = $(this).text();
	$('#chat-input').val(val);
	buttonsRemove();
	messageSubmit();
}

//update breadcrumb current position
function updateBreadcrumb(curr){
	var breadcrumbs = $('.custom-breadcrumb li');
	for(var i = 1; i <= breadcrumbs.length; i++){
		var crumb = breadcrumbs[i-1];
		$(crumb).removeClass();
		if(i < curr) {
			$(crumb).addClass('done-crumb');
		}else if(i == curr){
			$(crumb).addClass('in-progress-crumb');
		}else if(i%2 == 0){
			$(crumb).addClass('not-started-even-crumb');
		}else{
			$(crumb).addClass('not-started-odd-crumb');
		}
	}
}

/* AJAX queries */
function messageSend(message){
	//Request
	var data = {'message': message};
	var q = $.post(messageSendURL, data);

	//Success
	q.done(function(res){
		var res = JSON.parse(res);
		//add message
		if(Object.keys(res).indexOf('message') > -1){
			$(res['message']).each(function(d, i){messageAdd('bot', i)});
		}
		//enable input
		inputEnabled = true;
		//remove tiles
		tilesRemove();
		//add tiles
		if(Object.keys(res).indexOf('tiles') > -1){
			var tiles = res['tiles'];
			for(var i = 0; i < tiles.length; i++){
				tileAdd(tiles[i]);
			}
		}
		//remove buttons
		buttonsRemove();
		//add buttons
		if(Object.keys(res).indexOf('buttons') > -1){
			buttonsAdd(res['buttons']);
		}
		//change breadcrumb
		if(Object.keys(res).indexOf('breadcrumb_current') > -1){
			var curr = parseInt(res['breadcrumb_current']);
			if(!isNaN(i)) updateBreadcrumb(curr);
		}
	});

	//Failure
	q.fail(function(res){
		inputEnabled = true;
		alert('An error occured while sending your message to the bot: ' + JSON.stringify(res));
	});
}


/* Submit on enter */
$("#chat-input").keydown(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#chat-submit-btn").trigger('click');
    }
});

/* Event listeners */
$('#chat-submit-btn').click(messageSubmit);
$(document).on('click', '.chat-message.chat-button', buttonClick);

