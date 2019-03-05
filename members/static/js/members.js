function getPreferences(arr){
    $(document).ready(function(){
        var preferenceArray;
        preferenceArray = arr;
        for(i = 0; i < preferenceArray.length; i++) {
            $('input[type=checkbox]').each(function (){
                if($(this).val() == preferenceArray[i]){
                    $(this).prop('checked', true);
                }
            });
        }
    });
}