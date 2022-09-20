"""
Module to interact with the database.
"""

from sqlalchemy import create_engine, MetaData, Table, select, func

from . import placeholders
from . import db_ops


engine = create_engine("sqlite:///trains.db")

meta = MetaData(bind=engine)

train_table = Table("train", meta, autoload=True)

t = train_table

station_table = Table("station", meta, autoload=True)

s = station_table

db_ops.ensure_db()


def search_stations(q):
    """Returns the top ten stations matching the given query string.

    This is used to get show the auto complete on the home page.

    The q is the few characters of the station name or
    code entered by the user.
    """
    # TODO: make a db query to get the matching stations
    # and replace the following dummy implementation
    return placeholders.AUTOCOMPLETE_STATIONS


def search_trains(
        from_station_code,
        to_station_code,
        ticket_class=None,
        departure_date=None,
        departure_time=[],
        arrival_time=[]):
    """Returns all the trains that source to destination stations on
    the given date. When ticket_class is provided, this should return
    only the trains that have that ticket class.

    This is used to get show the trains on the search results page.
    """
    # TODO: make a db query to get the matching trains
    # and replace the following dummy implementation

    q = (
        select(t.c.number, t.c.name, t.c.from_station_code, t.c.from_station_name, t.c.to_station_code, t.c.to_station_name, t.c.departure, t.c.arrival, t.c.duration_h, t.c.duration_m).
        where(t.c.from_station_code == from_station_code,
              t.c.to_station_code == to_station_code)
    )
    print(q)

    results = q.execute().all()
    print(results)
    return results
    # return placeholders.SEARCH_TRAINS


def get_schedule(train_number):
    """Returns the schedule of a train.
    """
    return placeholders.SCHEDULE


def book_ticket(train_number, ticket_class, departure_date, passenger_name, passenger_email):
    """Book a ticket for passenger
    """
    # TODO: make a db query and insert a new booking
    # into the booking table

    return placeholders.TRIPS[0]


def get_trips(email):
    """Returns the bookings made by the user
    """
    # TODO: make a db query and get the bookings
    # made by user with `email`

    return placeholders.TRIPS
