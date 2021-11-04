let countrySelected = $('#id_def_country').val();

if (!countrySelected) {
    $('#id_def_country').css('color', '#AAB7C4' );
};

$('#id_def_country').change(function() {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#AAB7C4' );
    } else {
        $(this).css('color', '#061A40' );
    }
});