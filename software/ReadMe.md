# Backend Software
----
## Init
- Be sure to do the following to create the virtual env
```
pwd //should be accesspoint/software
virtualenv venv   //creates a virtual environment (the one that is ignored in the .gitignore)
source venv/bin/activate //activates the virtualenv
pip install -r requirements.txt  //installs all of the necessary python dependancies (flask, flask-sqlalchemy, sandman)
```
- Be sure to either create a new database file or use one that was previously created
```
pwd //should be accesspoint/software
python
from app import db
db.create_all()
```
- To start the backend RESTful API
```
sandmandctl sqlite:////<full path to the db file>
```

## Contributing
Please follow the generic branching model for this project.

Branch off of the develop branch and push commits there. No one should be bothering your specific branches. 
Feel free to rebase/force push/ etc on your individual branch.

Once things 'are' working for your specific bug/enhancement/milestone, rebase and merge with develop.
