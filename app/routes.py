from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/sign-in')
def sign_in_page():
    return render_template('sign-in.html')

@main_blueprint.route('/sign-up')
def sign_up_page():
    return render_template('sign-up.html')

@main_blueprint.route('/account')
def account_page():
    return render_template('account.html')

@main_blueprint.route('/report')
def report_page():
    return render_template('report.html')

