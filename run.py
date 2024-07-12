from src.main.server.server import app
from src.models.settings.db_connection_handdler import db_connection_handdler

if __name__ == '__main__':
    db_connection_handdler.connect()
    app.run(host='0.0.0.0', port=5000, debug=True)