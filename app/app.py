import os

from flask import Flask
import elasticapm
from elasticapm.contrib.flask import ElasticAPM
from dotenv import load_dotenv

from . import data

load_dotenv()

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': os.environ['SERVICE_NAME'],
  'SECRET_TOKEN': os.environ['SECRET_TOKEN'],
  'SERVER_URL': os.environ['SERVER_URL'],
  'ENVIRONMENT': os.environ['ENVIRONMENT'],
}

apm = ElasticAPM(app)


@app.route('/')
@elasticapm.capture_span()
def hello_world():
    return data.return_check()


if __name__ == '__main__':
    app.run(debug=True, port=6062)
