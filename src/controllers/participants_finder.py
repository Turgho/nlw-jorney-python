from typing import Dict


class ParticipantsFinder:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository
        
    def find_participants(self, trip_id) -> Dict:
        try:
            participants = self.__participants_repository.find_participants_from_trip(trip_id)
            
            formatted_participants = []
            for participant in participants:
                formatted_participants.append({
                    'id': participant[0],
                    'name': participant[1],
                    'is_confirmed': participant[2],
                    'email': participant[3]
                })
                
            return {
                'body': { 'participants': formatted_participants },
                'status_code': 200
            }
            
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }