# website/lang.py

from flask import Blueprint, redirect, request, session, current_app

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

    print(f"🌐 Language switched to: {lang}")

    # Redirect back to previous page, fallback to home
    return redirect(request.referrer or '/')
