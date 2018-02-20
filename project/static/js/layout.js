// Layout.js 
// Note: applied to all pages that extend layout.html

/***************** DropZone Widget Behaviour for file upload ********/      
/*+ function($) {
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

}(jQuery);*/