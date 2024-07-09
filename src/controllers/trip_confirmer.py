from typing import Dict


class TripConfirm:
    def __init__(self,trips_repository) -> None:
        self.__trips_repository = trips_repository
        
    def confirm(self, trip_id) -> Dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)
            return { 'body': None, 'status_code': 204 }
        
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }