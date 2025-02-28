from sys import hexversion
from sqlalchemy.sql.functions import user
from apps.authentication.utils import hash_pass
from apps.home import blueprint
from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.models import ArtistsData
from apps import db


@blueprint.route("/")
def index():

    return render_template(
        "home.html",
        artists=ArtistsData.query.all(),
    )

@blueprint.route("/api/artists")
def api_artists():
    def to_dict(artist):
        """Convert SQLAlchemy object to dictionary for JSON serialization."""
        return {
            "id": artist.id,
            "name": artist.name,
            "email": artist.email,
            "height": artist.height,
            "weight": artist.weight,
            "dob": artist.dob.strftime("%Y-%m-%d"),  # Convert date to string
        }
    
    return jsonify([to_dict(artist) for artist in ArtistsData.query.all()])
