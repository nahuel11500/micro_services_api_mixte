from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
from werkzeug.exceptions import NotFound
import booking_pb2_grpc
import booking_pb2
import grpc
from google.protobuf import json_format
app = Flask(__name__)

PORT = 3203
HOST = '0.0.0.0'

with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

@app.route("/users", methods=['GET'])
def get_json():
   return make_response(jsonify({"users": users}), 200)

@app.route("/users/<userid>", methods=['GET'])
def get_user_byid(userid):
    for user in users:
        if str(user["id"]) == str(userid):
            return make_response(jsonify(user),200)
    return make_response(jsonify({"error":"User ID not found"}),400)

@app.route("/bookings/<userid>", methods=['GET'])
def get_booking_for_user(userid):
   with grpc.insecure_channel('localhost:3004') as channel:
      stub = booking_pb2_grpc.BookingStub(channel)
      booking_pb2.userid()
      movie_date = booking_pb2.userid(userid=str(userid))
      bookings = stub.getBookingByUserId(movie_date)
   channel.close()
   return make_response(json_format.MessageToJson(bookings), 200)

@app.route("/movies", methods=['GET'])
def get_movies():
   query = """
query Get_all_movies{   
   get_all_movies{
      movies {
        id
        title
        director
        rating
        }
      }
    }
"""
   response = requests.post("http://127.0.0.1:3001/graphql",json={'query': query})
   return make_response(response.json(), response.status_code)

@app.route("/users/<userid>", methods=['POST'])
def add_user(userid):
   ## A Modifier
   req = request.get_json()
   for user in users:
      if str(user["id"]) == str(userid):
            return make_response(jsonify({"error":"User already exists"}),409)
   users.append(req)
   res = make_response(jsonify(req),200)
   return res

@app.route("/bookings/<userid>", methods=['POST'])
def add_booking_byuser(userid):
   ## A Modifier
   req = request.get_json()
   response = requests.post(f"http://{HOST}:3201/bookings/{userid}",json=req)
   return make_response(response.json(), response.status_code)

@app.route("/movies", methods=['GET'])
def get_movies():
    query = """
query Get_all_movies {
    get_all_movies {
        id
        title
        director
        rating
    }
}
    """
    response = requests.post("http://localhost:3001/graphql", json={'query':  query})
    return make_response(response.json(), response.status_code)

@app.route("/users/<userid>", methods=['POST'])
def add_user(userid):
   req = request.get_json()
   for user in users:
      if str(user["id"]) == str(userid):
            return make_response(jsonify({"error":"User already exists"}),409)
   users.append(req)
   res = make_response(jsonify(req),200)
   return res

@app.route("/bookings/<userid>", methods=['POST'])
def add_booking_byuser(userid):
   req = request.get_json()
   response = requests.post(f"http://{HOST}:3201/bookings/{userid}",json=req)
   return make_response(response.json(), response.status_code)


@app.route("/best_rated_movie", methods=['GET'])
def best_rated_movie():
   query = """
query Best_Rated_Movie {
    best_rated_movie {
        id
        title
        director
        rating
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)

@app.route("/worst_rated_movie", methods=['GET'])
def worst_rated_movie():
   query = """
query Worst_Rated_Movie {
    worst_rated_movie {
        id
        title
        director
        rating
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)  

@app.route("/best_rated_movie_of_actor/<actor_id>", methods=['GET'])
def best_rated_movie_of_actor(actor_id):
   query = """
query Best_rated_movie {
    best_rated_movie_of_actor(_id:"""+ str(actor_id)+""") {
        id
        title
        director
        rating
    }
}

"""
   response = requests.post("http://localhost:3001/graphql", json={"query" : query})
   return make_response(response.json(), response.status_code)  


@app.route("/worst_rated_movie_of_actor/<actor_id>", methods=['GET'])
def worst_rated_movie_of_actor(actor_id):
   query = """
query Worst_rated_movie {
    worst_rated_movie_of_actor(_id:"""+ str(actor_id)+""") {
        id
        title
        director
        rating
    }
}

"""
   response = requests.post("http://localhost:3001/graphql", json={"query" : query})
   return make_response(response.json(), response.status_code)  

@app.route("/youngest_actor_in_movie/<movie_id>", methods=['GET'])
def youngest_actor_in_movie(movie_id):
   query = """
query Youngest_actor_in_movie {
    youngest_actor_in_movie(_id:"""+movie_id+""") {
        id
        firstname
        lastname
        birthyear
        films
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)  

@app.route("/oldest_actor_in_movie/<movie_id>", methods=['GET'])
def oldest_actor_in_movie(movie_id):
   query = """
query Oldest_actor_in_movie {
    oldest_actor_in_movie(_id:"""+movie_id+""") {
        id
        firstname
        lastname
        birthyear
        films
    }
}
    """
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)  

@app.route("/colaboration_of_actors/<id_actors>", methods=['GET'])
def colaboration_of_actors(id_actors):
   id_actor1 = id_actors.split('-')[0]
   id_actor2 = id_actors.split('-')[1]
   print(type(id_actor1))
   query = """
query Colaboration_of_actors {
    colaboration_of_actors(_id1: """+id_actor1+""" , _id2: """+id_actor2+""") {
        id
        title
        director
        rating
    }
}

    """
   print(id_actor1)
   print(id_actor2)
   print(query)
   response = requests.post("http://localhost:3001/graphql", json={'query':  query})
   return make_response(response.json(), response.status_code)  

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT, debug=True)
