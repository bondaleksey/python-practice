def holidays_switch(season):
    # All of the following if and elif conditions have "season ==":
    if season == "Winter":
        holiday = "New Year's Day"
    elif season == "Spring":
        holiday = "May Day"
    elif season == "Summer":
        holiday = "Juneteenth"
    elif season == "Fall":
        holiday = "Halloween"
    else:
        holiday = "Personal day off"
    return holiday


def holidays_dict(season):
    holiday = {
        "Winter": "New Year's Day",
        "Spring": "May Day",
        "Summer": "Juneteenth",
        "Fall": "Halloween",
    }.get(season, "Personal day off")
    return holiday

if __name__ == "__main__":
    season = 'Fall'
    print(holidays_switch(season))
    print(holidays_dict(season))
    