"""
scrape_classes.py navigates to <SUBJECT NAME>.html and identifies all classes in Subject Courses.
After, it loops and puts the class information into a class_arr to be put in a database later.
"""
import os
import bs4

SCRAPER_ASSETS_PATH = f"{os.path.dirname(__file__)}/assets"
LOAD_DB_ASSETS_PATH = f"{os.path.abspath(os.path.join(
    __file__, "../../"))}/CSULB-Load-Database/assets"
SUBJECTS_TXT = f"{SCRAPER_ASSETS_PATH}/Subjects.txt"
SUBJECTS_LIST = f"{LOAD_DB_ASSETS_PATH}/ScrapedSubjects.txt"
COURSES_LIST = f"{LOAD_DB_ASSETS_PATH}/ScrapedCourses.txt"
CLASSES_LIST = f"{LOAD_DB_ASSETS_PATH}/ScrapedClasses.txt"


def __init__():
    """
    Setup DB assets directory. If it exists, remove SUBJECTS_LIST, COURSES_LIST, and CLASSES_LIST.
    """
    if not os.path.exists(LOAD_DB_ASSETS_PATH):
        os.makedirs(LOAD_DB_ASSETS_PATH)
    if os.path.exists(SUBJECTS_LIST):
        os.remove(SUBJECTS_LIST)
    if os.path.exists(COURSES_LIST):
        os.remove(COURSES_LIST)
    if os.path.exists(CLASSES_LIST):
        os.remove(CLASSES_LIST)


def parse_subject_file(subject):
    """
    Use Use <SUBJECt NAME>.html navigate and save classes into class_arr
    input:
      - assets/<SUBJECT NAME>.html
    output:
      - Looping class_arr to be transformed and put into a database
    """
    with open(f"{SCRAPER_ASSETS_PATH}/{subject}", 'r', encoding="UTF-8") as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

        with open(f"{SUBJECTS_LIST}", 'a', encoding="UTF-8") as subject_file:
            subject_file.write(f"{
                soup.find("h2", class_="departmentTitle").string}|\n")

        course_blocks = soup.find_all("div", class_="courseBlock")
        for block in course_blocks:
            with open(f"{COURSES_LIST}", 'a', encoding="UTF-8") as course_file:
                course_code = block.find(class_="courseCode").string
                course_title = block.find(class_="courseTitle").string

                course_file.write(f"{course_code}|")
                course_file.write(f"{course_title}|\n")

            with open(f"{CLASSES_LIST}", 'a', encoding="UTF-8") as class_file:
                course_entry = block.find_all("tr")

                for course_row in course_entry[1:]:
                    class_file.write(f"{course_code}|")

                    for course_cell in course_row:
                        class_file.write(f"{course_cell.string}|")

                    class_file.write("\n")


def get_classes():
    """
    Use Subjects.txt to parse the subject file for classes
    input:
      - assets/Subjects.txt
    """
    with open(f"{SUBJECTS_TXT}", 'r', encoding="UTF-8") as file:
        for subject in file:
            parse_subject_file(subject.strip())


# Force user to run scrape_subjects.py first.
if os.path.exists(SUBJECTS_TXT):
    __init__()
    get_classes()
else:
    print("Please run scrape_subjects.py first.")
