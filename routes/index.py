from . import *

main = Blueprint('index', __name__)

blacklist = ['赚钱', '无风险', '保本', '保息', '传播', '收益', '交易', '大额投资', '配资', '100%担保', '资金池', '稳赚不亏', ]


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/', methods=['POST'])
def events_search():
    text = request.form.get('text', '')
    old = request.form.get('text', '')
    check = "<span class='label label-success'>通过</span>"
    for i in blacklist:
        if i in text:
            check = "<span class='label label-danger'>未通过</span>"
            new = "<span style='background-color:red; color:white;'>{}</span>".format(i)
            text = text.replace(i, new)
    return render_template('index.html', text=text, check=check, old=old)
