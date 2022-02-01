from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from project.server import app, db, models
from project.server.models import User
import unittest
import coverage
import os
from sqlalchemy.exc import IntegrityError

# Initializing the manager
manager = Manager(app)

# Initialize Flask Migrate
migrate = Migrate(app, db)

# Add the flask migrate
manager.add_command('db', MigrateCommand)

print("manage.py initialized!!!!")

# Run the manager
if __name__ == '__main__':
    manager.run()
    print("manager RAN")
