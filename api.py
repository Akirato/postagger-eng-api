
from flask import Flask,request
from flask.ext.restful import Resource, Api
import nltk

app = Flask(__name__)
api = Api(app)

todos={}
class TodoSimple(Resource):
    def get(self,argument):
        argument = argument.replace('_',' ')
	a = nltk.pos_tag(nltk.word_tokenize(argument))
        return a

    def put(self,argument):
	todos[argument]=request.form['data']
	return {argument : todos[argument]}

api.add_resource(TodoSimple, '/<string:argument>')

if __name__ == '__main__':
    app.run(debug=True)

