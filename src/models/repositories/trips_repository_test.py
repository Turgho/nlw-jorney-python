import uuid
from datetime import datetime, timedelta

import pytest

from src.models.settings.db_connection_handdler import db_connection_handdler

from .trips_repository import TripsRepository

db_connection_handdler.connect()
trip_id = str(uuid.uuid4())

# Para testar cada função, comente ou tire: @pytest.mark.skip

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_create_trip():
    conn = db_connection_handdler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_info = {
        'id': trip_id,
        'destination': 'Osaka',
        'start_date': datetime.strptime('02-01-2024', '%d-%m-%Y'),
        'end_date': datetime.strptime('02-01-2024', '%d-%m-%Y') + timedelta(days=5),
        'owner_name': 'Piraque',
        'owner_email': 'piraque@gmail.com'
    }
    
    trips_repository.create_trip(trips_info)
    
@pytest.mark.skip(reason='interacao com o banco de dados')
def test_find_trip_by_id():
    conn = db_connection_handdler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    print()
    print(trip)

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_update_trip_status():
    conn = db_connection_handdler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_repository.update_trip_status(trip_id)