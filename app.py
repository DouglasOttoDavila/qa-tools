from flask import Flask

app = Flask(__name__)

from routes.pages import page
from routes.api import api

app.register_blueprint(page)
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    
    
    
