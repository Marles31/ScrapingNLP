from flask import render_template

from entities.parsingEntity import parsingEntity


def parsingController(main):
    @main.route('/parsing')
    def parsing():
        return render_template('parsing.html')

    @main.route('/parsing', methods=['POST'])
    def processParsing():
        entity = parsingEntity()
        response = parsingEntity.response(entity)
        return render_template('parsing.html', response=response)