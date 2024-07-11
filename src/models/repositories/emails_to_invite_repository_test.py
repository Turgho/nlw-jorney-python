import uuid

import pytest

from src.models.settings.db_connection_handdler import db_connection_handdler

from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handdler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_regestry_email():
    conn = db_connection_handdler.get_connection()
    email_to_invite_repository = EmailsToInviteRepository(conn)
    
    email_trips_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'email': 'helloworld@gmail.com'
    }
    
    email_to_invite_repository.registry_email(email_trips_info)

@pytest.mark.skip(reason='interacao com o banco de dados')
def test_find_emails_from_trip():
    conn = db_connection_handdler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)