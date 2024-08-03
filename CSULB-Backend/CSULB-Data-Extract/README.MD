Build 0.2
=========
Logic:
1. Use python's request library to pull web website and it into assets directory (that way I don't keep querying the website).
2. Open saved files into beautiful soup. Beautiful soup is good for html traversal which allows for simple tag traversal.
3. Loop through tag list and write to output extract files to be processed in CSULB-Data-Transform

Script Order:
1. extract_from_csulb_website.py
2. extract_from_html_assets.py

Results:
- ../CSULB-Data-Transform/assets
- ../CSULB-Data-Transform/assets/SubjectsExtract.txt
- ../CSULB-Data-Transform/assets/CoursesExtract.txt
- ../CSULB-Data-Transform/assets/ClassesExtract.txt
- ../CSULB-Data-Transform/assets/ClassroomsExtract.txt