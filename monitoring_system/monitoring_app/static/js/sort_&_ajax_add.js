$(document).ready(function() {
    function updateData(data) {
        $('#cpu_load').text(data.load_percentage + '%');
        $('#min_load_100').text(data.latest_100.min_load + '%');
        $('#max_load_100').text(data.latest_100.max_load + '%');
        $('#avg_load_100').text(data.latest_100.avg_load + '%');
        $('#min_load_all').text(data.all_records.min_load + '%');
        $('#max_load_all').text(data.all_records.max_load + '%');
        $('#avg_load_all').text(data.all_records.avg_load + '%');
        updateLastRecordsTable(data.last_100_records);
    }

    function updateLastRecordsTable(records) {
        // Clear the table before adding new data
        $('#last_100_records_table_body').empty();
        // Update the table with new data
        records.forEach(function(record) {
            $('#last_100_records_table_body').append(
                '<tr>' +
                    '<td>' + record.formatted_timestamp + '</td>' +
                    '<td>' + record.load_percentage + '</td>' +
                '</tr>'
            );
        });
    }

    function fetchData() {
        $.ajax({
            url: '/api/',
            type: 'GET',
            success: function(data) {
                updateData(data);
            },
            error: function(xhr, status, error) {
                console.error(error);
            },
            complete: function() {
                setTimeout(fetchData, 10000);
            }
        });
    }

    fetchData();

    function sortTable(n) {
        var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
        table = document.getElementById("cpu_load_table");
        switching = true;
        dir = "asc";
        while (switching) {
            switching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[n];
                y = rows[i + 1].getElementsByTagName("TD")[n];
                if (dir == "asc") {
                    if (n === 0) { // Sort by Timestamp
                        if (new Date(x.innerHTML) > new Date(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    } else { // Sort by Load Percentage
                        if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                } else if (dir == "desc") {
                    if (n === 0) { // Sort by Timestamp
                        if (new Date(x.innerHTML) < new Date(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    } else { // Sort by Load Percentage
                        if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
                            shouldSwitch = true;
                            break;
                        }
                    }
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                switchcount++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    }

    $("#timestamp_header").click(function() {
        sortTable(0);
    });
    $("#load_percentage_header").click(function() {
        sortTable(1);
    });
});
