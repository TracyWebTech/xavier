$(function() {
    /* Timetable */
    $('a[name="subjects"]').click(function() {
        $ul = $(this).parent().find('ul.list_subjects');
        $('ul.list_subjects', $(this).parent().parent().siblings()).hide();
        $('ul.list_subjects', $(this).parent().siblings()).hide();
        $ul.toggle();
    });

    $('.subject_choice').click(function() {
        $(this).parent().parent().toggle();

        var classroom = $('table.timetable_for_class').find('th:first').attr('id');
        var subject = $(this).attr('rel');

        $td = $(this).parent().parent().parent().parent();
        $td.find('a[name="subjects"] div').empty().prepend($(this).text());
        var class_subject_time_pk = '';
        if ($td.attr('id') != undefined) {
            class_subject_time_pk = $td.attr('id');
        }

        var time = $td.parent().find('.time').attr('id');
        var weekday = $td.find('.timetable_subjects').attr('rel');

        request = $.ajax({
            type: "POST",
            url: UPDATE_CLASSSUBJECT_TIME,
            data: {'subject_pk': subject,
                   'class': classroom,
                   'time': time,
                   'weekday': weekday,
                   'class_subject_time_pk': class_subject_time_pk,
            },
        });
        request.done(function ( data ) {
            $td.attr('id', data);
        });
    });
});
