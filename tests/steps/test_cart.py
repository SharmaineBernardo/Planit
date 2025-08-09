from pytest_bdd import when, then, scenarios, parsers
from tests.pages.shop_page import ShopPage
from tests.pages.cart_page import CartPage

scenarios("features/cart.feature")


@when(parsers.parse("I buy '{pieces:d}' pieces of '{item_name}'"))
def step_add_to_cart(shop_page: ShopPage, pieces: int, item_name: str) -> None:
    for _ in range(pieces):
        shop_page.add_to_cart(item_name)


@when("I checkout the items")
def step_checkout_items(shop_page: ShopPage) -> None:
    shop_page.go_to_page("Cart")


@then("I should see that the following details for each item are displayed:")
def step_verify_cart_item_details(
    cart_page: CartPage, datatable: list[list[str]]
) -> None:
    table_rows = datatable[1:]
    for item, price, subtotal in table_rows:
        actual_price = cart_page.get_item_price(item)
        actual_subtotal = cart_page.get_item_subtotal(item)

        assert actual_price == float(price), f"Incorrect price for item '{item}'"
        assert actual_subtotal == float(subtotal), (
            f"Incorrect subtotal for item '{item}'"
        )


@then(
    parsers.parse(
        "I should see that total cost '{total:f}' equals the sum of subtotals of these items:"
    )
)
def step_verify_total_cost(
    cart_page: CartPage, total: float, datatable: list[str]
) -> None:
    actual_total_cost = 0.0
    for item in datatable:
        actual_total_cost += cart_page.get_item_subtotal(item[0])
    assert actual_total_cost == total


@then(parsers.parse("I should see that total cost of '{total}' is displayed"))
def step_total_cost_is_visible(cart_page: CartPage, total: str) -> None:
    cart_page.total_cost_is_visible(total)


@then("I should see that subtotals for these items are correct:")
def step_verify_subtotal(cart_page: CartPage, datatable: list[list[str]]) -> None:
    table_rows = datatable[1:]
    for item, expected_subtotal in table_rows:
        actual_price = cart_page.get_item_price(item)
        actual_quantity = cart_page.get_item_quantity(item)

        assert float(expected_subtotal) == float(actual_quantity * actual_price), (
            f"Incorrect subtotal for item '{item}'"
        )
