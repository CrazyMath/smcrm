/* Project specific Javascript goes here. */

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

jQuery(document).ready(function ($) {
    // START DELETE CONFIRMATION
    $(document).on('click', '.delete-confirmation', function (e) {
        e.preventDefault();
        const _this = $(this);
        const deleteUrl = _this.attr('href');
        const message = _this.attr('data-message');
        const deleteConfirmationModal = $('#deleteConfirmation');
        const deleteMessage = _this.attr('data-delete-message');
        const deleteContainer = _this.attr('data-delete-container');

        deleteConfirmationModal.find('.modal-body').text(message);
        deleteConfirmationModal.find('.delete-object').attr('data-delete-url', deleteUrl);
        deleteConfirmationModal.find('.delete-object').attr('data-delete-message', deleteMessage);
        deleteConfirmationModal.find('.delete-object').attr('data-delete-container', deleteContainer);
        deleteConfirmationModal.modal('show');
    });

    $(document).on('click', '.delete-object', function (e) {
        e.preventDefault();
        const _this = $(this);
        const deleteUrl = _this.attr('data-delete-url');
        const deleteMessage = _this.attr('data-delete-message');
        const deleteContainer = _this.attr('data-delete-container');
        const deleteConfirmationModal = $('#deleteConfirmation');


        $.ajax({
            url: deleteUrl,
            method: 'DELETE',
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            success: function (data) {
                console.log(data);
                $(deleteContainer).remove();
                toastr.success(deleteMessage);
                deleteConfirmationModal.modal('hide')
            },
            error: function (data) {
                toastr.success('An error occurred. Try again later.');
            }
        })
    })
    // END DELETE CONFIRMATION
});
