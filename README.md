# houseplant-tracker
A web app to track your plant progress, create care schedules, and get help.

## Setup

### Server (Django)
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

### Client App (Vue/Parcel)
Install dependencies
```
npm install
```


## Running

### Server (Django)
Make sure you have sourced the virtual environment for your shell session:
```
source env/bin/activate
```

Run migrations
```
python manage.py migrate
```

Start up django
```
python manage.py runserver
```

### Client App (Vue/Parcel)

Run development server
```
npm run watch
```


## Deploying
