import json

import requests


def test_service_user():
    url = "http://172.16.134.102:3203/"
    print("Request is :")
    print("GET http://172.16.134.102:3203/")
    print("Response is :")
    response = requests.get(url)
    print(response.content)
    print()
    input("Push on Enter to make the following request : See all Users")

    url = "http://172.16.134.102:3203/users"
    print("Request is :")
    print("GET " + url)
    print("Response is :")
    response = requests.get(url)
    print(json.loads(response.content))
    print()
    input("Push on Enter to make the following request : Get the information about the user Chris Rivers")

    url = "http://172.16.134.102:3203/users/chris_rivers"
    print("Request is :")
    print("GET " + url)
    print("Response is :")
    response = requests.get(url)
    print(json.loads(response.content))
    print()
    input("Push on Enter to make the following request : See all movies")

    ## Fait appel au service movie
    url = "http://172.16.134.102:3203/movies"
    print("Request is :")
    print("GET " + url)
    print("Response is :")
    response = requests.get(url)
    print(json.loads(response.content))
    print()
    input("Push on Enter to make the following request : See the booking of Chris Rivers")

    ## Fait appel au service booking
    url = "http://172.16.134.102:3203/bookings/chris_rivers"
    print("Request is :")
    print("GET " + url)
    print("Response is :")
    response = requests.get(url)
    print(json.loads(response.content))
    print()
    input("Push on Enter to make the following request : Add an already existing user")

    ## Fait appel à une méthode post
    url = "http://172.16.134.102:3203/users/chris_rivers"
    query = """
{
    "id": "chris_rivers",
    "last_active": 1360031010,
    "name": "Chris Rivers"
}
    """
    print("Request is :")
    print("GET " + url)
    print("Body is :")
    print(query)
    print("Response is :")
    response = requests.post(url, json={'query': query})
    print(response.json())
    print()
    input("Push on Enter to make the following request : Add an new user")

    url = "http://172.16.134.102:3203/users/test"
    query = """
    {
        "id": "test",
        "last_active": 1360031010,
        "name": "test"
    }
        """
    print("Request is :")
    print("GET " + url)
    print("Body is :")
    print(query)
    print("Response is :")
    response = requests.post(url, json={'query': query})
    print(response.json())

def test_service_movie():
    query = """
query Get_all_movies{   
    get_all_movies {
        id
        title
        director
        rating
    }
}
"""
    response = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
    print(response.json())


def test_service_booking():
    print("test_service_booking Not Implementend")

def test_service_times():
    print("test_service_times Not Implementend")

if __name__ == "__main__":
    input("Appuyer sur Enter pour lancer le test du service user")
    test_service_user()
    print()
    input("Appuyer sur Enter pour lancer le test du service movie")
    test_service_movie()
    test_service_booking()
    test_service_times()

