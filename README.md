# FLASK2PRINT

simple flask app to generate pdf from markdown file 

## install

as usual 

1. `git clone https://github.com/zvevqx/flask2print.git`
2. `cd flask2print`
3. create a virtual environement 
    - **Linux** / **OSX** with python3 `python -m venv venv
    - **windows** `py -3 -m venv venv`
4. activate venv 
    - **Linux** / **OSX** : `. venv/bin/activate`
    - **windows** : `venv\Scripts\activate`
5. `pip install -r requirements.txt`
6. `flask run`

## usage

- go to `http://localhost:5000` to view all **markdown** files as `html`
- go to `http://localhost:5000/pdf` to generate pdf 
- go to `http://localhost:5000/upload` to upload **markdown** file

 

all the styling is done in `style.css`


