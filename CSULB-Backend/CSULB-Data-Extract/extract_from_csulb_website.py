""" 
scrape_csulb_website.py

All-purpose python program to pull csulb web pages.

input:
- SUBJECTS_URL
- CLASSROOMS_URL
output:
- assets
- assets/Subjects.txt
- assets/Subjects.html
- assets/<SUBJECT NAME>.html
- assets/Classrooms.html
"""
import os
import requests
import bs4

# Assets
DATA_EXTRACT_ASSETS_PATH = f"{os.path.dirname(__file__)}/assets"

# Input
SUBJECTS_URL = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject"
CLASSROOMS_URL = "https://www.csulb.edu/academic-technology-services/classroom-support-services/classroom-types-room"

# Output
SUBJECTS_HTML = f"{DATA_EXTRACT_ASSETS_PATH}/Subjects.html"
SUBJECTS_TXT = f"{DATA_EXTRACT_ASSETS_PATH}/Subjects.txt"
CLASSROOMS_HTML = f"{DATA_EXTRACT_ASSETS_PATH}/Classrooms.html"


def __init__():
    """
    Setup assets directory.
    output:
    - assets
    """
    if not os.path.exists(DATA_EXTRACT_ASSETS_PATH):
        os.makedirs(DATA_EXTRACT_ASSETS_PATH)


def get_all_subjects_to_html():
    """
    Get all subjects from website and save as HTML.
    output:
      - assets/Subjects.html
    """
    req = requests.get(SUBJECTS_URL)

    with open(SUBJECTS_HTML, "w", encoding="UTF-8") as file:
        file.write(req.text)


def get_subject_name_to_html():
    """
    Get each Subject from website and save as HTML.
    input:
      - assets/Subjects.html
    output:
      - assets/<SUBJECT NAME>.html
      - assets/Subjects.txt
    """
    with open(SUBJECTS_HTML, "r", encoding="UTF-8") as file:
        soup = bs4.BeautifulSoup(
            file, "html.parser", parse_only=bs4.SoupStrainer(class_="indexList")).findChildren("ul")

    with open(SUBJECTS_TXT, "w", encoding="UTF-8") as file:
        for subject in soup:
            # <ul>
            # <li><a href="BIOL.html">Biology (BIOL)</a></li>
            # <li><a href="BME.html">Biomedical Engineering (BME)</a></li>
            # <li><a href="BLAW.html">Business Law (BLAW)</a></li>
            # <li><a href="CBA.html">Business, College of (pre F24) (CBA)</a></li>
            # </ul>

            subject_file_name = subject.find("a")["href"]
            subject_url = f"{SUBJECTS_URL}/{subject_file_name}"

            file.write(f"{subject_file_name}\n")

            with open(f"{DATA_EXTRACT_ASSETS_PATH}/{subject_file_name}", "w", encoding="UTF-8") as subject_file:
                req = requests.get(subject_url)
                subject_file.write(req.text)


def get_classrooms_to_html():
    """
    Get all Classrooms from website and save as HTML.
    output:
    - assets/Classrooms.html
    """
    req = requests.get(CLASSROOMS_URL)
    with open(CLASSROOMS_HTML, "w", encoding="UTF-8") as file:
        file.write(req.text)


__init__()
get_all_subjects_to_html()
get_subject_name_to_html()
get_classrooms_to_html()
