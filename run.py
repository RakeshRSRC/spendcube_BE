from main_app import create_app
from flask_cors import CORS, cross_origin

app = create_app()
cors = CORS(app)


@app.after_request
# This will be called at the end of every request.
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run(debug=True)