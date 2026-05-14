import json


try:

    with open("exercise_04_employee_123.json", "r") as file:
        employee_data = json.load(file)


except json.JSONDecodeError:
    print("Invalid JSON format in employee config file.")
    exit()


patch = {
    "role": "engineer",
    "location": "Kochi",
    "active": False
}


def merge_config(base, patch):

    for key, value in patch.items():

        old_value = base.get(key, "Not Found")

        base[key] = value

        print(f"Updated {key}: {old_value} → {value}")

    return base


updated_config = merge_config(employee_data, patch)


with open("exercise_04_employee_123.json", "w") as file:
    json.dump(updated_config, file, indent=4)