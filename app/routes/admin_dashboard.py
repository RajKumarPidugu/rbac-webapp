from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_dash = Blueprint('admin_dash', __name__)

@admin_dash.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return "Unauthorized", 403
    return render_template('admin_dashboard.html')
