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

# helper function for search_trains
# # functionality is takes a time string converts it to int value for easier checkng of slot values / range


def helper_time(inp_time):
    inp_time_list = inp_time.split(':')[:2]
    inp_time_str = ''.join(inp_time_list)
    inp_tme_int = int(inp_time_str)
    return inp_tme_int


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
    print(
        f"The searched ticket_class {ticket_class} and the depart list is {departure_time} and the arrival list is {arrival_time}")

    # This helps to map input ticket_class with class type inside DB

    dict_get_class = {
        'SL': t.c.sleeper,
        '3A': t.c.third_ac,
        '2A': t.c.second_ac,
        '1A': t.c.first_ac,
        'FC': t.c.first_class,
        'CC': t.c.chair_car
    }

    # This helps to map input depart_list and arrival_list

    dict_get_slot_range = {
        'slot1': [0, 800],
        'slot2': [801, 1200],
        'slot3': [1201, 1600],
        'slot4': [1601, 2000],
        'slot5': [2001, 2359]
    }

    query = ''

    if ticket_class != None:
        attr_name = dict_get_class[ticket_class]
        query = (
            select(t.c.number, t.c.name, t.c.from_station_code, t.c.from_station_name, t.c.to_station_code, t.c.to_station_name, t.c.departure, t.c.arrival, t.c.duration_h, t.c.duration_m).
            where(t.c.from_station_code == from_station_code,
                  t.c.to_station_code == to_station_code,
                  attr_name > 0
                  )
        )

    else:  # only gets triggered for task 2
        query = (
            select(t.c.number, t.c.name, t.c.from_station_code, t.c.from_station_name, t.c.to_station_code, t.c.to_station_name, t.c.departure, t.c.arrival, t.c.duration_h, t.c.duration_m).
            where(t.c.from_station_code == from_station_code,
                  t.c.to_station_code == to_station_code)
        )

    results = query.execute().all()

    mod_results = []

    if len(departure_time) > 0:

        for dep_time in departure_time:

            time_range = dict_get_slot_range[dep_time]

            for res in results:

                curr_dep_time = helper_time(res.departure)
                if time_range[0] <= curr_dep_time and curr_dep_time <= time_range[1]:
                    mod_results.append(res)

    if len(arrival_time) > 0:

        for arri_time in arrival_time:

            time_range = dict_get_slot_range[arri_time]

            for res in results:

                curr_arri_time = helper_time(res.arrival)
                if time_range[0] <= curr_arri_time and curr_arri_time <= time_range[1]:
                    mod_results.append(res)

    if len(mod_results) > 0:
        results = mod_results

    # print(results)
    return results


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
