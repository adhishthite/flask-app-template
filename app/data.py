import elasticapm


@elasticapm.capture_span()
def return_check():
    return 'Hello World!'
