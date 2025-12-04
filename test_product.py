import pytest
from product import get_product_details

def test_get_employee_details():
    prd_id = "P102"
    name = "Wireless Bluetooth"
    quantity = 2
    price = 1500

    expected_output = (
        "Product ID: P102\n"
        "Product Name: Wireless Bluetooth\n"
        "Quantity: 2\n"
        "Price: ₹1500\n"
    )

    assert get_product_details(prd_id, name, quantity, price) == expected_output