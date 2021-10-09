from flask import (
    Blueprint
)

from durak.routes.middlewares import required_fields

bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/search', methods=['POST'])
def login_route():
    pass
