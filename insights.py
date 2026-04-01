def generate_insights(data, place):
    insights = []

    if data['budget'] < place['avg_budget']:
        insights.append("Your budget is slightly low, consider increasing it for better experience.")

    if place['crowd'] == "high":
        insights.append("This destination may be crowded during this time.")

    if place['crowd'] == "low":
        insights.append("Great choice! This place is less crowded and peaceful.")

    return insights