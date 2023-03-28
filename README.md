## Initial Setup
<hr>
Download chromedriver and add to any destination on you pc:
https://chromedriver.chromium.org/downloads

Make sure you have Python 3.9 installed

Clone repo and create a virtual environment
```
$ git clone https://github.com/giedriusstankauskas/en_code_fill.git
$ cd en_code_fill
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install -r requirements.txt
```
Change login details and add lvl number in main.py.
<br>
Check comments with "IMPORTANT!" tag to change if needed.
<br>
Do not leave blank lines in the end or middle of codes.txt file.

Run main.py
```
$ (venv) python3 main.py
```