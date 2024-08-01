import os, requests, bs4

by_subject_url = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject"
index_url = f"{by_subject_url}/index.html"

assets_path = f"{os.path.dirname(__file__)}\\assets"
subjects_file = f"{assets_path}\\Subjects.html"
subject_list_file = f"{assets_path}\\Subjects.txt"

def get_subject_index_file():
  req = requests.get(index_url)
  with open(subjects_file, 'w') as file:
    file.write(req.text)

def get_subjects():
  with open(subjects_file, 'r') as file:
    subject_soup = bs4.BeautifulSoup(file, "html.parser", parse_only=bs4.SoupStrainer(class_="indexList"))
  
  with open(subject_list_file, 'w') as file:
    for subject in subject_soup.findChildren("ul"):
      subject_file_name = subject.find('a')['href']
      subject_url = f"{by_subject_url}/{subject_file_name}"
      file.write(f"{subject_file_name}\n")

      with open(f"{assets_path}\\{subject_file_name}", "w") as subject_file:
        req = requests.get(subject_url)
        subject_file.write(req.text)

get_subject_index_file()
get_subjects()