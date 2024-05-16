from flask import render_template

from entities.classificationEntity import classificationEntity


def classificationController(main):
    @main.route('/classification')
    def classify():
        return render_template('classification.html')

    @main.route('/classification', methods=['POST'])
    def processClassification():
        entity = classificationEntity()
        response = classificationEntity.response(entity)
        return render_template('classification.html', response=response)