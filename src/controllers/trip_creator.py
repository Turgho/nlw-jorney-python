import uuid
from typing import Dict


class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository
        
    def create(self, body) -> Dict:
        try:
            emails = body.get('emails_to_invite')
        
            trip_id = str(uuid.uuid4())
            trips_info = { **body, 'id': trip_id }
            
            self.__trip_repository.create_trip(trips_info)
            
            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        'email':email,
                        'trip_id': trip_id,
                        'id': str(uuid.uuid4())
                    })
                    
            return {
                'body': { 'id': trip_id },
                'status_code': 201
            }
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }