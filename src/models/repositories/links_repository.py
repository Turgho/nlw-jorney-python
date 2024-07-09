from sqlite3 import Connection
from typing import Dict, Tuple


class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def registry_link(self, link_info: Dict) -> None:
        print(link_info)
        
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links (
                    id,
                    trip_id,
                    title,
                    link
                ) VALUES (
                    ?, ?, ?, ?
                )
            ''', (
                link_info['id'],
                link_info['trip_id'],
                link_info['title'],
                link_info['link']
            )
        )
        self.__conn.commit()
        
    def find_link_from_trip(self, trip_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE id = ?''', (trip_id,)
        )
        link = cursor.fetchall()
        return link
    