import json


try:

    with open("exercise_03_server.log", "r") as file:
        lines = file.readlines()

except UnicodeDecodeError:
    print("Error reading log file due to encoding issue.")
    exit()


def extract_errors(lines):

    errors = []

    for line in lines:

        if "ERROR" in line:
            errors.append(line)

    return errors


error_lines = extract_errors(lines)

summary = {}


for line in error_lines:

    date = line.split()[0]

    if date in summary:
        summary[date] += 1

    else:
        summary[date] = 1


with open("digest.json", "w") as file:
    json.dump(summary, file, indent=4)


print("\nDaily Error Summary:\n")

for date, count in summary.items():
    print(f"{date} : {count} errors")