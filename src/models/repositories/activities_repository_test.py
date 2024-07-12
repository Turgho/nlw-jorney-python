import uuid
from datetime import datetime

import pytest

from src.models.settings.db_connection_handdler import db_connection_handdler

from .activities_repository import ActivitiesRepository

db_connection_handdler.connect()
trip_id = str(uuid.uuid4())

# Para testar cada função, comente ou tire: @pytest.mark.skip

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_registry_actvities():
    conn = db_connection_handdler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    
    activities_trip_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'title': 'Andar na praia!',
        'occurs_at': datetime.strptime('02-01-2024', '%d-%m-%Y')
    }
    
    activities_repository.registry_activities(activities_trip_info)

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_find_actvities_from_trip():
    conn = db_connection_handdler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    
    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)