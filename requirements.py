# pascal case for class names
# 2023-05-20 (year / month / day)

# class Submission:

#     def __intit__(
#         self, quizName, quizModuel, quizScore, studentId, studentName, submissionDate
#     ):
#         self.score = quizName
#         self.quizModuel = quizModuel
#         self.quizScore = quizScore
#         self.name = studentName
#         self.id = studentId
#         self.submissionDate = submissionDate
#     def __str__(self):
#         print("")
# list_of_submissions = [
#     Submission("Revolution", "History", 99.9, 8701, "Noah", "2023-05-20"),
#     Submission("Variables", "Algebra", 89.2, 8702, "Ivan", "2023-03-16"),
#     Submission("Shakespear", "English", 30.5, 8703, "Ricky", "2023-01-29"),
#     Submission("Evolution", "Science", 78.6, 8704, "Oscar", "2023-10-07"),
# ]


list_of_submissions = [
    {
        "quizName": "Revolution",
        "quizModule": "History",
        "quizScore": 99.9,
        "studentId": 8701,
        "studentName": "Noah",
        "submissionDate": "2023-05-20",
    },
    {
        "quizName": "Variables",
        "quizModule": "Algebra",
        "quizScore": 89.2,
        "studentId": 8702,
        "studentName": "Ivan",
        "submissionDate": "2023-03-16",
    },
    {
        "quizName": "Shakspeare",
        "quizModule": "English",
        "quizScore": 30.5,
        "studentId": 8703,
        "studentName": "Ricky",
        "submissionDate": "2023-01-29",
    },
    {
        "quizName": "Evolution",
        "quizModule": "Science",
        "quizScore": 78.6,
        "studentId": 8704,
        "studentName": "Oscar",
        "submissionDate": "2023-10-07",
    },
]
studentId = 0

# def filter_by_date(date_of_submmission, list_of_submissions):
#     """
#     Given I have a list of submission objects, when I call the filterByDate function with
#     a date and the list of submissions (in that order), then a list of submission objects
#     with a submissionDate equal to that date are
#         Returns:
#             List of submission objects for a particular date.
#     """
#     for date in list_of_submissions:
#         if date["submissionDate"] == date_of_submmission:
#             return (
#                 date["quizName"],
#                 date["quizModule"],
#                 date["quizScore"],
#                 date["studentId"],
#                 date["studentName"],
#                 date["submissionDate"],
#             )


def filter_by_student_id(studentId, list_of_submissions):
    """
        Given I have a list of submission objects, when I supply a studentId and the list (in
    that order) to the filter_by_student_id function, then submission objects with a
    studentId equal to the studentId I supplied are returned to me, so I can see all
    submissions for a particular student.
    2. Given I have supplied a studentId and a list of submission objects (in that order),
    when the list is empty, or the filter_by_student_id feature does not find any results,
    then I am returned an empty list.

        Parameters:
            Student id and list of submissions.
        Returns:
            If the list is empty, or the filter_by_student_id feature does not find any results return empty list. Otherwise return all
    submissions for a particular student.
    """
    if studentId or not list_of_submissions:
        print([])
        return []
    else:
        for studentId in list_of_submissions:
            if studentId == list_of_submissions.id:
                return


# def find_unsubmitted(date, list_of_student_names, list_of_submissions):
#     """
#     Given I have a list of submission objects, when I supply a date, a list of student
#     names, and a list of submission objects (in that order) to the find_unsubmitted
#     function, then I am returned a list of names of students that have not completed
#     any quiz on that date.
#     2. Given that the find unsubmitted feature does not find any student names, I am
#     returned an empty list.
#     """
#     unsubmitted_names = []
#     return "list of names of students that have not completed any quiz on that date." unsubmitted_names


# def get_average_score(list_of_submissions):
#     """
#     From a list of submission objects find the average of all the quiz scores.

#     Parameters:
#         list of submissions

#     Returns:
#         average of all quiz scores (float of one decimal point).

#     """
#     quizScore / len(quizScore)
#     return average_score "float"


# def get_average_score_by_module(list_of_submissions):
#     """ """

#     return moduel get_average_score_by_module()

# filter_by_date("2023-05-20", list_of_submissions)
filter_by_student_id(8703, list_of_submissions)
# find_unsubmitted(date, list_of_student_names, list_of_submissions)
# get_average_score(list_of_submissions)
# get_average_score_by_module(list_of_submissions)
