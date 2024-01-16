import elasticapm


@elasticapm.capture_span()
def return_check():
    return b'Hello World!'
