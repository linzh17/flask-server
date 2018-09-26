from .. import api 
from flask import jsonify
from ...service.AuthService import authService

auth = authService()

@api.route('/api/register/<string:username>/<string:password>',methods=['POST'])
def register(username,password):
    auth.userRegister(username,password)
    return jsonify({
        "code":200,
    })
    