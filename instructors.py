import sqlite3


class Instructor():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} teaches {self.cohort}'


class InstructorExerciseReports():


    def create_instructor(self, cursor, row):
        return Instructor(row[1], row[2], row[3], row[5])

    def __init__(self):
        self.db_path = "/Users/platt/workspace/python/exercises/student_exercises/student_exercises.db"

    def all_instructors(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                c.Name
            from instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for each in all_instructors:
                print(each)


reports = InstructorExerciseReports()
reports.all_instructors()
