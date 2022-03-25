# FLASK2PRINT

simple flask app to generate pdf from markdown file  

https://www.markdownguide.org/cheat-sheet

All images files must be in ***static/img/filename.ext***

## usage

## rendering research data :
 replace `localhost` with `192.168.3.141`

- go to `http://localhost:5000` to view all **markdown** files as `html`
- go to `http://localhost:5000/pdf` to generate pdf 
- go to `http://localhost:5000/upload/` to upload **markdown** file
- go to `http://localhost:5000/NAMEOFYOURFILE` to preview <this> article PDF ( no `.md` at the end in the url) 


## install

as usual 

1. `git clone https://github.com/zvevqx/flask2print.git`
2. `cd flask2print`
3. create a virtual environement 
    - **Linux** / **OSX** with python3 `python -m venv venv`
    - **windows** `py -3 -m venv venv`
4. activate venv 
    - **Linux** / **OSX** : `. venv/bin/activate`
    - **windows** : `venv\Scripts\activate`
5. `pip install -r requirements.txt`
6. `flask run`

 
all the styling is done in `style.css`


