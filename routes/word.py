from . import *
from models.words import Words
from models.logs import Log

main = Blueprint('word', __name__)


@main.route('/')
def index():
    words = Words.read()
    logs = Log.history()
    return render_template('word.html', words=words, logs=logs)


@main.route('/', methods=['POST'])
def events_search():
    text = request.form.get('text', '')
    # print(request.headers.__dict__)
    form = dict(
        platform=request.user_agent.platform,
        browser=request.user_agent.browser,
        version=request.user_agent.version,
        user_agent=request.user_agent.string,
        ip=request.remote_addr,
        text=text,
    )
    # print(form)
    Log.new(form)
    Words.write(text)
    words = Words.read()
    logs = Log.history()
    return render_template('word.html', words=words, logs=logs)
