from flask import g, render_template, request, jsonify, make_response
from models.user import User

from .provider import create_oauth_provider

def create_oauth_app(app, db):
    oauth = create_oauth_provider(app.app, db)

    @app.app.before_request
    def load_current_user():
        user = User.query.get(1)
        g.user = user

    @app.app.route('/user_management/authorized')
    def authorized():
        code = request.args.get('code')
        return jsonify(code=code)

    @app.app.route('/user_management/oauth/authorize', methods=['GET', 'POST'])
    @oauth.authorize_handler
    def authorize(*args, **kwargs):
        # NOTICE: for real project, you need to require login
        if request.method == 'GET':
            # render a page for user to confirm the authorization
            return render_template('confirm.html')

        if request.method == 'HEAD':
            # if HEAD is supported properly, request parameters like
            # client_id should be validated the same way as for 'GET'
            response = make_response('', 200)
            response.headers['X-Client-ID'] = kwargs.get('client_id')
            return response

        confirm = request.form.get('confirm', 'no')
        return confirm == 'yes'

    @app.app.route('/user_management/oauth/token', methods=['POST', 'GET'])
    @oauth.token_handler
    def access_token():
        return {}

    @app.app.route('/user_management/oauth/revoke', methods=['POST'])
    @oauth.revoke_handler
    def revoke_token():
        pass

    @app.app.route('/user_management/api/email')
    @oauth.require_oauth('email')
    def email_api():
        oauth = request.oauth
        return jsonify(email='me@oauth.net', username=oauth.user.username)

    @app.app.route('/user_management/api/client')
    @oauth.require_oauth()
    def client_api():
        oauth = request.oauth
        return jsonify(client=oauth.client.name)

    @app.app.route('/user_management/api/address/<city>')
    @oauth.require_oauth('address')
    def address_api(city):
        oauth = request.oauth
        return jsonify(address=city, username=oauth.user.username)

    @app.app.route('/user_management/api/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
    @oauth.require_oauth()
    def method_api():
        return jsonify(method=request.method)

    @oauth.invalid_response
    def require_oauth_invalid(req):
        return jsonify(message=req.error_message), 401
    
    return app