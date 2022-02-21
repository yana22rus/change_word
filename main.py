import os.path
import uuid
from flask import Flask,request,render_template


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("file","uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1042 * 1042
ALLOWED_EXTENSIONS = {"txt","md"}


@app.route('/upload',methods=["GET","POST"])
def upload_file():

    if request.method == "POST":
        file = request.files["file"]

        file.filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1].lower()}'
        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        path = f"{os.getcwd()}/static/{UPLOAD_FOLDER}/{file.filename}"

        print(path)

        with open(path) as f:

            f = " ".join(f.readlines()).split()

        print(f)


        return "123"

    return render_template("uploads.html")



if __name__ == "__main__":
    app.run(debug=True)