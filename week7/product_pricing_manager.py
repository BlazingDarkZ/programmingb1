import logging




logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_discount(category, tier):
    category_discounts = {
        "Electronics": 10,
        "Clothing": 15,
        "Books": 5,
        "Home": 12
    }

    tier_discounts = {
        "Premium": 5,
        "Standard": 0,
        "Budget": 2
    }

    category_discount = category_discounts.get(category, 0)
    tier_discount = tier_discounts.get(tier, 0)

    return category_discount + tier_discount


def process_products(input_file, output_file):
    try:
        products = []
        total_discount = 0

        with open(input_file, "r") as file:
            for line_number, line in enumerate(file, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 4:
                        logging.warning(f"Line {line_number}: Invalid format")
                        continue

                    name, price_text, category, tier = parts
                    base_price = float(price_text)

                    discount_percent = calculate_discount(category, tier)
                    discount_amount = base_price * discount_percent / 100
                    final_price = base_price - discount_amount

                    products.append({
                        "name": name,
                        "base_price": base_price,
                        "discount_percent": discount_percent,
                        "discount_amount": discount_amount,
                        "final_price": final_price
                    })

                    total_discount += discount_percent

                except ValueError:
                    logging.error(f"Line {line_number}: Invalid price")
                    continue

        with open(output_file, "w") as file:
            file.write("=" * 80 + "\n")
            file.write("PRICING REPORT\n")
            file.write("=" * 80 + "\n")
            file.write(f"{'Product Name':<25} {'Base Price':>12} "
                       f"{'Discount %':>12} {'Discount $':>12} {'Final Price':>12}\n")
            file.write("-" * 80 + "\n")

            for product in products:
                file.write(f"{product['name']:<25} "
                           f"${product['base_price']:>11.2f} "
                           f"{product['discount_percent']:>11.1f}% "
                           f"${product['discount_amount']:>11.2f} "
                           f"${product['final_price']:>11.2f}\n")

            file.write("=" * 80 + "\n")

        average_discount = total_discount / len(products) if products else 0

        print("\nProcessing Complete!")
        print("Total products processed:", len(products))
        print(f"Average discount applied: {average_discount:.2f}%")
        print("Report saved to:", output_file)

        logging.info(f"Processed {len(products)} products successfully")

    except FileNotFoundError:
        print("Error: Input file not found.")
        logging.error("Input file not found.")

    except PermissionError:
        print("Error: Cannot write to output file.")
        logging.error("Permission denied.")

    except Exception as error:
        print("Unexpected error:", error)
        logging.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    import os
    print("Current working directory:", os.getcwd())
    process_products(
    "C:/Users/S/Documents/GitHub/azure-appointment-app/programmingb1/week7/products.txt",
    "C:/Users/S/Documents/GitHub/azure-appointment-app/programmingb1/week7/pricing_report.txt"
    )
            