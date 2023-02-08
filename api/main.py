import sys
from flask import Flask, jsonify, request

app = Flask(__name__)
last_reverse_word = ""

@app.route('/', methods = ['GET'])
def root():
    data = "service is up and running"
    return jsonify({'data': data})


@app.route('/reverse')
def reverse():
    # print('This is error output', file=sys.stderr)
    try:
        global last_reverse_word
        query = request.args.get('in', '')
        result = " ".join(list(reversed(query.split(' '))))
        # app.logger.info(result)
        
        last_reverse_word = result
        return jsonify({'result': result}) 
    except Exception as e:
        return jsonify({'error': str(e)}) 




@app.route('/restore', methods = ['GET'])
def restore():
    # app.logger.info(result)
    global last_reverse_word
    return jsonify({'result': last_reverse_word})


if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0')
