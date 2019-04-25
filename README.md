# houseplant-tracker
A web app to track your plant progress, create care schedules, and get help.

## Setup
Create a virtual environment:
```
python -m venv env
```

Source the environment:
```
source env/bin/activate
```

Install dependancies:
```
pip install -r requirements.txt
```

## Running
Make sure you have sourced the virtual environment for your shell session:
```
source env/bin/activate
```

Run watcher
```
npm run watch
``` 

Run migrations
```
python manage.py migrate
```

Start up django
```
python manage.py runserver
```
