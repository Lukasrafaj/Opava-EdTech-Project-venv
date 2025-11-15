# website/lang.py

from flask import Blueprint, redirect, request, session, current_app
from flask_login import login_required, current_user
from . import db

lang_bp = Blueprint('lang', __name__)


@lang_bp.route('/set_language/<lang>')
def set_language(lang):
    """Store selected language in session and redirect back to previous page."""

    supported = current_app.config.get("LANGUAGES", {}).keys()

    # If language is not supported → do nothing
    if lang not in supported:
        return redirect(request.referrer or '/')

    # Store into session
    session["lang"] = lang
    if current_user.is_authenticated:
        current_user.lang = lang
        db.session.add(current_user)
        db.session.commit()


    print(f"🌐 Language switched to: {lang}")

    # Redirect back to previous page, fallback to home
    return redirect(request.referrer or '/')



