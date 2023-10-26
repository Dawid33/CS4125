from flask import Blueprint, render_template, request, url_for, redirect, flash, session, send_from_directory

from . import db

bp = Blueprint('login', __name__, url_prefix="/api")


@bp.route('/register', methods=['POST'])
def register():
    result = {
        "success": False,
    }
    try:
        email = request.form['email']
        password = request.form['password']
        display_name = request.form['display_name']
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Failed while reading post request form data'
        return result

    try:
        db_conn = db.get_db()
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Cannot connect to database'
        return result

    try:
        cursor = db_conn.cursor()
        cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
        possible_user = cursor.fetchone()
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Failed to execute SQL query'
        return result

    if not email:
        result['error'] = 'Email is required.'
    elif not password:
        result['error'] = 'Password is required.'
    elif not display_name:
        result['error'] = 'Display name is required.'
    elif possible_user is not None:
        result['error'] = f"User with email '{email}' is already registered."

    if result.get('error') is None:
        try:
            cursor.execute('INSERT INTO users (display_name, email, password) VALUES (?, ?, ?)',
                           (display_name, email, password))

            cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            db_result = cursor.fetchone()

            result['user_id'] = db_result[0]

            db_conn.commit()
        except Exception as e:
            print(e)
            result['error'] = 'Internal Error: Database request failed, unable to register user'
        result['success'] = True

    return result


@bp.route('/login', methods=['POST'])
def login():
    result = {
        "success": False,
    }
    try:
        email = request.form['email']
        password = request.form['password']
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Failed while reading post request form data'
        return result

    try:
        db_conn = db.get_db()
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Cannot connect to database'
        return result

    try:
        cursor = db_conn.cursor()
        cursor.execute("SELECT password, user_id FROM users WHERE email = ?", (email,))
        db_result = cursor.fetchone()
    except Exception as e:
        print(e)
        result['error'] = 'Internal Error: Failed to execute SQL query'
        return result

    if db_result is None:
        result['error'] = 'Incorrect email or password'
    elif db_result[0] != password:
        result['error'] = 'Incorrect password'

    if result.get('error'):
        result['success'] = False
    else:
        try:
            cursor = db_conn.cursor()
            cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            db_result = cursor.fetchone()

            result['user_id'] = db_result[0]
        except Exception as e:
            print(e)
            result['error'] = 'Internal Error: Failed to execute SQL query'

        result['success'] = True
    return result


