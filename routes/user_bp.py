from flask import Blueprint
from controllers.UserController import index,store,show, update, destroy

user_bp = Blueprint('user_bp',__name__)
user_bp.route('/',method='GET')(index)
user_bp.route('/create',method='POST')(store)
user_bp.route('/update/<int:user_id>',method='PUT')(update)
user_bp.route('/<int:user_id>',method='GET')(show)
user_bp.route('/delete/<int:user_id>',method='DELETE')(destroy)