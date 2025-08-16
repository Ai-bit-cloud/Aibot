from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Training data
X = ["hello", "how are you", "what's your name"]
y = ["Hi!", "I'm good, thanks!", "I'm your chatbot."]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    user_msg = request.json["message"]
    input_vec = vectorizer.transform([user_msg])
    response = model.predict(input_vec)[0]
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
