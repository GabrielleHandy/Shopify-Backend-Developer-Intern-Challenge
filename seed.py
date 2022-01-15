import os
from datetime import datetime
import crud, model, server

os.system('dropdb inventory')
os.system('createdb inventory')

model.connect_to_db(server.app)
model.db.create_all()

# Create some items in inventory


