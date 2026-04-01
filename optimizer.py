def optimize_budget(budget):
    return {
        "transport": int(budget * 0.4),
        "stay": int(budget * 0.3),
        "food": int(budget * 0.2),
        "activities": int(budget * 0.1)
    }