document.addEventListener('DOMContentLoaded', function() { 
    var selectElements = document.querySelectorAll('.select-choices');
    selectElements.forEach(function(select) {
        new Choices(select, {
            placeholder: 'Select an option',
            itemSelectText: 'Press to select',
            position: 'bottom',
        });
   
    });

    const fileInput = document.getElementById('file');
    const fileError = document.getElementById('file-error');

    fileInput.addEventListener('change', (event) => {
    const files = event.target.files;
    if (files.length > 10) {
        fileError.textContent = 'Please select a maximum of 10 images.';
        event.preventDefault(); 
    } else {
        fileError.textContent = '';
    }
    });
});

