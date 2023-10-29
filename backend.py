from flask import Flask, request;
from flask_cors import CORS, cross_origin
# from pegasus import pegasus;\
from medmini import infer

app = Flask(__name__)
CORS(app)

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
  return infer(request.get_json(force=True)["question"])

if __name__ == '__main__':
  app.run(host='192.168.196.219', port=5000, debug=True)