import os.path
from config.config import Config
from flask import Flask, render_template, request
from src.mpd import MPD


class Weatherman:
    config = Config()

    def __init__(self, port=80):
        self.port = port

    def init(self):
        """ Bootstrapping """
        print("init")
        self.initFlask()

    def returnContext(self):
        context = self.config.get('labels').copy()
        context.update({
            'navigation': self.config.get('navigation').copy(),
        })

        return context

    def initFlask(self):
        """ Init Web Layer """
        app = Flask(__name__)

        @app.context_processor
        def utility_processor():

            def current_page_name():
                for link in self.config.get('navigation').copy():
                    if request.path == link.get('url'):
                        return ' - ' + link.get('name')

                return ''

            return dict(
                current_page_name=current_page_name,
            )

        # Home
        @app.route('/')
        def index():
            context = self.returnContext()

            return render_template('content/__index__.html', **context)

        @app.route('/<path:path>')
        def catch_all(path):
            context = self.returnContext()
            fspath = 'content/' + path + '.html'
            if os.path.isfile('./templates/' + fspath):
                return render_template(fspath, **context)
            else:
                return render_template('error.html', **context), 404

        if __name__ == '__main__':
            app.run(debug=True, host='0.0.0.0')


mpd = MPD()

mpd.connect()

mpd.doSomething()

mpd.disconnect()

weatherman = Weatherman()

weatherman.init()
