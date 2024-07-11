from typing import Dict


class ActivitiesFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository
        
    def find_activity(self, trip_id) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)
            
            formatted_activities = []
            print(activities)
            
            for activity in activities:
                formatted_activities.append({
                    'id': activity[0],
                    'title': activity[2],
                    'occurs-at': activity[3]
                })
                
            return {
                'body': { 'Activites': formatted_activities },
                'status_code': 200
            }
            
        except Exception as err:
            return {
                'body': { 'error': 'bad request' },
                'message': str(err),
                'status_code': 400
            }