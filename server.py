import crud
from datetime import date
from flask import (Flask, render_template, request, 
                   redirect, session, flash, jsonify,
                   Markup)
from model import connect_to_db
import os

app = Flask(__name__)




@app.route("/")
def inventory_shipment():
    """Shows inventory and Shipments"""

    inventory = crud.get_inventory()
    shipments = crud.get_shipments()
    ship_qty = crud.get_quantity_ship_item(shipments)

    return render_template("index.html", inventory =inventory, 
                            shipments=shipments, ship_qty = ship_qty)
                            

# Inventory routes
@app.route("/addItemInventory", methods=['POST'])
def add_item():
    name = request.form.get('name')
    description = request.form.get('description')
    quantity = request.form.get('quantity')

    if len(description) == 0:
        description = None

    item = crud.create_item(name, quantity, description)

    flash(Markup(f"""<div class="alert alert-success d-flex align-items-center" role="alert">
            <div>
                {item.name} was successfuly created!!
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>"""))
    return redirect("/")


@app.route("/deleteitem", methods=['POST'])
def remove_item():
    item_id = request.json.get("item_id")

    crud.delete_item(item_id)
    return jsonify("deleted")


@app.route("/edit_inventory", methods=['POST'])
def edit_item():
    name = request.form.get('new_name')
    qty = request.form.get('new_qty')
    desc = request.form.get('new_desc')
    item_id = request.form.get('id')

    if name:
        crud.change_name(item_id, name)
    if qty:
        crud.change_quantity_from_form(item_id, int(qty))

    if desc:
        crud.change_description(item_id, desc)

    return redirect('/')




# Shipment routes

@app.route("/createshipment", methods=['POST'])
def create_shipment():
    ship_to = request.form.get('ship_to')
    ship_from = request.form.get('ship_from')
    ship_date = request.form.get('ship_date')

    if len(ship_date) == 0:
        ship_date = date.today()

    ship = crud.create_shipment(ship_to= ship_to,
                                ship_from= ship_from,
                                ship_date= ship_date)

    flash(Markup(f"""<div class="alert alert-success d-flex align-items-center" role="alert">
            <div>
                Shipment {ship.ship_id} was successfuly created!!
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>"""))
    return redirect("/")



@app.route("/delete_ship", methods=['POST'])
def delete_shipments():

    ship_id = request.json.get('ship_id')

    crud.delete_shipment(ship_id)

    return jsonify("deleted")


@app.route("/addtoship", methods=['POST'])
def add_item_shipment():

    item_id = request.form.get('item_id')
    ship_id = request.form.get('ship_id')
    qty = request.form.get('qty')

    item = crud.get_item_by_id(item_id)
    if item:
        if item.quantity < int(qty):
            flash(Markup(f"""<div class="alert alert-warning d-flex align-items-center" role="alert">
            <div>
                {item.name} doesnt have {qty} in inventory!
                Inventory Status:
                {item.name}--{item.quantity}
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>"""))
        else:
            result = crud.add_item(ship_id, item_id, int(qty))

            if result == True:
                flash(Markup(f"""<div class="alert alert-success d-flex align-items-center" role="alert">
                <div>
                    {item.name} was successfully added to shipment!
                    Updated Inventory Status:
                    {item.name}--{item.quantity}
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>"""))
            else:
                flash(Markup(f"""<div class="alert alert-warning d-flex align-items-center" role="alert">
                <div>
                    {result}
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>"""))
    else:
        flash(Markup("""<div class="alert alert-warning d-flex align-items-center" role="alert">
            <div>
                The item you're trying to add doesn't exist!
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>"""))

    return redirect('/')

@app.route('/delete_item_ship', methods=['POST'])
def delete_item_from_shipment():
    item_id = request.json.get('item_id')
    ship_id = request.json.get('ship_id')

    crud.remove_item(ship_id, item_id)

    return jsonify("deleted")


if __name__ == '__main__':
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host='127.0.0.1', port=5002)