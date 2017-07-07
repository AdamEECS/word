from . import *
from models.words import Words

main = Blueprint('word', __name__)


@main.route('/')
def index():
    words = Words.read()
    return render_template('word.html', words=words)


@main.route('/', methods=['POST'])
def events_search():
    text = request.form.get('text', '')
    Words.write(text)
    words = Words.read()
    return render_template('word.html', words=words)
