from model import db, connect_to_db, Item, Item_Shipped, Shipment
from datetime import date


def create_item(name, quantity, description=None, image=None):
    """Creates a new item."""

    item = Item(name=name, quantity=quantity,
                description=description, image=image)

    db.session.add(item)
    db.session.commit()

    return item


def create_item_shipped(item_id, shipment_id, quantity):
    """Creates an item in a shipment"""

    item_ship = Item_Shipped(item_id=item_id,
                             shipment_id=shipment_id,
                             quantity=quantity)

    db.session.add(item_ship)
    db.session.commit()

    return item_ship


def get_item_shipped(item_shipped_id):
    return Item_Shipped.query.get(item_shipped_id)


def create_shipment(ship_to="Some happy customer",
                    ship_from="Some warehouse",
                    ship_date=date.today()):

    """Creates a Shipment """
    shipment = Shipment(ship_to=ship_to,
                        ship_from=ship_from,
                        ship_date=ship_date)

    db.session.add(shipment)
    db.session.commit()
    return shipment


# ITEM FUNCTIONS
def get_inventory():
    """Returns a list of all items"""

    return Item.query.all()


def get_item_by_id(item_id):
    return Item.query.get(item_id)


def delete_item(item):
    """Deletes an instance of an item"""
    db.session.delete(item)
    db.session.commit()
    return "deleted"


def change_name(item_id, new_name):
    item = get_item_by_id(item_id)
    item.name = new_name

    db.session.commit()


def change_quantity(item_id, new_quantity):
    """Changes an item's quantity"""
    item = get_item_by_id(item_id)
    item.quantity += new_quantity

    if item.quantity > 0:
        db.session.commit()
        return True
    else:
        return "Not enough items in Inventory"


def change_description(item_id, new_descr):
    item = get_item_by_id(item_id)
    item.description = new_descr

    db.session.commit()


# SHIPMENT FUNCTIONS

def get_shipment_by_id(shipment_id):
    return Shipment.query.get(shipment_id)


def add_item(shipment_id, item_id, quantity):
    shipment = get_shipment_by_id(shipment_id)
    item = get_item_by_id(item_id)
    if item not in shipment.items:
        result = change_quantity(item.item_id, -(quantity))
        if result == True:
            added_item = create_item_shipped(item_id, shipment_id, quantity)

            return added_item
        else:
            return result
    return "Already in shipment! Increase quantity to add more to shipment"


def remove_item(item_shipped_id):
    """Deletes an item from shipment"""
    ship_item = get_item_shipped(item_shipped_id)
    ship_amnt = ship_item.quantity

    change_quantity(ship_item.item_id, ship_amnt)

    db.session.delete(ship_item)
    db.session.commit()







if __name__ == '__main__':
    from server import app
    connect_to_db(app)