import uuid

import pytest

from src.models.settings.db_connection_handdler import db_connection_handdler

from .links_repository import LinksRepository

db_connection_handdler.connect()
trip_id = str(uuid.uuid4())

def test_registry_link():
    conn = db_connection_handdler.get_connection()
    links_repository = LinksRepository(conn)
    
    trip_link_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'title': 'Hotel',
        'link': 'http://google.com'
    }
    
    links_repository.registry_link(trip_link_info)