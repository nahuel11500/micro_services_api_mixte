from contextlib import nullcontext
import json

def get_all_movies(self,info):
     res = []
     with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            movie['actors'] = resolve_actors_in_movie(movie,nullcontext)
            res.append(movie)
     return res

def movie_with_id(_,info,_id):
    with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie
            
def actor_with_id(_,info,_id):
    with open('movie/data/actors.json'.format("."), "r") as file:
        actors = json.load(file)
        for actor in actors['actors']:
            if actor['id'] == _id:
                return actor
            
def update_movie_rate(_,info,_id,_rate):
    newmovies = {}
    newmovie = {}
    with open('movie/data/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
    with open('movie/data/movies.json'.format("."), "w") as wfile:
        json.dump(newmovies, wfile)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open('movie/data/actors.json'.format("."), "r") as file:
        data = json.load(file)
        actors = [actor for actor in data['actors'] if movie['id'] in actor['films']]
        return actors

def delete_movie(_,info,_id):
    with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movies.remove(movie)
                return 'Movie Deleted Successfully'
    return 'Movie Not Found'

def create_movie(_,info,_id,_title,_director,_rating,_actors):
    with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return 'Movie Already exist'
        newMovie = {"title": _title, "rating": _rating, "director": _director, "id": _id}  
        movies['movies'].append(newMovie)
        with open('movie/data/actors.json'.format("."), "r") as file2:
         actors = json.load(file2)
         for actor in actors["actors"]:
             if actor['id'] in _actors:
                 actor['films'].append(_id)
        return "Movie Created Successfully"
 
def best_rated_movie(_,info):
     with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        best =  movies['movies'][0]
        for movie in movies['movies']:
            if movie["rating"] > best["rating"]:
                best = movie
        return best
     
def worst_rated_movie(_,info):
     with open('movie/data/movies.json'.format("."), "r") as file:
        movies = json.load(file)
        worst =  movies['movies'][0]
        for movie in movies['movies']:
            if movie["rating"] < worst["rating"]:
                worst = movie
        return worst
     
def best_rated_movie_of_actor(_,info,_id):
    actor = actor_with_id(nullcontext,nullcontext,_id)
    best = movie_with_id(nullcontext,nullcontext,actor['films'][0])
    for movie in actor['films']:
        if movie_with_id(nullcontext,nullcontext,movie)['rating'] > best['rating']:
            best = movie_with_id(nullcontext,nullcontext,movie)
    return best

def worst_rated_movie_of_actor(_,info,_id):
    actor = actor_with_id(nullcontext,nullcontext,_id)
    worst = movie_with_id(nullcontext,nullcontext,actor['films'][0])
    for movie in actor['films']:
        if movie_with_id(nullcontext,nullcontext,movie)['rating'] < worst['rating']:
            worst = movie_with_id(nullcontext,nullcontext,movie)
    return worst

def youngest_actor_in_movie(_,info,_id):
    actors = resolve_actors_in_movie(movie_with_id(nullcontext,nullcontext,_id),nullcontext,)
    youngest = actors[0]
    for actor in actors :
        if actor['birthyear'] > youngest['birthyear']:
            youngest = actor
    return youngest

def oldest_actor_in_movie(_,info,_id):
    actors = resolve_actors_in_movie(movie_with_id(nullcontext,nullcontext,_id),nullcontext,)
    oldest = actors[0]
    for actor in actors :
        if actor['birthyear'] < oldest['birthyear']:
            oldest = actor
    return oldest

def colaboration_of_actors(_,info,_id1,_id2):
   actor1 = actor_with_id(nullcontext,nullcontext,_id1)
   actor2 = actor_with_id(nullcontext,nullcontext,_id2)
   return [movie_with_id(nullcontext,nullcontext,value) for value in actor1['films'] if value in actor2['films']]
