import json

def refine_with_rules(city, data):
    with open('data.json') as f:
        places = json.load(f)

    for place in places:
        if place['city'] == city:
            score = 0

            if place['type'] == data['interest']:
                score += 2

            if data['budget'] >= place['avg_budget']:
                score += 2

            if place['crowd'] == "low":
                score += 1

            place['score'] = score
            return place

    return None