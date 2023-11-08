from flask import Flask, request;
from flask_cors import CORS, cross_origin
from medmini import infer,systemInit

app = Flask(__name__)
CORS(app)
summarizer=None
vectordb=None

@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def root():
  if request.method == 'GET':
    return 'Hello, World!'
  return (request.get_json(force=True))

@app.route('/query', methods=['POST'])
@cross_origin(supports_credentials=True)
def x():
  # print(request.get_json(force=True)["question"])
    # return request.get_json(force=True)["text"]
  global summarizer
  global vectordb
  return infer(request.get_json(force=True)["question"],summarizer,vectordb)

if __name__ == '__main__':
  summarizer,vectordb=systemInit()
  app.run(host="0.0.0.0",port=5000,debug=True)