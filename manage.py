from server_app import creat_app
from register_bp import register

app = creat_app()
app=register(app)

if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)