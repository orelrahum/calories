import csv
import json
import os

# Define the input and output file paths
home_dir = "HEB_DB"
csv_file_path = 'moh_mitzrachim.csv'
json_file_path = 'moh_mizrachim.json'

# Initialize an empty list to store the data
data = []

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Add the group id and serving size to each row
        row['group_id'] = 555
        row['serving_size'] = 100
        data.append(row)
# Transform the data to the desired format
formatted_data = []
for row in data:
    formatted_row = {
        "id": int(row["smlmitzrach"]),
        "name": row["shmmitzrach"],
        "categoryId": "555",
        "energy": float(row["food_energy"]) if row["food_energy"] else 0,
        "fat": float(row["total_fat"]) if row["total_fat"] else 0,
        "saturatedFat": float(row["saturated_fat"]) if row["saturated_fat"] else 0,
        # "monounsaturatedFat": float(row["monounsaturatedFat"]) if row["monounsaturatedFat"] else 0,
        # "polyunsaturatedFat": float(row["polyunsaturatedFat"]) if row["polyunsaturatedFat"] else 0,
        "carbs": float(row["carbohydrates"]) if row["carbohydrates"] else 0,
        "sugar": float(row["total_sugars"]) if row["total_sugars"] else 0,
        "fiber": float(row["total_dietary_fiber"]) if row["total_dietary_fiber"] else 0,
        "protein": float(row["protein"]) if row["protein"] else 0,
        "sodium": float(row["sodium"]) if row["sodium"] else 0,
        "cholesterol": float(row["cholesterol"]) if row["cholesterol"] else 0,
        # "vitaminA": float(row["vitaminA"]) if row["vitaminA"] else 0,
        # "vitaminB1": float(row["vitaminB1"]) if row["vitaminB1"] else 0,
        # "vitaminB2": float(row["vitaminB2"]) if row["vitaminB2"] else 0,
        # "vitaminB3": float(row["vitaminB3"]) if row["vitaminB3"] else 0,
        # "vitaminB5": float(row["vitaminB5"]) if row["vitaminB5"] else 0,
        # "vitaminB6": float(row["vitaminB6"]) if row["vitaminB6"] else 0,
        # "vitaminB9": float(row["vitaminB9"]) if row["vitaminB9"] else 0,
        # "vitaminB12": float(row["vitaminB12"]) if row["vitaminB12"] else 0,
        # "vitaminC": float(row["vitaminC"]) if row["vitaminC"] else 0,
        # "vitaminD": float(row["vitaminD"]) if row["vitaminD"] else 0,
        # "vitaminE": float(row["vitaminE"]) if row["vitaminE"] else 0,
        # "vitaminK": float(row["vitaminK"]) if row["vitaminK"] else 0,
        "magnesium": float(row["magnesium"]) if row["magnesium"] else 0,
        # "calcium": float(row["calcium"]) if row["calcium"] else 0,
        # "phosphorus": float(row["phosphorus"]) if row["phosphorus"] else 0,
        # "potassium": float(row["potassium"]) if row["potassium"] else 0,
        # "iron": float(row["iron"]) if row["iron"] else 0,
        # "selenium": float(row["selenium"]) if row["selenium"] else 0,
        # "zinc": float(row["zinc"]) if row["zinc"] else 0,
        # "manganese": float(row["manganese"]) if row["manganese"] else 0,
        # "copper": float(row["copper"]) if row["copper"] else 0,
        # "choline": float(row["choline"]) if row["choline"] else 0
    }
    formatted_data.append(formatted_row)

# Write the formatted data to a JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(formatted_data, json_file, indent=4, ensure_ascii=False)

print(f"Data has been successfully converted from {csv_file_path} to {json_file_path}")