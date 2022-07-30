from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['Get','Post'])
def index():
    return "Flask running"

if __name__=="__main__":
    app.run(debug=True)
