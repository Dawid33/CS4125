from flask import Blueprint, render_template


home = Blueprint('home_page', __name__, url_prefix='')

@home.route('/home', methods=['GET', 'POST'])
def load():
    return render_template('home/home.html')
    
    