from flask import Flask, render_template

from controllers.classificationController import classificationController
from controllers.homeWebScrappingController import homeWebScrapingController
from controllers.parsingController import parsingController
from controllers.webScrapingController import webScrapingController

app = Flask(__name__)

homeWebScrapingController(app)
webScrapingController(app)
parsingController(app)
classificationController(app)

@app.route('/')
def index():
    return render_template('Menu.html')


if __name__ == '__main__':
    app.run()
