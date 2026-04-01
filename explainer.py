def explain(data, place):
    return f"""
Recommended: {place['city']} ({place['state']})

Reason:
- Matches your interest: {data['interest']}
- Budget ₹{data['budget']} is suitable
- Crowd level: {place['crowd']}

Insight:
This destination gives the best balance of cost and experience.
"""