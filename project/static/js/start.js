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
	$('.custom-breadcrumb li').remove();
	var wrapper = $('.custom-breadcrumb');
	for(var i = 1; i <= breadcrumbs.length; i++){
		var crumb = breadcrumbs[i-1];
		var crumbHTML = ['<li class="crumb ', 'done-crumb','"><a>', crumb['name'], '</a></li>'];
		if(i < curr[0]) {
			crumbHTML[1] = 'done-crumb';
			crumbHTML[3] += ' <i class="fa fa-check fa-green"></i>'
		}else if(i == curr[0]){
			crumbHTML[1] = 'in-progress-crumb';
		}else if(i%2 == 0){
			crumbHTML[1] = 'not-started-even-crumb';
		}else{
			crumbHTML[1] = 'not-started-odd-crumb';
		}

		if(i == curr[0]){
			var subBreadcrumbs = crumb['sub'];
			for(var j = 1; j <= subBreadcrumbs.length; j++){
				var subCrumb = subBreadcrumbs[j-1];
				var subCrumbHTML = ['<li class="sub-crumb ', 'sub-done-crumb','"><a>', subCrumb['name'], '</a></li>'];
				if(j < curr[1]) {
					subCrumbHTML[1] = 'sub-done-crumb';
				}else if(j == curr[1]){
					subCrumbHTML[1] = 'sub-in-progress-crumb';
				}else if(j%2 == 0){
					subCrumbHTML[1] = 'sub-not-started-even-crumb';
				}else{
					subCrumbHTML[1] = 'sub-not-started-odd-crumb';
				}
				wrapper.append(subCrumbHTML.join(''));
			}
		}else{
			wrapper.append(crumbHTML.join(''));
		}
	}
}

//Lock and unlock the chat input box
function lockInput(locked){
	var input = $('#chat-input');
	if(locked){
		input.val('');
		$('#chat-input-wrapper').addClass('locked');
		input.prop('disabled', true);
		input.prop('placeholder', 'Please select an option above');
		$('#chat-submit-btn').hide();
	}else{
		$('#chat-input-wrapper').removeClass('locked');
		input.prop('disabled', false);
		input.prop('placeholder', 'Send a message...');
		$('#chat-submit-btn').show();
	}
}

/* AJAX queries */
function getValidationTile(){
	var breadcrumb = $(this).text().trim();
	//Request
	var data = {'breadcrumb': breadcrumb};
	var q = $.post(getValidationTileURL, data);

	//Success
	q.done(function(res){
		tilesRemove();
		tileAdd(JSON.parse(res)['tiles'][0]);
		console.log(res);
	});
	q.fail(function(err){
		alert(err);
		console.log(data);
	});
}
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
		//locked input if locked step
		if(Object.keys(res).indexOf('locked') > -1){
			lockInput(res['locked']);
		}else{
			lockInput(false);
		}
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
			var curr = res['breadcrumb_current'];
			if(curr.length == 2) updateBreadcrumb(curr);
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
$(document).on('click', '.done-crumb', getValidationTile);
