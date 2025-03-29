def weekday_name(day_of_week):
    """Return name of weekday."""
    days = [
        'Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday'
    ]
    if 1 <= day_of_week <= 7:
        return days[day_of_week - 1]
    return None
