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
    When called returns a list of submission objects with a submissionDate equal to user date.

    Parameters:
        User chosen date and list of summission objects.

    Returns:
        Empty list if submissions are empty or date is not found. Else: list of submission objects for a particular date.
    """
    if not list_of_submissions:
        return []
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
    Gets submission objects based on date.

    Parameters:
        Student id and a list of submissions.

    Returns:
        Empty list if submission list is empty, or studentId does not find any results. Otherwise returns all submissions for a particular student.
    """
    if not list_of_submissions:
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
            else:
                return []


def find_unsubmitted(date, list_of_student_names, list_of_submissions):
    """
    Gives list of students that have not completed any quiz on the date.

    parameters:
        Date for seach, list of names, list of submission objects.

    returns:
        Names of students that have not completed any quiz on given date.
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
        List of submissions.

    Returns:
        Average of all quiz scores (float of one decimal point).
    """
    average = 0
    for score in list_of_submissions:
        average += score["quizScore"]
    return round(average / len(list_of_submissions), 1)


def get_average_score_by_module(list_of_submissions):
    """
    Finds the average of all quiz scores from the same "quizModule".

    Parameters:
        List of submissions.

    Returns:
        Object of all quiz scores (float of one decimal point) for each quiz name.
    """
    module_scores = {}
    for submission in list_of_submissions:
        module = submission["quizModule"]
        score = submission["quizScore"]
        if module not in module_scores:
            module_scores[module] = []
        module_scores[module].append(score)
    average_by_module = {
        module: round(sum(scores) / len(scores), 1)
        for module, scores in module_scores.items()
    }
    return average_by_module


filter_by_date("2023-05-20", list_of_submissions)
filter_by_student_id(8703, list_of_submissions)
find_unsubmitted("2023-10-07", student_list, list_of_submissions)
get_average_score(list_of_submissions)
get_average_score_by_module(list_of_submissions)
