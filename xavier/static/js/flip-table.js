function transpose() {
    var $table = $("#timetable_class");
    var num_cols = $table.find('tr:first').find('th, td').length;
    
    var $thead = $('<thead>');
    var $tbody = $('<tbody>');
    for (i = 1; i <= num_cols; i++) {
        var $tr = $("<tr>").append($("tr td:nth-child(1), tr th:nth-child(1)"));
        if (i == 1) {
            $thead.append($tr);
        } else {
            $tbody.append($tr);
        }
    }
    $table.empty().append($thead).append($tbody); 
}

$(function() {
    window.current_width = window.innerWidth;
    if (window.innerWidth <= 800) {
        transpose();
    }

    $(window).on('resize', function() {
        if ((window.innerWidth <= 800 && window.current_width > 800) || (window.innerWidth > 800 && window.current_width <= 800)) {
            transpose();
        }
        window.current_width = window.innerWidth;
    });
});
