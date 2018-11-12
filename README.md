# flask_demo
Flask Demo

### install environment
```
$ virtualenv venv_api
$ source venv_api/bin/activate
$ cd flask_demo
$ pip install -r requirements.txt
```

### command line
```
$ cd flask_demo
$ python manage.py run -h 127.0.0.1 -p 5000

# enable debug with --debugger
$ python manage.py run -h 127.0.0.1 -p 5000 --debugger
```

### use gunicorn
```
$ cd flask_demo
$ gunicorn -b 127.0.0.1:5000 --name=server_api --workers=2 --max-requests=10 --pid=/tmp/gunicorn.pid -D api.wsgi:app
```


