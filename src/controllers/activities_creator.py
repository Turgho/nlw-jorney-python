import uuid
from typing import Dict


class ActivitiesCreator:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository
        
    def create(self, body, trip_id) -> Dict:
        try:
            activity_id = str(uuid.uuid4())
            
            activity_info = { **body, 'id': activity_id, 'trip_id': trip_id }
            
            self.__activities_repository.registry_activity(activity_info)
            return {
                'body': { 'id': activity_id },
                'status_code': 201
            }
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }