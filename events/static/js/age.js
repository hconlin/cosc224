function ageReq() {
    $(document).ready(function () {
        $('#id_age').remove();
        $('.age-requirement').change(function () {
            if ($(this).val() != 'None') {
                if($('#id_age').length == 0) {
                    $('.append-age').append('<input type="number" min="1" name="age" id="id_age" style="width:50px; height: 30px; margin-left: 10px; margin-right: 10px; padding-left: 5px;"><span>years old</span>');
                }
            } else {
                $('#id_age').remove();
                $('span').remove();
            }
        })
    });
}