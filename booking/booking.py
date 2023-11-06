import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json
import showtime_pb2
import showtime_pb2_grpc
import os

class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingUser(userid=booking['userid'], dates=booking['dates'])

    def getBookingByUserId(self, request, context):
        for booking in self.db:
            if booking["userid"] == request.userid:
                return booking_pb2.BookingUser(userid=booking['userid'], dates=booking['dates'])
        return booking_pb2.BookingUser(userid='', dates='')

    def AddNewMovieBooking(self, request, context):
        datee = request.date
        movieId= request.movieid
        userId = request.userid

        # Make a request to see if the date is available for the movie
        with grpc.insecure_channel('localhost:4001') as channel:
            stub = showtime_pb2_grpc.ShowtimeStub(channel)
            showtime_pb2.Movie_Date()
            movie_date = showtime_pb2.Movie_Date(date=str(datee))
            schedule = stub.getMovieByDate(movie_date)
        channel.close()

        ## Iterate throught all the movies avalaible at the date requested to see if the movie
        ## requested is here.
        for movie in schedule.movie:
            if movie == movieId:
                ## Add the reservation for the user
                for user_booking in self.db:
                    if user_booking['userid'] == userId:
                        for d in user_booking['dates']:
                            if d['date'] == datee:
                                d['movies'].append(movieId)
                        # Add new date if not exists
                        user_booking['dates'].append({
                            "date": datee,
                            "movies": [movieId]
                        })
                return booking_pb2.SuccessMessage(message = "Booking Successful")
        return booking_pb2.SuccessMessage(message="Booking Unsuccessful")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:4000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
