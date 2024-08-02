Build 0.1
=========

Subject [1..*] Courses [1..*] Classes

Requirements...
python3
virtualenv
requests
beautifulsoup4

Housekeeping...
- Update Execution Policy for venv = Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
- Enable Virtual Environment = <path>\CSULB-Class-Visualizer\CSULB-Subjects-Scraper\venv\Scripts\activate.ps1
- Install Virtual Environment = pip install -r <path>\CSULB-Class-Visualizer\CSULB-Subjects-Scraper\requirements.txt

Logic...
1. I used python's request library to pull the website of all course subjects and saved it into a html file (that way I don't keep querying the website).
https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/index.html

2. I opened the saved file into beautiful soup. Beautiful soup is good for html traversal which allowed me to grab all the important html tags with the data I needed (which is a bunch of li's within a ul). 
https://beautiful-soup-4.readthedocs.io/en/latest/

3. I grabbed the href attribute and created a list of urls to the many subject pages for request and traversal later. On those subject pages are a bunch of tables with the course id, name, and section #'s.

4. Pretty much like 1, but using the list of subject page urls.
https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/ACCT.html, https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2024/By_Subject/AFRS.html, etc.

5. Pretty much like 2, but digging into a table rather than a list.

6. Build and output the row with the results and save into Classese.csv to be inputted into a DB later.

Results(with all parsed data): Classes.csv 