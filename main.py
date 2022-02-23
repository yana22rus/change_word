import os.path
from random import sample
import uuid
from flask import Flask,request,render_template


app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("file","uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1042 * 1042
ALLOWED_EXTENSIONS = {"txt","md"}


@app.route('/upload',methods=["GET","POST"])
def upload_file():

    lst = []

    if request.method == "POST":

        file = request.files["file"]

        file.filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1].lower()}'
        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        path = f"{os.getcwd()}/static/{UPLOAD_FOLDER}/{file.filename}"


        with open(path) as f:

            f = " ".join(f.readlines()).split()


        for x in f:

            if len(x) > 3:

                first_char = x[0]

                last_char = x[-1]

                slice_word = x[1:len(x) - 1]

                r = "".join(sample(list(slice_word), len(slice_word)))

                lst.append(f"{first_char}{r}{last_char}")
            else:

                lst.append(x)

        return " ".join(lst)

    return render_template("uploads.html")



if __name__ == "__main__":
    app.run(debug=True)