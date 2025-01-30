
from flask import Flask, render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open("popular.pkl", "rb"))
app = Flask(__name__)
pt = pickle.load(open("pt.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))
similarity_score = pickle.load(open("smliarity_score.pkl","rb"))

@app.route('/')
def index():
    return render_template(
        "index.html",
        name=list(popular_df["Book-Title"].values),
        aurthor=list(popular_df["Book-Author"].values),
        votes=list(popular_df["num_rating"].values),  # Fixed
        ratings=list(popular_df["avg_rating"].values),  # Fixed
        publish=list(popular_df["Year-Of-Publication"].values) , # Fixed
    img = list(popular_df["Image-URL-M"].values)  # Fixed

    )
@app.route('/rec')
def rec():
    return render_template("rec.html")

@app.route('/recb',methods=["GET"])
def recb():
    name = request.args.get("name")
    try:
        index = np.where(pt.index == name)[0][0]
    except IndexError:
        return render_template("rec.html", error="Book not found. Please try another title.")

    # index = np.where(pt.index == name)[0][0]
    similiar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similiar_items:
        item = []
        temp_df = books[books["Book-Title"] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-M"].values))
        item.extend(list(temp_df.drop_duplicates("Book-Title")["Year-Of-Publication"].values))

        data.append(item)

    print(data)

    return render_template("rec.html",data=data)




if __name__ == "__main__":
    app.run(debug=True)
