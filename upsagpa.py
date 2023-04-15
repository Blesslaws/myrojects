import streamlit as st

def calculate_gpa(courses):
    total_credits = 0
    total_points = 0
    for course in courses:
        credit_hours = course["credit_hours"]
        grade = course["grade"]
        if grade >= 90:
            grade_point = 4.0
        elif grade >= 85:
            grade_point = 3.7
        elif grade >= 80:
            grade_point = 3.3
        elif grade >= 75:
            grade_point = 3.0
        elif grade >= 70:
            grade_point = 2.7
        elif grade >= 65:
            grade_point = 2.3
        elif grade >= 60:
            grade_point = 2.0
        elif grade >= 55:
            grade_point = 1.7
        elif grade >= 50:
            grade_point = 1.3
        else:
            grade_point = 0.0
        total_credits += credit_hours
        total_points += grade_point * credit_hours
        course["grade_point"] = grade_point
        course["total_points"] = grade_point * credit_hours
    gpa = total_points / total_credits
    return gpa, total_points

st.header("Calculate GPA")

total_courses = st.number_input("Enter the total number of courses:", value=0, min_value=0, step=1)

courses = []

for i in range(total_courses):
    st.subheader(f"Course {i+1}")
    course_name = st.text_input(f"Enter the name of course {i+1}:")
    grade = st.number_input(f"Enter the grade for course {i+1} (0-100):", value=0.0, min_value=0.0, max_value=100.0, step=1.0)
    credit_hours = st.number_input(f"Enter the credit hours for course {i+1}:", value=0.0, min_value=0.0, step=0.5)

    course = {"name": course_name, "grade": grade, "credit_hours": credit_hours}
    courses.append(course)

if st.button("Calculate GPA"):
    gpa, total_points = calculate_gpa(courses)
    st.write("Number of courses:", total_courses)
    st.write("Courses:")
    for course in courses:
        st.write(f" - {course['name']}: Grade - {course['grade']}, Credit hours - {course['credit_hours']}, Grade point - {course['grade_point']}, Total grade points - {course['total_points']}")
    st.write(f"GPA: {gpa:.2f}, Total grade points: {total_points:.2f}")
