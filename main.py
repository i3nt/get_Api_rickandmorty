from app import create_app

app = create_app()

if __name__ == '__main__': # cuando se ejecute una aplicacion en flask acceda a este flask y aqui habra un app.run que va a dar la funcion para que se ejeucte la app
    app.run(debug=True)
