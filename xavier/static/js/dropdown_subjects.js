$(function() {
    // Scores
    $('a[name="subjects"]').each(function() {
        $ul = $(this).parent().find('ul.list_subjects');
        if ($('li', $ul).length == 1) {
            $(this).find('.caret').remove();
        }
    });
    $('a[name="subjects"]').click(function() {
        $ul = $(this).parent().find('ul.list_subjects');
        $('ul.list_subjects', $(this).parent().siblings()).hide();
        if ($('li', $ul).length == 1) {
            window.location = $('li a', $ul).attr('href');
        } else {
            $ul.toggle();
        }
    });
});
