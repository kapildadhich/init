from sanic import Sanic
from sanic.log import logger
from app.routes.identity import identity
from .constants.config import CONFIG 
from app.exceptions.base import handle_exception
from tortoise import Tortoise

db_config = CONFIG.config["DB_CONFIG"]

app = Sanic("app")
app.blueprint(identity)
app.error_handler.add(Exception, handle_exception)

@app.before_server_start
async def init_db(app, loop):
    await Tortoise.init(
        db_url= f'postgres://{db_config["USER"]}:{db_config["PASSWORD"]}@{db_config["HOST"]}:{db_config["PORT"]}/{db_config["NAME"]}',
        modules={'models':["app.models"]}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, dev=True)