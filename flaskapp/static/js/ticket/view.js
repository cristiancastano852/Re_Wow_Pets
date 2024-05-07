    // Get references to the tabs and card bodies
    const imagesTab = document.getElementById('imagesTab');
    const commentsTab = document.getElementById('commentsTab');
    const imagesCard = document.getElementById('imagesCard');
    const commentsCard = document.getElementById('commentsCard');

    imagesTab.addEventListener('click', function (event) {
        event.preventDefault(); 
        imagesTab.classList.add('active');
        commentsTab.classList.remove('active');
        imagesCard.style.display = 'block';
        commentsCard.style.display = 'none';
    });
    commentsTab.addEventListener('click', function (event) {
        event.preventDefault(); 
        imagesTab.classList.remove('active');
        commentsTab.classList.add('active');
        imagesCard.style.display = 'none';
        commentsCard.style.display = 'block';
    });

    $('#editTicketBtn').click(function() {
        $('#editTicketModal').modal('show');
    });

    $('#saveChangesBtn').click(function() {
        $('#editTicketModal').modal('hide');
    });



