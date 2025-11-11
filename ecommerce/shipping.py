# this is a module inside a ecommerce package to be used in other parts of the ecommerce application


def calculate_shipping_cost(weight_kg, distance_km):
    base_cost = 5.0  # base cost in dollars
    cost_per_kg = 2.0  # cost per kilogram
    cost_per_km = 0.5  # cost per kilometer

    total_cost = base_cost + (cost_per_kg * weight_kg) + (cost_per_km * distance_km)
    return total_cost


def estimate_delivery_time(distance_km, speed_kmh=60):
    if speed_kmh <= 0:
        raise ValueError("Speed must be greater than zero.")
    delivery_time_hours = distance_km / speed_kmh
    return delivery_time_hours


def is_expedited_shipping(weight_kg):
    return weight_kg < 2.0  # expedited shipping for packages under 2 kg


def calculate_insurance_cost(value_usd):
    insurance_rate = 0.02  # 2% of the item's value
    return value_usd * insurance_rate


def track_package(tracking_number):
    # Dummy implementation for tracking
    return f"Package with tracking number {tracking_number} is in transit."


def apply_discount(shipping_cost, discount_percentage):
    discount_amount = shipping_cost * (discount_percentage / 100)
    return shipping_cost - discount_amount


def calculate_tax(shipping_cost, tax_rate):
    tax_amount = shipping_cost * (tax_rate / 100)
    return shipping_cost + tax_amount


def generate_shipping_label(recipient_name, address, weight_kg):
    label = f"Shipping Label:\nRecipient: {recipient_name}\nAddress: {address}\nWeight: {weight_kg} kg"
    return label
