"""
extract_from_html_assets.py
Extract data from html files and save in CSULB-Data-Transform assets.
input:
- assets/Subjects.txt
- assets/<SUBJECT NAME>.html
- assets/Classrooms.html
output:
- ../CSULB-Data-Transform/assets
- ../CSULB-Data-Transform/assets/SubjectsExtract.txt
- ../CSULB-Data-Transform/assets/CoursesExtract.txt
- ../CSULB-Data-Transform/assets/ClassesExtract.txt
- ../CSULB-Data-Transform/assets/ClassroomsExtract.txt
"""
import os
import bs4

# Assets
DATA_EXTRACT_ASSETS_PATH = f"{os.path.dirname(__file__)}/assets"
DATA_TRANSFORM_ASSETS_PATH = f"{os.path.abspath(os.path.join(
    __file__, "../../"))}/CSULB-Data-Transform/assets"

# Input
SUBJECTS_TXT = f"{DATA_EXTRACT_ASSETS_PATH}/Subjects.txt"
CLASSROOMS_HTML = f"{DATA_EXTRACT_ASSETS_PATH}/Classrooms.html"

# Output
SUBJECTS_EXTRACT = f"{DATA_TRANSFORM_ASSETS_PATH}/SubjectsExtract.txt"
COURSES_EXTRACT = f"{DATA_TRANSFORM_ASSETS_PATH}/CoursesExtract.txt"
CLASSES_EXTRACT = f"{DATA_TRANSFORM_ASSETS_PATH}/ClassesExtract.txt"
CLASSROOMS_EXTRACT = f"{DATA_TRANSFORM_ASSETS_PATH}/ClassroomExtract.txt"
DEPARTMENTS_EXTRACT = f"{DATA_TRANSFORM_ASSETS_PATH}/DepartmentsExtract.txt"


def __init__():
    """
    Setup DB assets directory. If it exists, remove SUBJECTS_LIST, COURSES_LIST, and CLASSES_LIST.
    """
    if not os.path.exists(DATA_TRANSFORM_ASSETS_PATH):
        os.makedirs(DATA_TRANSFORM_ASSETS_PATH)
    if os.path.exists(SUBJECTS_EXTRACT):
        os.remove(SUBJECTS_EXTRACT)
    if os.path.exists(COURSES_EXTRACT):
        os.remove(COURSES_EXTRACT)
    if os.path.exists(CLASSES_EXTRACT):
        os.remove(CLASSES_EXTRACT)
    if os.path.exists(CLASSROOMS_EXTRACT):
        os.remove(CLASSROOMS_EXTRACT)
    if os.path.exists(DEPARTMENTS_EXTRACT):
        os.remove(DEPARTMENTS_EXTRACT)


def extract_classes_from_subjects_html():
    """
    Use assets/Subjects.txt to parse the subject file for classes
    input:
      - assets/Subjects.txt
    """
    with open(f"{SUBJECTS_TXT}", "r", encoding="UTF-8") as file:
        for subject in file:
            extract_subjects_from_subjects_html(subject.strip())


def extract_subjects_from_subjects_html(subject):
    """
    Use <SUBJECt NAME>.html to generate Subjects, Courses, and Classes Extracts.
    input:
      - assets/<SUBJECT NAME>.html
    output:
      - ../CSULB-Data-Transform/assets/SubjectsExtract.txt
      - ../CSULB-Data-Transform/assets/CoursesExtract.txt
      - ../CSULB-Data-Transform/assets/ClassesExtract.txt
    """
    with open(f"{DATA_EXTRACT_ASSETS_PATH}/{subject}", "r", encoding="UTF-8") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

        # Get Subjects Extract
        with open(f"{SUBJECTS_EXTRACT}", "a", encoding="UTF-8") as subject_file:
            subject_file.write(f"{soup.find(
                "h2", class_="departmentTitle").string}\n")

        # Get Courses and Classes Extract
        course_blocks = soup.find_all("div", class_="courseBlock")
        with open(f"{COURSES_EXTRACT}", "w", encoding="UTF-8") as course_file, open(f"{CLASSES_EXTRACT}", "w", encoding="UTF-8") as classes_file:
            for course in course_blocks:

                # Get Courses Extract
                course_code = course.find(class_="courseCode").string
                course_title = course.find(class_="courseTitle").string

                course_file.write(f"{course_code}|")
                course_file.write(f"{course_title}|\n")

                # Get Classes Extract
                course_rows = course.find_all("tr")
                for course_row in course_rows[1:]:
                    classes_file.write(f"{course_code}|")

                    for course_cell in course_row:
                        classes_file.write(f"{course_cell.string}|")

                    classes_file.write("\n")


def extract_classrooms_from_classrooms_html():
    """
    Use Classrooms.html to generate Departments and Classrooms Extracts
    input:
      - assets/Classrooms.html
    output:
      - ../CSULB-Data-Transform/assets/DepartmentsExtract.txt
      - ../CSULB-Data-Transform/assets/ClassesExtract.txt
    """
    with open(f"{CLASSROOMS_HTML}", "r", encoding="UTF-8") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

        # Get Departments Extract
        department_blocks = soup.find_all("button", class_="collapsed")
        with open(f"{DEPARTMENTS_EXTRACT}", "w", encoding="UTF-8") as departments_file:
            for department in department_blocks:
                departments_file.write(department.text.strip())

        # Get Classrooms Extract
        classroom_blocks = soup.find_all("tbody")
        for classroom in classroom_blocks:
            classroom_rows = classroom.find_all("tr")

            for classroom_row in classroom_rows[1:]:
                classroom_entry = ""

                for classroom_cell in classroom_row.findChildren():
                    classroom_entry = f"{classroom_entry}{
                        classroom_cell.text}|"

                # Get Classrooms Extract
                with open(f"{CLASSROOMS_EXTRACT}", "a", encoding="UTF-8") as classrooms_file:
                    classrooms_file.write(f"{classroom_entry}\n")


# Force user to run extract_from_csulb_website.py
if os.path.exists(SUBJECTS_TXT):
    __init__()
    extract_classes_from_subjects_html()
    extract_classrooms_from_classrooms_html()
else:
    print("Please run extract_from_csulb_website.py first.")
