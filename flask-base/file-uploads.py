from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/upload",methods=['GET','POST'])
def upload():
    print(request.files)
    img = request.files['img']
    img.save('./static/'+secure_filename(img.filename))
    return secure_filename(img.filename)

if __name__ == '__main__':
    app.run(port=8080,debug=True)
