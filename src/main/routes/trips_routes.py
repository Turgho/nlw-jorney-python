from flask import Blueprint, jsonify, request

# import Controllers
from src.controllers.activities_creator import ActivitiesCreator
from src.controllers.activities_finder import ActivitiesFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participants_confirmer import ParticipantConfirm
from src.controllers.participants_creator import ParticipantsCreator
from src.controllers.participants_finder import ParticipantsFinder
from src.controllers.trip_confirmer import TripConfirm
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.models.repositories.activities_repository import ActivitiesRepository
# import Repositories
from src.models.repositories.emails_to_invite_repository import \
    EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import \
    ParticipantsRepository
from src.models.repositories.trips_repository import TripsRepository
# import connection DB
from src.models.settings.db_connection_handdler import db_connection_handdler

# import Repositories



trips_routes_bp = Blueprint('trip_routes', __name__)

# TRIPS ROUTES

@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    conn = db_connection_handdler.get_connection()
    
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)
    
    response = controller.create(request.json)
    
    return jsonify(response['body']), response['status_code']

@trips_routes_bp.route('/trips/<trip_id>', methods=['GET'])
def find_trip(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)
    
    response = controller.find_trip_details(trip_id)
    
    return jsonify(response['body'], response['status_code'])

@trips_routes_bp.route('/trips/<trip_id>/confirm', methods=['GET'])
def confirm_trip(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    trips_repository = TripsRepository(conn)
    controller = TripConfirm(trips_repository)
    
    response = controller.confirm(trip_id)
    
    return jsonify(response['body'], response['status_code'])

# TRIPS LINKS ROUTES

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['POST'])
def create_trip_link(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response['body'], response['status_code'])

@trips_routes_bp.route('/trips/<trip_id>/links', methods=['GET'])
def find_links(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)
    
    response = controller.find_links(trip_id)
    
    return jsonify(response['body'], response['status_code'])

# TRIPS PARTICIPANTS ROTES

@trips_routes_bp.route('/trips/<trip_id>/invite', methods=['POST'])
def create_participant(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantsCreator(participants_repository, emails_repository)
    
    response = controller.create(request.json, trip_id)
    
    print(response)
    
    return jsonify(response['body'], response['status_code'])

@trips_routes_bp.route('/trips/<trip_id>/invite', methods=['GET'])
def find_participants(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    parcipants_repository = ParticipantsRepository(conn)
    controller = ParticipantsFinder(parcipants_repository)
    
    response = controller.find_participants(trip_id)
    
    return jsonify(response['body'], response['status_code'])

@trips_routes_bp.route('/participants/<participant_id>/confirm', methods=['PATCH'])
def confirm_participant(participant_id):
    conn = conn = db_connection_handdler.get_connection()
    
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirm(participants_repository)
    
    response = controller.confirm(participant_id)
    print(response)
    
    return jsonify(response['body'], response['status_code'])

# TRIPS ACTIVITIES ROUTES

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['POST'])
def create_activities(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    activities_repository = ActivitiesRepository(conn)
    controller = ActivitiesCreator(activities_repository)
    
    response = controller.create(request.json, trip_id)
    
    return jsonify(response['body'], response['status_code'])

@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['GET'])
def find_activities(trip_id):
    conn = conn = db_connection_handdler.get_connection()
    
    activities_repository = ActivitiesRepository(conn)
    controller = ActivitiesFinder(activities_repository)
    
    response = controller.find_activity(trip_id)
    
    return jsonify(response['body'], response['status_code'])