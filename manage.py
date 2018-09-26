from server_app import creat_app
from register_bp import register
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from server_app import db
from server_app.model.User_M import User,LocalUser


app = creat_app()
app=register(app)

manager=Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()