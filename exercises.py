import sqlite3


class Exercise():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f"{self.name} uses {self.language}"


class ExerciseReports():
    def __init__(self):
        self.db_path = "/Users/platt/workspace/python/exercises/student_exercises/student_exercises.db"

    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.Name,
                    e.LanguageName
                from Exercise e
                where e.LanguageName = 'lOne'
                """)

            exercises = db_cursor.fetchall()

            for each in exercises:
                print(each)
                
reports = ExerciseReports()
reports.all_exercises()
