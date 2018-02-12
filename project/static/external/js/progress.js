/* Style information for progress buttons, for use in results page */

$(document).ready(function(){

    // Convert all the links with the progress-button class to
    // actual buttons with progress meters.
    // You need to call this function once the page is loaded.
    // If you add buttons later, you will need to call the function only for them.

    $('.progress-button').progressInitialize();

});

// The progress meter functionality is available as a series of plugins.
// You can put this code in a separate file if you wish to keep things tidy.

(function($){

    // Creating a number of jQuery plugins that you can use to
    // initialize and control the progress meters.

    $.fn.progressInitialize = function(val_in=10){

        // This function creates the necessary markup for the progress meter
        // and sets up a few event listeners.

        // Loop through all the buttons:

        return this.each(function(){

            var button = $(this),
                progress = val_in*100,
                skill = button.attr('skill');

            // Extract the data attributes into the options object.
            // If they are missing, they will receive default values.

            var options = $.extend({
                type:'background-horizontal',
            }, button.data());

            //Add bar text
            button.attr({'data-loading': skill});

            // Add the needed markup for the progress bar to the button
            var bar = $('<span class="tz-bar ' + options.type + '">').appendTo(button);

            button.removeClass('finished').addClass('in-progress')
            setProgress(progress);


            function setProgress(percentage){
                bar.filter('.background-horizontal,.background-bar').width(percentage+'%');
                bar.filter('.background-vertical').height(percentage+'%');
            }

        });

    };

    $.fn.progressSet = function(val){
        val = val || 10;

        var finish = false;
        if(val >= 100){
            finish = true;
        }

        return this.first().trigger('progress',[val, true, finish]);
    };

})(jQuery);