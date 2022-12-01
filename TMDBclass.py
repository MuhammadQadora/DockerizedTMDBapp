import json
import requests
from Secrets import api
import imdb
from MongoApi import MongoAPI
import base64

class tmdbDownload:
    def __init__(self):
        self.CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
        self.KEY = api
        self.url = self.CONFIG_PATTERN.format(key=self.KEY)
        self.r = requests.get(self.url)
        self.config = self.r.json()
        self.base_url = self.config['images']['base_url']
        self.max_size = 'original'
        self.name = ''
        self.mvid = ''
        self.filename= ''

    def setName(self,name):
        self.name=name
    
    def getMovieId(self):
        ia = imdb.IMDb()
        ia = ia.search_movie_advanced(self.name)
        self.mvid = "tt" + str(ia[0].movieID)
        return self.mvid

    def downloadPoster(self):
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
        r = requests.get(IMG_PATTERN.format(key=self.KEY,imdbid=self.mvid))
        api_response = r.json()
        posters = api_response['posters']
        poster_urls = []
        for poster in posters:
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(self.base_url, self.max_size, rel_path)
            poster_urls.append(url)
        r = requests.get(poster_urls[0])
        filetype = r.headers['content-type'].split('/')[-1]
        self.filename = 'poster_{0}.{1}'.format(self.name, filetype)
        ob = MongoAPI()
        ob.uploadImage(r.content,self.filename)

    def ReturnToHtml(self):
        obj = MongoAPI()
        conv = obj.downloadImage(self.filename)
        img = base64.b64encode(conv).decode('utf-8')
        return img
        



def downloadAndUpload(name):
    obj = tmdbDownload()
    obj.setName(name)
    obj.getMovieId()
    obj.downloadPoster()

def downloadAndDisplay(name):
    obj = tmdbDownload()
    obj.setName(name)
    obj.getMovieId()
    obj.downloadPoster()
    return obj.ReturnToHtml()