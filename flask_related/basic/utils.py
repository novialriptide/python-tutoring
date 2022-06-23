import json


def calculate_gpa(grades):
    gpa_data = json.load(open("grades.json"))

    gpa = 0
    i = 0
    for g in grades:
        if g == "":
            continue

        gpa += gpa_data[g]
        i += 1

    return gpa / i
