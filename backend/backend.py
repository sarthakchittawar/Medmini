from flask import Flask, request;
from flask_cors import CORS, cross_origin
# from pegasus import pegasus;\
from model import summarize

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def root():
  if request.method == 'GET':
    return 'Hello, World!'
  return (request.get_json(force=True))

@app.route('/summarize', methods=['POST'])
@cross_origin(supports_credentials=True)
def x():
    # print(request.get_json(force=True)["text"])
    # return request.get_json(force=True)["text"]
  return summarize(request.get_json(force=True)["text"])

if __name__ == '__main__':
  app.run(debug=True)