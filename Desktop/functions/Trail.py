from flask import Flask,request
from linear import model
app = Flask(__name__)

@app.route('/',methods=["Post"])
def api_lin():
    if request.header['Conten-Type']=='text/plain':
        return model(request.data)
    else:
        return"wrong content type or wrong data type"

if __name__=="__main__":
    app.run(debug=True)
