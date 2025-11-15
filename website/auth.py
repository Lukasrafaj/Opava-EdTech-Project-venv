from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_babel import gettext, ngettext, lazy_gettext as _l
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_babel import _

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(Email=email).first()

        if user:
            if check_password_hash(user.Password, password):
                flash(gettext('Logged in successfully!'), category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
                
            else:
                flash(gettext('Incorrect password'), category='error')
        else:
            flash(gettext('Email does not exist!'), category='error')
    

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.courses'))


@auth.route('/settings-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword', '').strip()
        newpassword1 = request.form.get('newpassword1', '').strip()
        newpassword2 = request.form.get('newpassword2', '').strip()

        if not oldpassword:
            flash(gettext('Please enter your current password.'), 'error')
        elif not newpassword1 or not newpassword2:
            flash(gettext('Please enter the new password twice.'), 'error')
        elif newpassword1 != newpassword2:
            flash(gettext('New passwords do not match.'), 'error')
        elif len(newpassword1) < 7:
            flash(gettext('New password must be at least 7 characters long.'), 'error')
        elif not current_user.Password:
            flash(gettext('No existing password is set for this account.'), 'error')
        else:
            try:
                if not check_password_hash(current_user.Password, oldpassword):
                    flash(gettext('Current password is incorrect.'), 'error')
                else:
                    current_user.Password = generate_password_hash(newpassword1)
                    db.session.add(current_user)
                    db.session.commit()
                    flash(gettext('Password updated successfully.'), 'success')
                    return redirect(url_for('auth.change_password'))
            except (TypeError, ValueError):
                flash(gettext('Error verifying password. Please try again.'), 'error')

    return render_template('setting_templates/settings-password.html', user=current_user)

@auth.route('/settings-email',methods=['GET', 'POST'])
@login_required
def change_email():
    return render_template('setting_templates/settings-email.html', user=current_user)



@auth.route('/settings-name',methods=['GET', 'POST'])
@login_required
def change_name():
    return render_template('setting_templates/settings-name.html', user=current_user)


@auth.route('/settings-language')
def change_language():
   
    return render_template('setting_templates/settings-language.html')




@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check if user already exists
        existing_user = User.query.filter_by(Email=email).first()

        if existing_user:
            flash(gettext('Email already exists!'), category='error')
        elif len(email) < 4:
            flash(gettext('Email must be greater than 3 characters!'), category='error')
        elif len(name) < 2:
            flash(gettext('Name must greater than 1 character!'), category='error')
        elif password1 != password2:
            flash(gettext('Passwords do not match!'), category='error')
        elif len(password1) < 7:
            flash(gettext('Passwords must contain at least 7 characters!'), category='error')
        else:
            new_user = User(Email = email, Name = name, Password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(gettext('Account created!!'), category='success')
            return redirect(url_for('views.home'))
            


    return render_template('sign_up.html', user = current_user)