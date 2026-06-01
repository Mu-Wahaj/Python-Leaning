def shipping_cost(weight, distance):
    # Calculate shipping cost based on weight and distance
    base_cost = 5.0  # Base cost for shipping
    cost_per_kg = 2.0  # Cost per kilogram
    cost_per_km = 0.5  # Cost per kilometer
    
    total_cost = base_cost + (cost_per_kg * weight) + (cost_per_km * distance)
    return total_cost
