# learning modules in python programming
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added.
# Modules are used to break down large programs into small manageable and
# organized files. They also provide reusability of code.
# We can define our most used functions in a module and import it, instead of copying their definitions into different programs.
# Example of a module in Python

import converters
import ecommerce.shipping

print(converters.lbs_to_kg(150))  # Convert 150 pounds to kilograms
# this file is a converter functions file to be used in other modules

numbers = [1, 2, 3, 4, 5]

print(converters.find_max(numbers))  # Output: 5
print(converters.find_min(numbers))  # Output: 1
print(converters.calculate_average(numbers))  # Output: 3.0
print(converters.calculate_sum(numbers))  # Output: 15

# this is a module outside a ecommerce package using the functions inside the ecommerce package

weight = 10  # in kg
distance = 100  # in km
shipping_cost = ecommerce.shipping.calculate_shipping_cost(weight, distance)
print(f"Shipping Cost: ${shipping_cost:.2f}")
delivery_time = ecommerce.shipping.estimate_delivery_time(distance)
print(f"Estimated Delivery Time: {delivery_time:.2f} hours")
expedited = ecommerce.shipping.is_expedited_shipping(weight)
print(f"Is Expedited Shipping: {expedited}")
insurance_cost = ecommerce.shipping.calculate_insurance_cost(500)  # item value in USD
print(f"Insurance Cost: ${insurance_cost:.2f}")
tracking_info = ecommerce.shipping.track_package("TRACK123456")
print(tracking_info)
discounted_cost = ecommerce.shipping.apply_discount(shipping_cost, 10)  # 10
print(f"Discounted Shipping Cost: ${discounted_cost:.2f}")
taxed_cost = ecommerce.shipping.calculate_tax(shipping_cost, 5)  # 5% tax
print(f"Taxed Shipping Cost: ${taxed_cost:.2f}")
shipping_label = ecommerce.shipping.generate_shipping_label(
    "John Doe", "123 Main St, Anytown, USA", weight
)
print(shipping_label)
# this is a module inside a ecommerce package to be used in other parts of the ecommerce application
