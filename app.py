from flask import Flask, request, render_template , jsonify , redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import random, string
import os

# Lê a URL do MongoDB da variável de ambiente, com um valor padrão caso não exista
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://admin:secret@localhost:27017/url_shortener?authSource=admin&authMechanism=SCRAM-SHA-1')

app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

def randomId():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(8))

def generateShortUrl(url_original , url_local):
    idUrl = randomId()
    urlFormat = url_local + f"{idUrl}"

    # temp = url_original.split("/")
    # host = "/".join(temp[0:3])
    # path_name = "/".join(temp[4:])

    return idUrl,urlFormat

def detailsPage():
    details = {
        "method": request.method,
        "url": request.url, 
        "base_url": request.base_url, 
        "path": request.path, 
        "args": request.args.to_dict(), 
        "host": request.host_url
    }
    return details

def alreadyExistsInDb(originalURL):
    qtd_elements_in_mongo = mongo.db.urls.count_documents({'original_url': originalURL})
    return qtd_elements_in_mongo > 0
    
def getURLinDb(originalURL):
    data = mongo.db.urls.find_one({'original_url': originalURL})
    if data:
        return data['short_url'], data['idURL']
    return None, None

def saveUrl(idURL , originalURL , shortenURL , mongo):
    # Inserting the urls in the doc "urls" (if not exist , then the Mongo will create) and inserting
    mongo.db.urls.insert_one({
            'original_url': originalURL,
            'short_url': shortenURL,
            'idURL':idURL
    })


@app.route("/" , methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shorten" , methods=["POST"])
def shorten():
    # Get the url that will be shortened
    originalURL = request.get_json().get("url")

    # Get the url of the sys
    LocalUrl = detailsPage()["host"]

    # Verify if the url already exists:
    if(alreadyExistsInDb(originalURL) == True):
        shortUrl , idUrl = getURLinDb(originalURL)
    else:
        idUrl , shortUrl = generateShortUrl(originalURL , LocalUrl)
        
        # Saving the urls in the MongoDB
        mongo.db.urls.insert_one({
            'original_url': originalURL,
            'short_url': shortUrl,
            'idURL': idUrl
        })

    return jsonify({"status": 200 , "idUrl":idUrl , "shortUrl":shortUrl})

@app.route('/<short_url>')
def redirect_to_url(short_url):
    # Consultando a URL original no MongoDB
    mapping = mongo.db.urls.find_one({'idURL': short_url})
    if mapping:
        return redirect(mapping['original_url'])
    return "URL não encontrada.", 404


if __name__ == '__main__':
    app.run(debug=True)