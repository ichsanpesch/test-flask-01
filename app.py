import flask
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/get-json', methods=['POST'])
def getJson():

    if (flask.request.headers.get('content-type') != "application/json"):

        data = {
            "status" : "xxx",
            "message" : "content-type is not allowed"
        }

        Response = flask.Response(json.dumps(data))
        Response.headers['content-type'] = 'application/json'

        app.logger.info(json.dumps(data))
        
        return Response

    Request = flask.request.json

    Response = flask.Response(json.dumps(Request))
    Response.headers['content-type'] = 'application/json'

    app.logger.info(json.dumps(Request))

    return Response

app.run()