import uuid
from typing import Dict


class ParticipantsCreator:
    def __init__(self, participants_repository, emails_repository) -> None:
        self.__emails_repository = emails_repository
        self.__participants_repository = participants_repository
        
    def create(self, body, trip_id) -> Dict:
        try:
            participants_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())
            
            emails_info = {
                **body,
                'id': email_id,
                'trip_id': trip_id
            }
            
            participants_info = {
                **body,
                'id': participants_id,
                'trip_id': trip_id,
                'emails_to_invite_id': email_id,
                'is_confirmed': 0
            }
            
            self.__emails_repository.registry_email(emails_info)
            self.__participants_repository.registry_participants(participants_info)
                    
            return {
                'body': { 'id': participants_id },
                'status_code': 201
            }
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }