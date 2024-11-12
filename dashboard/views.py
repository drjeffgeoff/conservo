from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    context = {
        "fields": [
            {"name": "Field A", "rainfall": 0.74, "moisture": 0.37},
            {"name": "Field B", "rainfall": 0.30, "moisture": 0.36},
            {"name": "Field C", "rainfall": 0.28, "moisture": 0.29},
        ],
        "weather": {
            "city": "Kampala",
            "temperature": 28.09,
            "description": "few clouds"
        },
        # Example data
        "soil_moisture_data": [0.35, 0.36, 0.34, 0.37, 0.33, 0.39],
        "notifications": [
            {
                "message": "New soil moisture reading recorded: Soil wet at Field A",
                "time": "2024-07-26 10:24",
                "unread": True
            }
        ]
    }
    return render(request, 'dashboard/dashboard.html', context)
