from main import Item

def test_item_init():
    item1 = Item('Телевизор', 50000, 2)
    assert item1.name == 'Телевизор'
    assert item1.price == 50000
    assert item1.quantity == 2

def test_item_calculate_total_price():
    item1 = Item('Телевизор', 50000, 2)
    check_total_price = item1.price * item1.quantity
    assert check_total_price == 100000

def test_item_apply_discount():
    item1 = Item('Телевизор', 50000, 2)
    check_price = item1.price * item1.discount
    assert check_price == 40000