{
    "name": "qs2_HR Holidays Negative Hours",
    "summary": """
        Allow submit time-off request with negative extra hours.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Human Resources",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["qs2_hr_holidays_attendance"],
    "data": [
        "data/hr_holidays_negative_hours_data.xml",
        "views/hr_leave_type_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
