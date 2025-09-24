# pascal case for class names
# 2023-05-20 (year / month / day)

list_of_submissions = [
    {
        "quizName": "Revolution",
        "quizModule": "History",
        "quizScore": 99.9,
        "studentId": 8701,
        "studentName": "Matt",
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
        "submissionDate": "2023-4-04",
    },
    {
        "quizName": "Variables",
        "quizModule": "Algebra",
        "quizScore": 45.3,
        "studentId": 8705,
        "studentName": "Jane",
        "submissionDate": "2023-10-07",
    },
    {
        "quizName": "Evolution",
        "quizModule": "Science",
        "quizScore": 78.6,
        "studentId": 8706,
        "studentName": "Jacob",
        "submissionDate": "2023-05-20",
    },
    {
        "quizName": "Revolution",
        "quizModule": "History",
        "quizScore": 70,
        "studentId": 8707,
        "studentName": "Maria",
        "submissionDate": "2023-11-30",
    },
]
studentId = 0
student_list = [
    "Noah",
    "Ivan",
    "Ricky",
    "Oscar",
]


def filter_by_date(date_of_submmission, list_of_submissions):
    """
    Given I have a list of submission objects, when I call the filterByDate function with
    a date and the list of submissions (in that order), then a list of submission objects
    with a submissionDate equal to that date are
        Returns:
            List of submission objects for a particular date.
    """
    if not list_of_submissions:
        return []
    else:
        for date in list_of_submissions:
            if date["submissionDate"] == date_of_submmission:
                return (
                    date["studentName"],
                    date["quizName"],
                    date["quizModule"],
                    date["quizScore"],
                    date["studentId"],
                    date["submissionDate"],
                )
            else:
                return []


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
    if not studentId or not list_of_submissions:
        return []
    else:
        for id in list_of_submissions:
            if id["studentId"] == studentId:
                return (
                    id["studentName"],
                    id["quizName"],
                    id["quizModule"],
                    id["quizScore"],
                    id["studentId"],
                    id["submissionDate"],
                )


def find_unsubmitted(date, list_of_student_names, list_of_submissions):
    """
    Given I have a list of submission objects, when I supply a date, a list of student
    names, and a list of submission objects to the find_unsubmitted
    function, then I am returned a list of names of students that have not completed
    any quiz on that date.
    2. Given that the find unsubmitted feature does not find any student names, I am
    returned an empty list.
    returns:
    "names of students that have not completed any quiz on that date."
    """
    if not list_of_student_names:
        return []
    user_chosen_names = set()
    for submission in list_of_submissions:
        if submission["submissionDate"] == date:
            user_chosen_names.add(submission["studentName"])
    unsubmitted = []
    for student in list_of_student_names:
        if student not in user_chosen_names:
            unsubmitted.append(student)
    return unsubmitted


def get_average_score(list_of_submissions):
    """
    From a list of submission objects find the average of all the quiz scores.
    Parameters:
        list of submissions
    Returns:
        average of all quiz scores (float of one decimal point).
    """
    average = 0
    for score in list_of_submissions:
        average += score["quizScore"]
    return round(average / len(list_of_submissions), 1)


def get_average_score_by_module(list_of_submissions):
    moduel_and_score = {}
    for score in list_of_submissions:
        module_list = score["quizModule"]
        score_list = score["quizScore"]
        if score["quizModule"] not in module_list:
            module_list.add(score["quizModule"])
            average += score["quizScore"]

    print(module_list, round(average / len(score_list), 1))


# filter_by_date("2023-05-20", list_of_submissions)
# filter_by_student_id(8703, list_of_submissions)
# find_unsubmitted("2023-10-07", student_list, list_of_submissions)
# get_average_score(list_of_submissions)
get_average_score_by_module(list_of_submissions)
