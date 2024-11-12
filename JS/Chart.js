<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    var ctx = document.getElementById('soilMoistureChart').getContext('2d');
    var soilMoistureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [...Array(soil_moisture_data.length).keys()], // Replace with actual dates
            datasets: [{
                label: 'Soil Moisture',
                data: {{ soil_moisture_data }},
                borderColor: 'teal',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
</script>
