from . import *
from models.words import Words

main = Blueprint('index', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/', methods=['POST'])
def events_search():
    blacklist = Words.read_list()
    text = request.form.get('text', '')
    old = request.form.get('text', '')
    check = "<span class='label label-success'>通过</span>"
    for i in blacklist:
        if i in text:
            check = "<span class='label label-danger'>未通过</span>"
            new = "<span style='background-color:red; color:white;'>{}</span>".format(i)
            text = text.replace(i, new)
    return render_template('index.html', text=text, check=check, old=old)


@main.route('/word')
def word():
    return render_template('index.html')
