import os
from .enviroment import Enviroment

Enviroment(os.getenv('ENV'))
