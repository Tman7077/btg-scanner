from swapp import create_app, cred

app = create_app()

with app.app_context():
    cred.create_all()

if __name__ == '__main__':
    app.run(debug=True)