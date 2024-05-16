from flask import render_template

from entities.webScrapingEntity import webScrappingEntity


def homeWebScrapingController(main):
    @main.route('/homescraping')
    def homeScraping():
        return render_template('scraping.html')

    @main.route('/homescraping', methods=['POST'])
    def processHomeScraping():
        entity = webScrappingEntity()
        homeResponse = webScrappingEntity.HomeResponse(entity)
        return render_template('scraping.html', homeResponse=homeResponse)