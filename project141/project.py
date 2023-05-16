from flask import Flask, jsonify, request
import csv
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations
all_articles = []

with open("articles.csv",encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route('/')
def get_articles():
   return jsonify({all_articles[0]}) 

@app.route("/get-article")
def get_article():
    movie_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("popular_article")
def popular_article():
    article_data = []
    for i in output:
      movie_data = {
        "url": i[0],
        "title": i[1],
        "text": i[2],
        "lang": i[3],
        "total_events": i[4]
      }
      article_data.append(movie_data)
       
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("recommended_article")
def recommend_article():
   recommended_article_data = []
   for i in output:
    movie_data = {
        "url": i[0],
        "title": i[1],
        "text": i[2],
        "lang": i[3],
        "total_events": i[4]
      }
    recommended_article_data.append(movie_data)
       
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route('/liked_articles',methods = ['POST'])
def post_articles():
  article = all_articles[0]
  liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({"status":"success"}),201

@app.route('/not_liked_articles',methods = ['POST'])
def post__articles():
  article = all_articles[0]
  not_liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
        "status": "success"
    }), 201
  
if __name__ == "__main__":
    app.run(debug=True)
