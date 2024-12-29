from flask import Blueprint
from app.controllers.UserController import index, store

user_bp = Blueprint('user_bp',__name__)
user_bp.route('/',methods=['GET'])(index)
user_bp.route('/create',methods=['POST'])(store)
# user_bp.route('/update/<int:user_id>',method='PUT')(update)
# user_bp.route('/<int:user_id>',method='GET')(show)
# user_bp.route('/delete/<int:user_id>',method='DELETE')(destroy)