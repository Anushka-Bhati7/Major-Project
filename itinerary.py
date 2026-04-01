def generate_itinerary(city):

    if city == "Shimla":
        return [
            "Day 1: Arrival + Mall Road visit",
            "Day 2: Kufri + Adventure activities",
            "Day 3: Jakhoo Temple + Return"
        ]

    elif city == "Manali":
        return [
            "Day 1: Arrival + Local market",
            "Day 2: Solang Valley + Snow activities",
            "Day 3: Rohtang Pass + Return"
        ]

    elif city == "Goa":
        return [
            "Day 1: Beach + Relax",
            "Day 2: Water sports",
            "Day 3: Night market + Return"
        ]

    else:
        return [
            "Day 1: Explore city",
            "Day 2: Visit attractions",
            "Day 3: Return"
        ]