from flask import Flask

app = Flask(__name__)

from routes.pages import main_page
from modules.user_story_analyzer.routes.pages import rr_page
from modules.user_story_analyzer.routes.api import rr_api

app.register_blueprint(main_page)
app.register_blueprint(rr_page)
app.register_blueprint(rr_api)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    
    
    
