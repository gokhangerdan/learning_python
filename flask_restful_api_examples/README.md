### Flask RESTful API Examples

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

> Save this as api.py and run it using your Python interpreter. Note that we’ve enabled Flask debugging mode to provide code reloading and better error messages.

```
$ python api.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```
> Warning:
> Debug mode should never be used in a production environment!

Quote break.
