from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from ml_model import predict_ml
from recommender import refine_with_rules
from optimizer import optimize_budget
from explainer import explain
from itinerary import generate_itinerary
from insights import generate_insights

app = Flask(__name__)
CORS(app)

@app.route('/plan', methods=['POST'])
def plan_trip():
    data = request.json
    input_data = {
        "budget": data['budget'],
        "interest": data['interest'],
        "crowd": "low",
        "season": "summer"
    }
    city = predict_ml(input_data)
    place = refine_with_rules(city, data)
    itinerary = generate_itinerary(city)
    budget = optimize_budget(data['budget'])
    explanation = explain(data, place)
    insights = generate_insights(data, place)

    return jsonify({
        "destination": place,
        "itinerary": itinerary,
        "budget_split": budget,
        "explanation": explanation,
        "insights": insights
    })

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()

    if "cheap" in user_message:
        budget = 6000
    elif "medium" in user_message:
        budget = 8000
    else:
        budget = 10000

    if "mountain" in user_message:
        interest = "mountains"
    elif "beach" in user_message:
        interest = "beach"
    else:
        interest = "nature"

    data = {"budget": budget, "interest": interest}
    input_data = {"budget": budget, "interest": interest, "crowd": "low", "season": "summer"}

    city = predict_ml(input_data)
    place = refine_with_rules(city, data)
    itinerary = generate_itinerary(city)
    budget_split = optimize_budget(budget)
    explanation = explain(data, place)
    insights = generate_insights(data, place)

    return jsonify({
        "message": f"I recommend {place['city']} for your trip. Here's your plan.",
        "user_input": user_message,
        "destination": place,
        "itinerary": itinerary,
        "budget": budget_split,
        "explanation": explanation,
        "insights": insights
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
