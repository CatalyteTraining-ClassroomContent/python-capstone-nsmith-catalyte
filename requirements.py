# pascal case for class names
# 2023-05-20 (year / month / day)

class Date:
    """
    """
    def __int__(self, day, month, year):
        self.day = day
        self.month = month
        self. year = year


class Submission:
    """
    
    """
    def __int__(self, quizName, quizModuel, quizScore, studentName, studentId, submissionDate):
        self.score = quizName
        self.quizModuel = quizModuel
        self.quizScore = quizScore
        self.name = studentName
        self.id = studentId
        self.submissionDate = submissionDate


def filter_by_date(date_of_submmission, list_of_submissions):
    """
    Given I have a list of submission objects, when I call the filterByDate function with
a date and the list of submissions (in that order), then a list of submission objects
with a submissionDate equal to that date are 
    Returns: 
        List of submission objects for a particular date.
    """
    for date in list_of_submissions:
        if date == list_of_submissions.date:
            return list_of_submittions for that day


# def filter_by_student_id(studentId, list_of_submissions):
#     """ 
#     Given I have a list of submission objects, when I supply a studentId and the list (in
# that order) to the filter_by_student_id function, then submission objects with a
# studentId equal to the studentId I supplied are returned to me, so I can see all
# submissions for a particular student.
# 2. Given I have supplied a studentId and a list of submission objects (in that order),
# when the list is empty, or the filter_by_student_id feature does not find any results,
# then I am returned an empty list.
#     Parameters:
#         Student id and list of submissions.

#     Returns:
#         If the list is empty, or the filter_by_student_id feature does not find any results return empty list. Otherwise return all
# submissions for a particular student.
#     """
#     if not studenId or not list_of_submissions:
#         return []
#     else:
#         for studentId in list_of_submissions:
#             if studentId == list_of_submissions.id:
#                 return 



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

# filter_by_date(date_of_submmission, list_of_submissions)
# def filter_by_student_id(studentId, list_of_submissions)
# find_unsubmitted(date, list_of_student_names, list_of_submissions)
# get_average_score(list_of_submissions)
# get_average_score_by_module(list_of_submissions)