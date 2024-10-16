# import pytest
#
# @pytest.fixture()
# def set_up():
#     print("Open Browser")
#     yield
#     print("Close Browser")
#
# @pytest.mark.number1
# def test_login():
#     print("login to the account")
#
# @pytest.mark.number2
# def test_search_product():
#     print("Search for a product")
#
# @pytest.mark.skip
# def test_select_product():
#     print("Select the product needed")
#
# @pytest.mark.skipif(True, reason= "check")
# def test_add_item():
#     print("Item added to cart successfully")
#
# @pytest.mark.skipif(False, reason= "check")
# def test_remove_item():
#     print("Item removed successfully")
#
# @pytest.mark.xfail
# def test_add_payment():
#     print("Payment details added successfully")
#
# @pytest.mark.parametrize("a, b, c", [(1, 2, 3) ,(5, 7, 12) ,(10, 1, 15)])
# def test_add(a, b, c):
#     assert a+b == c
#
# @pytest.mark.parametrize("year", ["", 2023, "abc"])
# def test_post_api_with_negative_cases(year):
#     print(year)
#
# def test_logout(set_up):
#     print("Successfully logged out")