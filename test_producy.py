import pytest
from products import Product


# Test that creating a normal product works.
def test_create_product():
    product = Product("test Product", price=10, quantity=5)
    assert product.name == "test Product"
    assert product.price == 10
    assert product.quantity == 5
    assert product.is_active() is True


# Test that creating a product with invalid details (empty name, negative price) invokes an exception.
def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=10, quantity=5)

    with pytest.raises(ValueError):
        Product("Test Product", price=-10, quantity=5)

    with pytest.raises(ValueError):
        Product("Test Product", price=10, quantity=-5)


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_product_become_inactive_at_zero_quantity():
    product = Product("Test Product", price=10, quantity=0)
    assert product.is_active() is False


# Test that product purchase modifies the quantity and returns the right output.
def test_product_purchase():
    product = Product("Test Product", price=10, quantity=5)
    total_price = product.buy(3)
    assert product.quantity == 2
    assert total_price == 30


# Test that buying a larger quantity than exists invokes exception
def test_product_purchase_with_insufficient_quantity():
    product = Product("Test Product", price=10, quantity=5)
    with pytest.raises(Exception):
        product.buy(10)


if __name__ == "__main__":
    pytest.main()