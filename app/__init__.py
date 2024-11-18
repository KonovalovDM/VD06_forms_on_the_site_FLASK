from flask import Flask

# создаем экземпляр класса Flask (переменную app)
app = Flask(__name__)

# создаем секретный ключ
app.config['SECCRET_KEY'] = "your_secret_key"

# импортируем маршруты
from app import routes