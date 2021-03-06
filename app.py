import logging

from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


def register_routes(app):
    from routes.index import main as routes_index
    from routes.word import main as routes_word
    app.register_blueprint(routes_index, url_prefix='/')
    app.register_blueprint(routes_word, url_prefix='/word')


def register_filters(app):
    from usr_util.filters import filters
    app.jinja_env.filters.update(filters)


def register_errorhandler(app):
    from flask import render_template

    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('error/401.html'), 401

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html'), 404


def configure_app():
    from config import key
    app.secret_key = key.secret_key
    from config.config import config_dict
    app.config.update(config_dict)
    register_routes(app)
    register_filters(app)
    register_errorhandler(app)
    # 设置 log, 否则输出会被 gunicorn 吃掉
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=8005,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_app()
    manager.run()

# (gunicorn wsgi --worker-class=gevent -t 4 -b 0.0.0.0:8000 &)
