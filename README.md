# Flask App Template

This is a template of a Flask App that uses NGINX and GUNICORN for deployment.

## Overview

The Flask App Template is designed to provide a starting point for developing web applications using the Flask framework. It includes integration with NGINX and GUNICORN for efficient deployment.

## Features

- Integration with NGINX and GUNICORN
- Simplified structure for easy project initiation
- Use of best practices and recommended plugins

## Getting Started

To get started with this template, follow these steps:

1. Clone the repository.

```bash
git clone https://github.com/adhishthite/flask-app-template
```

2. Navigate to the repository

```bash
cd flask-app-template
```

3. Add the `.env` file for ElasticAPM credentials. (I use Elastic for APM so I have put it there. Modify the `app.py` if you don't want to use the Elastic.)

4. Build the Docker image

```bash
docker build flask-app .
```

[WIP]


## License


## Feedback

I welcome feedback and suggestions. Please feel free to open an issue or submit a pull request.

---

For more information on creating a great README for your programming project, you can visit [Make a README](https://www.makeareadme.com).
