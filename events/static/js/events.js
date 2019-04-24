function getTime(time){
     $(document).ready(function(){
         var hour = time.split(':')[0];
         var minute = time.split(':')[1];
         $('select#id_minute.time-input').val(minute);

         // remove the leading 0
         if(hour < 10){
             hour = hour.substring(1, 2);
         }

         //after noon
        if(hour > 12){
            $('select#id_hour.time-input').val(hour - 12);
            $('select#id_meridiem.time-input').val("PM");
        }

        //noon
        else if (hour == 12) {
            $('select#id_hour.time-input').val(12);
            $('select#id_meridiem.time-input').val("PM");
        }

        //midnight
        else if (hour == 0){
            $('select#id_hour.time-input').val(12);
            $('select#id_meridiem.time-input').val("AM");
        }

        //before noon
        else {
            $('select#id_hour.time-input').val(hour);
            $('select#id_meridiem.time-input').val("AM");
        }
    });
}