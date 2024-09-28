import csv
import json

# Path to your CSV file
csv_file_path = "C:\\Users\\MITYash\\PycharmProjects\\pythonProject7\\Book11.csv"
# Path to your JSON template file
json_template_path = "C:\\Users\\MITYash\\PycharmProjects\\pythonProject7\\template.json"
# Path to save the JSON output
json_output_path = "C:\\Users\\MITYash\\PycharmProjects\\pythonProject7\\output.json"

# Read the JSON template
with open(json_template_path, "r") as template_file:
    json_template = json.load(template_file)

# Ensure 'items' key exists in the JSON template
if 'items' not in json_template:
    json_template['items'] = []

# Read the CSV file and populate the JSON template
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Create a new item dictionary based on the template
        item = json_template.get("item", {}).copy()

        # Populate the item with data from the CSV row
        for key, value in row.items():
            item[key] = value

        # Append the item to the 'items' list in the template
        json_template["items"].append(item)

# Save the JSON output
with open(json_output_path, "w") as json_file:
    json.dump(json_template, json_file, indent=4)

print(f"CSV data from '{csv_file_path}' has been successfully converted to JSON as '{json_output_path}'.")
