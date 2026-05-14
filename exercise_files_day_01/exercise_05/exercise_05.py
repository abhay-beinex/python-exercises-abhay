import json


try:

    file = open("exercise_05_sales_week.json", "r")

    sales_data = json.load(file)


    def compute_revenue(sales):

        revenue_dict = {}

        for item in sales:

            product = item["product"]
            units_sold = item["units_sold"]
            unit_price = item["unit_price"]

            revenue = units_sold * unit_price

            revenue_dict[product] = revenue

        return revenue_dict


    revenue_data = compute_revenue(sales_data)


    sorted_revenue = sorted(
        revenue_data.items(),
        key=lambda item: item[1],
        reverse=True
    )


    report_file = open("report.txt", "w")

    report_file.write("WEEKLY SALES REPORT\n\n")


    grand_total = 0


    for product, revenue in sorted_revenue:

        line = f"{product} : {revenue:.2f}\n"

        report_file.write(line)

        grand_total += revenue


    report_file.write(f"\nGrand Total Revenue: {grand_total:.2f}")


    print("Sales report generated successfully.")


except FileNotFoundError:
    print("Sales data file not found.")


finally:

    try:
        file.close()
    except:
        pass

    try:
        report_file.close()
    except:
        pass