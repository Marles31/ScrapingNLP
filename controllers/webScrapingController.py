from flask import render_template

from entities.webScrapingEntity import webScrappingEntity

def webScrapingController(main):
    @main.route('/scraping')
    def scraping():
        return render_template('scraping.html')

    @main.route('/scraping', methods=['POST'])
    def processScraping():
        entity = webScrappingEntity()
        classResponse = webScrappingEntity.classResponse(entity)
        return render_template('scraping.html', classResponse=classResponse)
