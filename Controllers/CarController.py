from main import app

class CarController:


    def __init__(self):
        pass

    @app.get("/")
    async def hello(self) ->str:
        return "hello world"
