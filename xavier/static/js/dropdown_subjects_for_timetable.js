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

        var subject_for_time = $('strong', $(this)).text();
        var teacher = $('span', $(this)).text();
        var subject_chosen = $(this).parents('td:first').find('.subject_chosen');

        var classroom = $('table.timetable_for_class').find('th:first').attr('id');
        var subject_pk = $(this).attr('rel');

        $td = $(this).parents('td:first');
        var td_index = $td.index()+1;
        console.log(td_index);
        $td.find('a[name="subjects"] div').empty().prepend($(this).text());
        var class_subject_time_pk = '';
        if ($td.attr('id') != undefined) {
            class_subject_time_pk = $td.attr('id');
        }

        var time = '';
        var transposed = false;
        if ($td.parent().find('.time').attr('id') != undefined) {
            time = $td.parent().find('.time').attr('id');
        }
        if (time.length == 0) {
            time = $("table.timetable_for_class thead th:nth-child("+ td_index +")").attr('id');
            transposed = true;
        }
        var weekday = $td.find('.timetable_subjects').attr('rel');

        request = $.ajax({
            type: "POST",
            url: UPDATE_CLASSSUBJECT_TIME,
            data: {'subject_pk': subject_pk,
                   'class': classroom,
                   'time': time,
                   'weekday': weekday,
                   'class_subject_time_pk': class_subject_time_pk,
            },
        });
        request.done(function ( data ) {
            if (!transposed) {
                $td.attr('id', data);
            } else {
                $("table.timetable_for_class thead th:nth-child("+ td_index +")").attr('id', data);
            }
        });
        var $strong = $('<strong>');
        var $br = $('<br>');
        var $span = $('<span>').addClass('muted');
        $strong.append(subject_for_time);
        $span.append(teacher);
        subject_chosen.empty();
        subject_chosen.append($strong);
        subject_chosen.append($br);
        subject_chosen.append($span);
        if (subject_pk.length == 0) {
            var $br = $('<br>');
            subject_chosen.empty();
            subject_chosen.append('&nbsp;');
            subject_chosen.append($br);
            subject_chosen.append('&nbsp;');
        }
    });
});
