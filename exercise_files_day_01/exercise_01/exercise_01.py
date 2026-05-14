import json
try:
    with open("exercise_01_inventory.json", "r") as file:
        inventory_data = json.load(file)
except FileNotFoundError:
    print("Inventory file not found.")
    exit()
    
def check_stock(items):
    healthy = []
    low_stock = []

    for item in items:

        if item["qty"] < item["reorder_at"]:
            low_stock.append(item)

        else:
            healthy.append(item)

    return healthy, low_stock

healthy_items, low_stock_items = check_stock(inventory_data)
print("\nLow Stock Report:\n")
print(f"Total low stock items: {len(low_stock_items)}\n")

for item in low_stock_items:
    print(f"⚠ {item['item']}: {item['qty']} units (reorder at {item['reorder_at']})")

with open("alerts.json", "w") as file:
    json.dump(low_stock_items, file, indent=4)