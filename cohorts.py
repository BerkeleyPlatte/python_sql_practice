import sqlite3


class Cohort():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class CohortReports():

    def __init__(self):
        self.db_path = "/Users/platt/workspace/python/exercises/student_exercises/student_exercises.db"

    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select c.Name
                from Cohort c
                """)

            cohorts = db_cursor.fetchall()

            for cohort in cohorts:
                print(cohort)


reports = CohortReports()
reports.all_cohorts()
