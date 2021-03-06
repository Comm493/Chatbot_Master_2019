import os
from watson_developer_cloud import ConversationV1
from flask import Flask, jsonify, jsonify, request, render_template

conversation = ConversationV1(
    username= '689b2bd7-c415-456f-89c3-85ace7763659',
    password= 'yRwAQIN0QbGo',
    version= '2017-05-26'
)
workspace_id = 'c2a34f87-d36b-45f5-b4b2-bae20b484c81'

app = Flask(__name__)

global context
context = {}

@app.route('/')
def Welcome():
    return app.send_static_file('webpage.html')

@app.route('/conversation', methods=['GET', 'POST'])
def manage_conversation():
    global context

    if request.method == 'GET':
        return render_template('conversation.html')

    if "message" not in request.form or len(request.form["message"]) <= 0:
        return jsonify({'message': 'No message was provided.'}), 400

    message_response = conversation.message(workspace_id = workspace_id, 
    message_input = {'text': request.form['message']}, context=context)
    context = message_response["context"]

    return jsonify(message_response)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
