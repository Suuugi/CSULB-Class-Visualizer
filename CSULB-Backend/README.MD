Requirements:
- python3
- virtualenv
- requests
- beautifulsoup4
- psycopg2

Execution Order:
1. Install venv: pip install virtualenv
2. Create venv for backend: python -m venv venv
3. Update Execution Policy for venv = Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
4. Enable Virtual Environment = <path>\CSULB-Class-Visualizer\CSULB-Backend\venv\Scripts\Activate.ps1
5. Install Virtual Environment = pip install -r <path>\CSULB-Class-Visualizer\CSULB-Backend\requirements.txt
6. CSULB-Classes-Scraper/extract_from_csulb_website.py
7. CSULB-Classes-Scraper/extract_from_html_assets.py