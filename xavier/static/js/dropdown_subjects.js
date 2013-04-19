$(function() {
    $('a[name="subjects"]').click(function() {
        $('ul.list_subjects', $(this).parent().siblings()).hide();
        $(this).parent().find('ul.list_subjects').toggle();
    });
});
