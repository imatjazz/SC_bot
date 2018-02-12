// Layout.js 
// Note: applied to all pages that extend layout.html

//Search redirect
function doSearch() {
    var search_data = document.getElementById("nav-box").value;
    window.location = results_path+search_data
}

/************************** Event listeners *************************/
$("#nav-button").on({click: function(){doSearch()}});

$("#nav-box").keydown(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#nav-button").trigger('click');
    }
});

/***************** DropZone Widget Behaviour for file upload ********/      
+ function($) {
    'use strict';

    // UPLOAD CLASS DEFINITION
    // ======================

    var dropZone = document.getElementById('drop-zone');

    if(dropZone != null){
        window.startUpload = function(files) {
            window.file = files[0];
            var filename = files[0].name;
            $('.upload-drop-zone').addClass('dropped');
            $('.upload-drop-zone').html(filename + ' <i class="glyphicon glyphicon-ok" style="color: green"></i>');
        }

        dropZone.ondrop = function(e) {
            e.preventDefault();
            this.className = 'upload-drop-zone';

            window.startUpload(e.dataTransfer.files)
        }

        dropZone.ondragover = function() {
            this.className = 'upload-drop-zone drop';
            return false;
        }

        dropZone.ondragleave = function() {
            this.className = 'upload-drop-zone';
            return false;
        }   
    }

}(jQuery);