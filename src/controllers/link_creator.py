import uuid
from typing import Dict


class LinkCreator:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository
        
    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            
            link_infos = { **body, 'id': link_id, 'trip_id': trip_id }
            self.__links_repository.registry_link(link_infos)
            
            return {
                'body': { 'link_id': link_id },
                'status_code': 201
            }
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }
