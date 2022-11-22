from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  user_input = request.form.get('reflected', '')
  resp = make_response(render_template('index.html', user_input=user_input))
  resp.headers['X-XSS-Protection'] = '0'
  return resp

@app.route('/search/<path:title>')
def search(title):
  resp = make_response(render_template('search.html', title=title))
  resp.headers['X-XSS-Protection'] = '0'
  return resp

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)