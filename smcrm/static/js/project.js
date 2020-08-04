/* Project specific Javascript goes here. */
jQuery(document).ready(function ($) {
    $(document).on('click', '.delete-project', function (e) {
        e.preventDefault()
        let _this = $(this);
        let url = _this.attr('href')
        console.log('Send delete request to ', url)
    })
});
