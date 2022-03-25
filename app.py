from flask import Flask
from flask_weasyprint import HTML, render_pdf
from flask import render_template , request
from flask import flash, redirect, url_for
from flask_flatpages import FlatPages
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_MARKDOWN_EXTENSIONS = ['extra']
FLATPAGES_EXTENSION_CONFIGS = {
    'codehilite': {
        'linenums': 'True'
    }
}

UPLOAD_FOLDER = 'pages/'
ALLOWED_EXTENSIONS = {'md', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config.from_object(__name__)




#Markdown(app, extensions=['tables','fenced_code'])

pages = FlatPages(app)
pages.get('foo')


@app.route('/')
def index():
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=True,key=lambda p: p.meta['published'])
    return render_template('text.html', articles=latest) 


@app.route('/<path:path>/')
def pdfExportsingle(path):
    page = pages.get_or_404(path)
    html =  render_template('single.html', page=page) 
    return render_pdf(HTML(string=html))


@app.route('/pdf')
def pdfExport():
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=False,key=lambda p: p.meta['published'])
    html =  render_template('text.html', articles=latest) 
    return render_pdf(HTML(string=html))

       
 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
