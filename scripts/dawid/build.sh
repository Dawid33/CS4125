
source venv/bin/activate
flask --app dev.py --debug run -p 8080 2>&1 | less -R +F  
