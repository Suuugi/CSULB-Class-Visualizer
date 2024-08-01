import os, requests, bs4

# Index url location 
index_url = "https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject"
assets_path = f"{os.path.dirname(__file__)}/assets"
subjects_html = f"{assets_path}/Subjects.html"
subjects_list = f"{assets_path}/Subjects.txt"

def get_index_file():
  """
  Navigate and save index file with all school subjects 
  output:
    - assets/Subjects.html
  """
  req = requests.get(index_url)
  with open(subjects_html, 'w') as file:
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
  with open(subjects_html, 'r') as file:
    subjects_soup = bs4.BeautifulSoup(file, "html.parser", parse_only=bs4.SoupStrainer(class_="indexList"))
  
  with open(subjects_list, 'w') as file:
    for subject in subjects_soup.findChildren("ul"):
      # <ul>
      # <li><a href="BIOL.html">Biology (BIOL)</a></li>
      # <li><a href="BME.html">Biomedical Engineering (BME)</a></li>
      # <li><a href="BLAW.html">Business Law (BLAW)</a></li>
      # <li><a href="CBA.html">Business, College of (pre F24) (CBA)</a></li>
      # </ul>

      subject_file_name = subject.find('a')['href'] # subject_file_name = BIOL.html
      subject_url = f"{index_url}/{subject_file_name}"

      # Write to subjects_list
      file.write(f"{subject_file_name}\n")

      # Write to subject_file
      with open(f"{assets_path}/{subject_file_name}", "w") as subject_file:
        req = requests.get(subject_url)
        subject_file.write(req.text)

get_index_file()
get_subject_files()