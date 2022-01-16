import os
from datetime import datetime
import crud, model, server

os.system('dropdb inventory')
os.system('createdb inventory')

model.connect_to_db(server.app)
model.db.create_all()

# Create some items in inventory

groovy = crud.create_item('Groovy Pants', 50, "Blue and Orange bell bottoms")
glasses = crud.create_item("Galactic Glasses", 25, "Star shaped glasses")
wicker = crud.create_item("Wicked Wicker Basket", 40)




ship1 = crud.create_shipment(ship_to = "Jessica Broadway, Sunny California", ship_from = "Warehouse 18")
crud.add_item(ship1.ship_id, wicker.item_id, 10)
crud.add_item(ship1.ship_id, glasses.item_id, 2)

ship2 = crud.create_shipment(ship_date = datetime(2020, 5, 15))
crud.add_item(ship2.ship_id, wicker.item_id, 4)
crud.add_item(ship2.ship_id, glasses.item_id, 2)
crud.add_item(ship2.ship_id, groovy.item_id, 5)

ship4 = crud.create_shipment(ship_date = datetime(2022, 1, 8))

