import os
from .enviroment import Enviroment

Enviroment(os.getenv('APP_ENV'))
