from typing import List


def students_credits(*args):
    #"{course name}-{credits}-{max test points}-{diyan's points}"

    threshold = 240
    result_dict = {}

    for arg in args:
        course_name, course_credits, max_points, total_points = arg.split("-")
        percentage = int(total_points)/int(max_points)
        credits = int(course_credits)*percentage
        result_dict[course_name] = credits

    total_credits = sum(result_dict.values())

    output: list[str] = []

    if total_credits<threshold:
        output.append(f"Diyan needs {abs(total_credits-threshold):.1f} credits more for a diploma.")
    else:
        output.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")

    for key, value in sorted(result_dict.items(), key=lambda x: -x[1]):
        output.append(f"\n{key} - {value:.1f}")
    return "".join(output)



print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)


# def students_credits(*args):
#     #"{course name}-{credits}-{max test points}-{diyan's points}"
#
#     threshold = 240
#     total_credits = 0
#     result_dict = {}
#
#     for arg in args:
#         course_name, course_credits, max_points, total_points = arg.split("-")
#         percentage = int(total_points)/int(max_points)
#         credits = int(course_credits)*percentage
#         result_dict[course_name] = credits
#         total_credits+=credits
#
#     output = ''
#     if total_credits<threshold:
#         output+= f"Diyan needs {abs(total_credits-threshold):.1f} credits more for a diploma."
#     else:
#         output+= f"Diyan gets a diploma with {total_credits:.1f} credits."
#
#     for key, value in sorted(result_dict.items(), key=lambda x: -x[1]):
#         output+=f"\n{key} - {value:.1f}"
#     return output
#
#
#
# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )
