from .import api

@api.route('/api/hello')
def hello():
    return '<h1>nihao</h1>'

    