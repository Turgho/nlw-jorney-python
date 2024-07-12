import uuid
from datetime import datetime, timedelta

import pytest

from src.models.settings.db_connection_handdler import db_connection_handdler

from .participants_repository import ParticipantsRepository

db_connection_handdler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())

# Para testar cada função, comente ou tire: @pytest.mark.skip

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_create_participants():
    conn = db_connection_handdler.get_connection()
    parcipants_repository = ParticipantsRepository(conn)
    
    participants_info = {
        'id': participant_id,
        'trip_id': trip_id,
        'emails_to_invite_id': str(uuid.uuid4()),
        'name': 'João'
    }
    parcipants_repository.registry_participants(participants_info)
    
@pytest.mark.skip(reason='interacao com o banco de dados')
def test_find_participants_from_trip():
    conn = db_connection_handdler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants = participants_repository.find_participants_from_trip(trip_id)
    print()
    print(participants)

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_update_partucipant_status():
    conn = db_connection_handdler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants_repository.update_participant_status(participant_id)