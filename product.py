def get_product_details(prd_id, name, quantity, price):
    return (
        f"Product ID: {prd_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ₹{price}\n"
    )

# Example usage
if __name__ == "__main__":
    print(get_product_details("P102", "Wireless Bluetooth", 2, 1500))
