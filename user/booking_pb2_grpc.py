# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import booking_pb2 as booking__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBookings = channel.unary_stream(
                '/Booking/GetBookings',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=booking__pb2.BookingUser.FromString,
                )
        self.getBookingByUserId = channel.unary_unary(
                '/Booking/getBookingByUserId',
                request_serializer=booking__pb2.userid.SerializeToString,
                response_deserializer=booking__pb2.BookingUser.FromString,
                )
        self.AddNewMovieBooking = channel.unary_unary(
                '/Booking/AddNewMovieBooking',
                request_serializer=booking__pb2.BookingRequest.SerializeToString,
                response_deserializer=booking__pb2.SuccessMessage.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBookingByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddNewMovieBooking(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetBookings,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=booking__pb2.BookingUser.SerializeToString,
            ),
            'getBookingByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.getBookingByUserId,
                    request_deserializer=booking__pb2.userid.FromString,
                    response_serializer=booking__pb2.BookingUser.SerializeToString,
            ),
            'AddNewMovieBooking': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNewMovieBooking,
                    request_deserializer=booking__pb2.BookingRequest.FromString,
                    response_serializer=booking__pb2.SuccessMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetBookings',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            booking__pb2.BookingUser.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBookingByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/getBookingByUserId',
            booking__pb2.userid.SerializeToString,
            booking__pb2.BookingUser.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddNewMovieBooking(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/AddNewMovieBooking',
            booking__pb2.BookingRequest.SerializeToString,
            booking__pb2.SuccessMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
