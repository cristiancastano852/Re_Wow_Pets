const ticketTable = document.getElementById('ticketTable');
//datatable
$(document).ready(function() {
    $('#ticketTable').DataTable(
        {
            order: [[4, 'desc']],
            dom: 'lftip',
            lengthMenu: [10,20, 50],
        }
    );

    var isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);

    var statusBadges = document.querySelectorAll('.status-badge');
    console.log("asdasdasd",isSafari, navigator.userAgent);
    statusBadges.forEach(function(statusBadge) {
        if (isSafari) {
            statusBadge.style.top = '0.5rem';
            statusBadge.style.left = '1.4rem';
        } else {
            statusBadge.style.top = '-0.5rem';
            statusBadge.style.left = '0.4rem';
        }
    });
} );