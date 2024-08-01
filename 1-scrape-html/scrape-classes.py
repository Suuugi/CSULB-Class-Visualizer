import os, bs4

assets_path = f"{os.path.dirname(__file__)}\\assets"

def parse_subject_file(subject):
  class_arr = [None] * 12

  with open(f"{assets_path}\\{subject}") as file:
    soup = bs4.BeautifulSoup(file, "html.parser")
    course_blocks = soup.find_all("div", class_="courseBlock")
    
    for block in course_blocks:
      course_code = block.find(class_="courseCode").string
      course_title = block.find(class_="courseTitle").string

      print(f"{course_code} - {course_title}")
      
      course_entry = block.find_all("tr")

      # [<tr><th scope="col">SEC.</th><th scope="col">CLASS #</th><th scope="col">NO MATERIAL <br/> COST </th><th scope="col">RESERVE <br/> CAPACITY </th><th scope="col">CLASS NOTES</th><th scope="col">TYPE</th><th scope="col">DAYS</th><th scope="col">TIME</th><th scope="col">OPEN SEATS <br/> as of 07/31 05:02:21</th><th scope="col">LOCATION</th><th scope="col">INSTRUCTOR</th><th scope="col">COMMENT</th></tr>, <tr><th scope="row">03</th><td>10259</td><td></td><td><div class="dot"><a border="0" href="https://www.csulb.edu/student-records/reserved-seats-reserve-capacity-faqs"><img alt="Reserve Capacity" height="55" src="https://www.csulb.edu/sites/default/files/u33991/reserve_capacity_icon_2.png" title="Reserve Capacity" width="55"/></a></div></td><td><a href="#note1">309</a></td><td>SEM</td><td>Th</td><td>6-8:45PM</td><td><div class="dot"><a border="0" href="https://www.csulb.edu/student-records/reserved-seats-reserve-capacity-faqs"><img alt="Reserve Capacity" height="16" src="https://web.csulb.edu/depts/enrollment/registration/assets/yellow_dot.png" title="Reserve Capacity" width="16"/></a></div></td><td>ONLINE-ONLY</td><td>Huang X</td><td>Class instruction is: Online - Mixed Meet Times.<br/>Class enrollment for OMBA students only. Please contact cob-gradprograms@csulb.edu if you have questions.</td></tr>, <tr><th scope="row">03</th><td></td><td></td><td></td><td></td><td></td><td>NA</td><td>NA</td><td></td><td>ONLINE-ONLY</td><td>Huang X</td><td>additional meeting detail</td></tr>]
      for course_row in course_entry[1:]:
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
        for index, course_cell in enumerate(course_row):
          class_arr[index] = course_cell.string
        print(class_arr)

def get_classes():
  with open(f"{assets_path}\\Subjects.txt", 'r') as file:
    for subject in file:
      parse_subject_file(subject.strip())

get_classes()