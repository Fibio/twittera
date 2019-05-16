// Call the dataTables jQuery plugin
$(document).ready(function() {
    console.log($('#dataTable').attr("data-uri"));
    $('#dataTable').DataTable({
        "ajax": {
            url: $('#dataTable').attr("data-uri"),
            dataSrc: '',
        },
        "columns": [
            { "title": "Word", "data": "word" },
            { "title": "Count", "data": "count" },
        ],
    });
});
