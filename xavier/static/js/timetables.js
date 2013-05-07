function add_new_line( value ) {
    $section1 = $('<section>').attr('class', 'span2 timetable');
    $section2 = $('<section>').attr('class', 'span2 timetable');

    $input1 = $('<input>').attr({type: 'time',
                                 class: 'times timetable time-start',
                                 placeholder: START,
                                 value: value,
                                 pattern: '[0-2][0-9]:[0-6][0-9]'});
    $input2 = $('<input>').attr({type: 'time',
                                 class: 'times timetable time-end',
                                 placeholder: END,
                                 value: '',
                                 pattern: '[0-2][0-9]:[0-6][0-9]'});

    $section1.append($input1);
    $section2.append($input2);

    $li = $('<li>').addClass('start_end');
    $li.append($section1);
    $li.append($section2);

    $('ul#timetable_list').append($li);
    $section1.focus();
}

$(function() {

    /* TIMETABLE ADD AND EDIT */

    // Add the icon with minus sign
    $(document).on('mouseenter', 'li.start_end', function() {

        $i = $('<i>').addClass('icon-minus-sign');
        $a = $('<a>').attr('href', '#');

        $a.attr('id', 'remove_line');

        $a.append($i);
        $a.css('position', 'absolute');
        $a.css('margin-top', '6px');

        $(this).prepend($a);
    });

    // Remove minus sign icon
    $(document).on('mouseleave', 'li.start_end', function() {
        $(this).find($('#remove_line')).remove();
    });

    // Remove schedule from timetable
    $(document).on('click', '#remove_line', function() {
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
    $('#add_new_line').click(function() {
        add_new_line('');
    });

    $('.time-end').keydown(function(event) {
        if (event.which == 9) {
            if ($(this).parent().parent().next().length == 0) {
                add_new_line($(this).val());
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
            TIMETABLE_SLUG = data['slug'];
            timetable.attr('id', data['pk']);
            $('a#add_new_line').css('display', 'block');
            $('ul#timetable_list').css('display', 'block');

        });
    });

    // Save the timetable with the modifications
    $(document).on('change', '.times', function() {
        // If the element has an ID, it means that he already exists
        $li = $(this).parent().parent();
        var start = $li.find('input.times:first').val();
        var end = $li.find('input.times:last').val();
        var time_combination_pk = '';
        var timetable_slug = TIMETABLE_SLUG;
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
                'timetable_slug': timetable_slug
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
        var $li = $(this).parent();
        var timetable_pk = $(this).parent().find('a.timetable_url');
        var timetable_pk = timetable_pk.attr('id').replace(/\D+/, '');
        request = $.ajax({
            type: 'POST',
            url: REMOVE_TIMETABLE,
            data: {
                'timetable_pk': timetable_pk
            },
        });
        request.done(function( data ) {
            $li.remove();
        });
    });
});
