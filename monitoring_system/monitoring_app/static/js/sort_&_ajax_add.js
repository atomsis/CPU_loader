$(document).ready(function() {
    function fetchLast100Records() {
        $.ajax({
            url: '/api/get_last_100_cpu_load/',
            type: 'GET',
            success: function(data) {
                updateLast100RecordsTable(data);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    }

    function updateLast100RecordsTable(records) {
        $('#last_100_records_table_body').empty();
        records.forEach(function(record) {
            $('#last_100_records_table_body').append(
                '<tr>' +
                    '<td>' + record.timestamp + '</td>' +
                    '<td>' + record.load_percentage + '</td>' +
                '</tr>'
            );
        });
    }

    function fetchData() {
        $.ajax({
                url: '/api/cpu/load/',
                type: 'GET',
                success: function(data) {
                     $('#latest_cpu').text('Latest CPU=' + data.last_cpu + '%');
                     $('#min_load_value').text(data.latest_100.min_load + '%');
                     $('#max_load_value').text(data.latest_100.max_load + '%');
                     $('#avg_load_value').text(data.latest_100.avg_load + '%');
                     $('#min_load_all').text(data.all_records.min_load + '%');
                     $('#max_load_all').text(data.all_records.max_load + '%');
                     $('#avg_load_all').text(data.all_records.avg_load + '%');
                    },
                error: function(xhr, status, error) {
                     console.error(error);
                    },
                     complete: function() {
                        setTimeout(fetchData, 10000);
                    }
                });
            }

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

    fetchLast100Records();
    fetchData()
    setInterval(fetchLast100Records, 10000);
});
