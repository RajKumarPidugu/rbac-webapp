from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return "Unauthorized", 403
    return render_template('admin_dashboard.html')

@main.route('/user-dashboard')
@login_required
def user_dashboard():
    if current_user.role != 'user':
        return "Unauthorized", 403
    return render_template('user_dashboard.html')
