from flask import Flask
from flask_weasyprint import HTML, render_pdf
from flask import render_template
from flask_flatpages import FlatPages
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



app.config.from_object(__name__)




#Markdown(app, extensions=['tables','fenced_code'])

pages = FlatPages(app)
pages.get('foo')


@app.route('/')
def index():
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=True,key=lambda p: p.meta['published'])
    return render_template('text.html', articles=latest) 



@app.route('/pdf')
def pdfExport():
    articles = (p for p in pages if 'published' in p.meta)
    latest = sorted(articles, reverse=False,key=lambda p: p.meta['published'])
    html =  render_template('text.html', articles=latest) 
    return render_pdf(HTML(string=html))

        
