import json


try:

    with open("exercise_02_transactions.json", "r") as file:
        transaction_data = json.load(file)

except FileNotFoundError:
    print("Transaction file not found.")
    exit()


def parse_transactions(data):

    completed = []
    pending = []
    failed = []

    for txn in data:

        txn_id = txn.get("id", "Unknown ID")
        amount = txn.get("amount", 0)
        currency = txn.get("currency", "N/A")
        status = txn.get("status", "unknown")

        try:

            if amount < 0:
                raise ValueError(f"Negative amount found in transaction {txn_id}")

            cleaned_transaction = {
                "id": txn_id,
                "amount": amount,
                "currency": currency,
                "status": status
            }

            if status == "completed":
                completed.append(cleaned_transaction)

            elif status == "pending":
                pending.append(cleaned_transaction)

            elif status == "failed":
                failed.append(cleaned_transaction)

        except ValueError as error:
            print(f"Error: {error}")
            print(f"Skipping transaction {txn_id}\n")

    return completed, pending, failed


completed_transactions, pending_transactions, failed_transactions = parse_transactions(transaction_data)


with open("completed.json", "w") as file:
    json.dump(completed_transactions, file, indent=4)

with open("pending.json", "w") as file:
    json.dump(pending_transactions, file, indent=4)

with open("failed.json", "w") as file:
    json.dump(failed_transactions, file, indent=4)


print("\nTransaction Summary:\n")

print(f"Completed Transactions: {len(completed_transactions)}")
print(f"Pending Transactions: {len(pending_transactions)}")
print(f"Failed Transactions: {len(failed_transactions)}")