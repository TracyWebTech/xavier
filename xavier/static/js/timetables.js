function add_new_line( value, tabindex ) {
    $section1 = $('<section>').attr('class', 'span2 timetable');
    $section2 = $('<section>').attr('class', 'span2 timetable');

    $input1 = $('<input>').attr({type: 'time',
                                 class: 'times timetable time-start',
                                 placeholder: START,
                                 value: value,
                                 pattern: '[0-2][0-9]:[0-6][0-9]',
                                 tabindex: (parseInt(tabindex)+1)});
    $input2 = $('<input>').attr({type: 'time',
                                 class: 'times timetable time-end',
                                 placeholder: END,
                                 value: '',
                                 pattern: '[0-2][0-9]:[0-6][0-9]',
                                 tabindex: (parseInt(tabindex)+2)});

    $section1.append($input1);
    $section2.append($input2);

    $li = $('<li>').addClass('start_end');
    $li.append($section1);
    $li.append($section2);

    $i = $('<i>').attr('class', 'icon-remove icon-white');
    $btn = $('<button>').attr('class', 'btn btn-danger');
    $a = $('<a>').attr({href: '#', id: 'remove_line'});
    $btn.append($i);
    $a.append($btn);
    $li.append($a);

    $('li#start_end_example').before($li);
    $input1.focus();
}

$(function() {

    /* TIMETABLE ADD AND EDIT */

    // Remove schedule from timetable
    $('ul#timetable_list').on('click', '#remove_line', function() {
        $li = $(this).parent();
        var time_combination_pk = '';
        if ($li.attr('id') != undefined) {
            time_combination_pk = $li.attr('id').replace(/\D+/, '');
        }
        request = $.ajax({
            type: "POST",
            url: UPDATE_TIMES_URL,
            data: {
                'time_combination_pk': time_combination_pk,
            },
        });
        request.done(function() {
            $li.remove();
        });
    });

    // Add new line for new start - end inputs
    $('.timetable-add-line').click(function() {
        add_new_line('', $(this).parents('li:first').prev().find('input:last').attr('tabindex'));
    });

    $('ul#timetable_list').on("keypress", ".time-end", function(event) {
        if (event.which == 0 && event.shiftKey == false || event.which == 13) {
            if ($(this).parent().parent().next().find('.time-start').val().length == 0 && $(this).parent().parent().next().attr('id') == "start_end_example") {
                if ($(this).val().length == 0) {
                    console.log($(this).attr('tabindex'));
                    add_new_line('', $(this).attr('tabindex'));
                } else {
                    add_new_line($(this).val(), $(this).attr('tabindex'));
                }
            }
        }
    });

    // Adding timetables
    if ($('.timetable_name').val() == "") {
        $('a#add_new_line').css('display', 'none');
        $('ul#timetable_list').css('display', 'none');
    }

    // Save the timetable name
    $(document).on('click', '#apply_timetable_name', function() {
        var timetable = $(this).parent().find('.timetable_name');
        var timetable_pk = '';
        if (timetable.attr('id') != undefined) {
            timetable_pk = timetable.attr('id').replace(/\D+/, '');
        }
        request = $.ajax({
            type: "POST",
            url: UPDATE_TIMETABLE_NAME_URL,
            data: {'timetable_name': timetable.val(),
                   'timetable_pk': timetable_pk},
        });
        request.done(function ( data ) {
            timetable.attr('id', data['pk']);
            $('ul#timetable_list').css('display', 'block');

        });
    });

    // Save the timetable with the modifications
    $('ul#timetable_list').on('change', '.times', function() {
        // If the element has an ID, it means that he already exists
        $li = $(this).parent().parent();
        var start = $li.find('input.times:first').val();
        var end = $li.find('input.times:last').val();
        var time_combination_pk = '';
        var timetable_pk = $('.timetable_name').attr('id').replace(/\D+/, '');
        if ($li.attr('id') != undefined) {
            time_combination_pk = $li.attr('id').replace(/\D+/, '');
        }
        request = $.ajax({
            type: "POST",
            url: UPDATE_TIMES_URL,
            data: {
                'start': start,
                'end': end,
                'time_combination_pk': time_combination_pk,
                'timetable_pk': timetable_pk
            },
        });
        request.done(function ( data ) {
            if ($li.attr('id') == undefined) {
                $li.attr('id', 'timeline-'+data);
            }
        });
    });

    /* TIMETABLES LIST */

    // remove timetable
    $(document).on('click', '.remove_timetable', function() {
        var timetable_pk = $('.timetable_name').attr('id').replace(/\D+/, '');
        request = $.ajax({
            type: 'POST',
            url: REMOVE_TIMETABLE,
            data: {
                'timetable_pk': timetable_pk
            },
        });
        request.done(function( data ) {
            window.location.href = TIMETABLE_LIST_URL;
        });
    });

    // Choose timetable popover control
    var activePopOver = null;
    $('.timetable_block').popover({html: 'true', trigger: 'manual'}).click(function() {
        if (activePopOver && $(activePopOver)[0] != $(this)[0]) {
            $(activePopOver).popover('hide');
        }
        $(this).popover('toggle');
        activePopOver = $(this);
        return false;
    });

    // ajax to save classtimetable
    $('.timetable_to_apply').on('click', '.apply_timetable_to_class', function(e) {
        request = $.ajax({
            type: 'POST',
            url: URL_APPLY_CLASSTIMETABLE,
            data: {
                'timetable_pk': $(this).attr('id').replace(/\D+/, ''),
                'class_pk': CLASSROOM_PK
            },
        });
        request.done(function() {
            if (CLASS_TIMETABLE_URL != "") {
                window.location.href = CLASS_TIMETABLE_URL;
            } else {
                location.reload();
            }
        });
    });

});
