from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required
from app.models import DBUser

bp = Blueprint('auth', __name__, url_prefix='/auth')

def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_user)
    login_manager.init_app(app)

def load_user(user_id):
    user = DBUser.query.get(user_id)
    return user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')
        if login and password:
            user = DBUser.query.filter_by(login=login).first()
            if user and user.check_password(password):
                login_user(user, remember=remember_me)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
