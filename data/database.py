import sqlite3

class VoiceClipDB:
    def __init__(self):
        self.conn = self.create_connection('voice_clips.db')
        self.setup()

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def setup(self):
        sql_create_clips_table = """CREATE TABLE IF NOT EXISTS clips (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        description text,
                                        author text,
                                        file_location text NOT NULL
                                    ); """
        if self.conn is not None:
            #create_table(self.conn, sql_create_clips_table)
            cursor = self.conn.cursor()
            cursor.execute(sql_create_clips_table)
            self.conn.commit()
            print("created table lol?")
        else:
            print("Could not create table.")


database = VoiceClipDB()
