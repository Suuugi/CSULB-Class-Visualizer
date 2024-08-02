""" 
scrape_subjects.py navigates to INDEX_URL and identifies all CSULB Subjects.
After, it uses the list of Subjects to save off all the Subject html files.
"""
import os
import requests
import bs4

INDEX_URL = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/"
SCRAPER_ASSETS_PATH = f"{os.path.dirname(__file__)}/assets"
SUBJECTS_HTML = f"{SCRAPER_ASSETS_PATH}/Subjects.html"
SUBJECTS_TXT = f"{SCRAPER_ASSETS_PATH}/Subjects.txt"


def __init__():
    """
    Setup assets directory.
    """
    if not os.path.exists(SCRAPER_ASSETS_PATH):
        os.makedirs(SCRAPER_ASSETS_PATH)


def get_index_file():
    """
    Navigate and save index file with all school subjects 
    output:
      - assets/Subjects.html
    """
    req = requests.get(INDEX_URL)

    with open(SUBJECTS_HTML, 'w', encoding="UTF-8") as file:
        file.write(req.text)


def get_subject_files():
    """
    Use saved index file to navigate and save all school subject files
    input:
      - assets/Subjects.html
    output:
      - assets/<SUBJECT NAME>.html
      - assets/Subjects.txt
    """
    with open(SUBJECTS_HTML, 'r', encoding="UTF-8") as file:
        subjects_soup = bs4.BeautifulSoup(
            file, "html.parser", parse_only=bs4.SoupStrainer(class_="indexList"))

    with open(SUBJECTS_TXT, 'w', encoding="UTF-8") as file:
        for subject in subjects_soup.findChildren("ul"):
            # <ul>
            # <li><a href="BIOL.html">Biology (BIOL)</a></li>
            # <li><a href="BME.html">Biomedical Engineering (BME)</a></li>
            # <li><a href="BLAW.html">Business Law (BLAW)</a></li>
            # <li><a href="CBA.html">Business, College of (pre F24) (CBA)</a></li>
            # </ul>

            subject_file_name = subject.find('a')['href']
            subject_url = f"{INDEX_URL}/{subject_file_name}"

            file.write(f"{subject_file_name}\n")

            with open(f"{SCRAPER_ASSETS_PATH}/{subject_file_name}", "w", encoding="UTF-8") as subject_file:
                req = requests.get(subject_url)
                subject_file.write(req.text)


__init__()
get_index_file()
get_subject_files()
