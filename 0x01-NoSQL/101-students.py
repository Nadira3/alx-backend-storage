#!/usr/bin/env python3

""" module containing database function """

list_all = __import__('8-all').list_all


def top_students(mongo_collection):
    """
        function that returns all students
        sorted by average score
    """

    students = list_all(mongo_collection)
    stud_list = []

    for student in students:
        stud_dict = {}
        stud_dict['_id'] = student['_id']
        stud_dict['name'] = student['name']
        topics = student['topics']

        total_score = sum(topic['score'] for topic in topics)
        number_of_topics = len(topics)

        stud_dict['averageScore'] = total_score / number_of_topics
        stud_list.append(stud_dict)
    stud_list.sort(key=lambda x: x['averageScore'], reverse=True)
    return stud_list
