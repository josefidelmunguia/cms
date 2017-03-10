(function ($) {
    'use strict';
    
    $.fn.fileUploader = function (options) {
        
        var settings = $.extend({
            activeColor: 'orangered',
            baseColor: '#ccc',
            overlayColor: 'rgba(255,255,255,0.7)'
        }, options);
        
        var $el = $(this),
          $label, $fileInput, $img, $icon;
        
        setup();
        suscribe();
        
        function setup() {
          $label = $('<label></label>')
            .addClass('uploader')
            .attr('ondragover', 'return false')
            .insertAfter($el);
            
          $fileInput = $el.clone()
            .appendTo($label);
          
          $img = $('<img />')
            .appendTo($label);
            
          $icon = $('<i></i>')
            .addClass('icon icon-upload')
            .appendTo($label);
              
          $el.remove();
              
            _setInactive();
        }
        
        function suscribe() {
            $fileInput.on('change', _handleInputChange);
            $img.on('load', _handleImageLoaded);
            $label.on('dragenter', _handleDragEnter);
            $label.on('dragleave', _handleDragLeave);
            $label.on('drop', _handleDrop);
        }
        
        function _handleDragEnter(e){
            e.preventDefault();
            _setActive();
        }
        
        function _handleDragLeave(e) {
            e.preventDefault();
            _setInactive();
        }
        
        function _handleDrop(e) {
            e.preventDefault();
            _setInactive();
            $fileInput[0].files = e.originalEvent.dataTransfer.files;
            _handleInputChange();
        }
        
        function _handleImageLoaded() {
            if (!$img.hasClass('loaded')) {
                $img.addClass('loaded');
            }
            
            _setInactive();
        }
        
        function _handleInputChange(e) {
            var file = (undefined !== e)
              ? e.target.files[0]
              : $fileInput[0].files[0];

            var pattern = /image-*/;
            var reader = new FileReader();

            if (!file.type.match(pattern)) {
                alert('invalid format');
                return;
            }

            if ($label.hasClass('loaded')) {
                $label.removeClass('loaded');
            }

            reader.onload = _handleReaderLoaded;
            reader.readAsDataURL(file);
        }
        
        function _handleReaderLoaded(e) {
            var reader = e.target;
            $img[0].src = reader.result;
            $label.addClass('loaded');
        }
        
        function _setActive() {
          $label.css('outline-color', settings.activeColor);
          $icon.css('color', settings.activeColor);
        }
        
        function _setInactive() {
          $label.css('outline-color', settings.baseColor);
          $icon.css('color', ($img.hasClass('loaded') ? settings.overlayColor : settings.baseColor));
        }
        
        return this;
    }
    
} (jQuery));