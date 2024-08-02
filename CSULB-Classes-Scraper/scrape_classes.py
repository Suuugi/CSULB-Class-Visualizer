"""
scrape_classes.py navigates to <SUBJECT NAME>.html and identifies all classes in Subject Courses.
After, it loops and puts the class information into a class_arr to be put in a database later.
"""
import os
import bs4

ASSETS_PATH = f"{os.path.dirname(__file__)}\\assets"
CLASSES_LIST = f"{ASSETS_PATH}/Classes.csv"


def parse_subject_file(subject):
    """
    Use Use <SUBJECt NAME>.html navigate and save classes into class_arr
    input:
      - assets/<SUBJECT NAME>.html
    output:
      - Looping class_arr to be transformed and put into a database
    """
    with open(f"{ASSETS_PATH}\\{subject}", 'r', encoding="UTF-8") as file:
        with open(f"{CLASSES_LIST}", 'a', encoding="UTF-8") as class_file:

            soup = bs4.BeautifulSoup(file, "html.parser")
            course_blocks = soup.find_all("div", class_="courseBlock")

            for block in course_blocks:
                course_entry = block.find_all("tr")

                # [<tr><th scope="col">SEC.</th><th scope="col">CLASS #</th><th scope="col">NO MATERIAL <br/> COST </th><th scope="col">RESERVE <br/> CAPACITY </th><th scope="col">CLASS NOTES</th><th scope="col">TYPE</th><th scope="col">DAYS</th><th scope="col">TIME</th><th scope="col">OPEN SEATS <br/> as of 07/31 05:02:21</th><th scope="col">LOCATION</th><th scope="col">INSTRUCTOR</th><th scope="col">COMMENT</th></tr>, <tr><th scope="row">03</th><td>10259</td><td></td><td><div class="dot"><a border="0" href="https://www.csulb.edu/student-records/reserved-seats-reserve-capacity-faqs"><img alt="Reserve Capacity" height="55" src="https://www.csulb.edu/sites/default/files/u33991/reserve_capacity_icon_2.png" title="Reserve Capacity" width="55"/></a></div></td><td><a href="#note1">309</a></td><td>SEM</td><td>Th</td><td>6-8:45PM</td><td><div class="dot"><a border="0" href="https://www.csulb.edu/student-records/reserved-seats-reserve-capacity-faqs"><img alt="Reserve Capacity" height="16" src="https://web.csulb.edu/depts/enrollment/registration/assets/yellow_dot.png" title="Reserve Capacity" width="16"/></a></div></td><td>ONLINE-ONLY</td><td>Huang X</td><td>Class instruction is: Online - Mixed Meet Times.<br/>Class enrollment for OMBA students only. Please contact cob-gradprograms@csulb.edu if you have questions.</td></tr>, <tr><th scope="row">03</th><td></td><td></td><td></td><td></td><td></td><td>NA</td><td>NA</td><td></td><td>ONLINE-ONLY</td><td>Huang X</td><td>additional meeting detail</td></tr>]
                for course_row in course_entry[1:]:

                    class_file.write(
                        f"{block.find(class_="courseCode").string},")
                    class_file.write(
                        f"{block.find(class_="courseTitle").string},")

                    # SEC = 01
                    # CLASS = None
                    # NO MATERIAL COST = None
                    # RESERVE CAPACITY = None
                    # CLASS NOTES = None
                    # TYPE = None
                    # DAYS = Th
                    # TIME = 6-9:45PM
                    # OPEN SEATS = None
                    # LOCATION = ONLINE-ONLY
                    # INSTRUCTOR = Staff
                    # COMMENT = additional meeting detail
                    for course_cell in course_row:
                        class_file.write(f"{course_cell.string},")
                    class_file.write("\n")


def get_classes():
    """
    Use Subjects.txt to parse the subject file for classes
    input:
      - assets/Subjects.txt
    """
    if os.path.exists(CLASSES_LIST):
        os.remove(CLASSES_LIST)

    with open(f"{ASSETS_PATH}\\Subjects.txt", 'r', encoding="UTF-8") as file:
        for subject in file:
            parse_subject_file(subject.strip())


get_classes()
