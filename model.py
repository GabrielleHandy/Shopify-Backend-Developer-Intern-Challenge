from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()



class Item(db.Model):
    """An Item in inventory"""

    __tablename__ = 'items'

    item_id = db.Column(db.Integer, 
                      primary_key=True, 
                      autoincrement=True)
    name = db.Column(db.String(50),
                     nullable = False)
    # In the future images can be applied to items
    image = db.Column(db.String, nullable=True)

    # descriptions of that can be used on websites or for better search
    description = db.Column(db.String(),
                     nullable = True) 

    quantity = db.Column(db.Integer, nullable = False)              
    
    shipments = db.relationship("Shipment",secondary= "items_shipped", back_populates="items") 
    
    def __repr__(self):
        return f"""Item 
        item_id:{self.item_id} 
        name:{self.name} 
        quantity:{self.quantity}"""


class Item_Shipped(db.Model):
    # association table
    """Shipments with more than one item 
    and items being in more than one shipment"""

    __tablename__ = 'items_shipped'

    item_shipped_id = db.Column(db.Integer, 
                      primary_key=True, 
                      autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipments.ship_id'))
    quantity = db.Column(db.Integer, nullable = False)

    
    def __repr__(self):
        return f"""Item_Shipped 
        item_shipped_id: {self.item_shipped_id} 
        item_id:{self.item_id} 
        shipment_id:{self.shipment_id} 
        quantity:{self.quantity}"""


class Shipment(db.Model):
    """A shipment of items"""

    __tablename__ = 'shipments'

    ship_id = db.Column(db.Integer, 
                      primary_key=True, 
                      autoincrement=True)

    # possible future customers' addresses 
    ship_to = db.Column(db.String(50), nullable = True)
    
    # possible future warehouse addresses 
    ship_from = db.Column(db.String(100), nullable = True)
    ship_date = db.Column(db.Date, nullable = True)



    items = db.relationship('Item', secondary= "items_shipped", back_populates="shipments")
   
    def __repr__(self):
        return f"""Shipment 
        shipment_id:{self.ship_id} 
        From:{self.ship_from}
        To: {self.ship_to}
        Shipment date: {self.ship_date}"""



def connect_to_db(flask_app, db_uri="postgresql:///inventory", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)