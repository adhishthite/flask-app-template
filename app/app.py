from flask import Flask
import elasticapm
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': '',
  'SECRET_TOKEN': '',
  'SERVER_URL': '',
  'ENVIRONMENT': '',
}

apm = ElasticAPM(app)


@app.route('/get')
@elasticapm.capture_span()
def hello_world():
    return b"Hello World!"


if __name__ == '__main__':
    app.run(debug=True, port=6062)
