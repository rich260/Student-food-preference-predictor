import glob
import json
import csv

foods = []

for file_path in glob.glob("./menus/*.json"):
    with open(file_path, "r") as f:
        data = json.load(f)
        menu_items = data["data"]["menuItems"]

        for item in menu_items:
            foods.append(item["name"].strip())

for food in foods:
    print(food)

with open("foods_raw.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Food"])
    for food in foods:
        writer.writerow([food])