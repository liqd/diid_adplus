# adhocracy+

[adhocracy.plus](https://adhocracy.plus/) is a free Open-Source participation platform maintained and primarily developed by Liquid Democracy e.V.. It is based on [adhocracy 4](https://github.com/liqd/adhocracy4) and [Django](https://github.com/django/django).

![Build Status](https://github.com/liqd/diid-adplus/actions/workflows/django.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/liqd/diid-adplus/badge.svg?branch=main)](https://coveralls.io/github/liqd/diid-adplus?branch=main)

## Getting started

adhocracy+ is designed to make online participation easy and accessible to everyone. It can be used on our SaaS-platform or installed on your own servers. How to get started on our platform is explained [here](https://adhocracy.plus/info/start/).

## Installation for development

### Requirements:

 * nodejs (+ npm)
 * python 3.x (+ venv + pip)
 * libpq (only if postgres should be used)

### Installation:

    git clone https://gitlab.cs.uni-duesseldorf.de/diid/diid_adplus.git
    cd diid_adplus
    make install
    make fixtures

### Start virtual environment:
    source venv/bin/activate

### Check if tests work:

    make test

### Start a local server:
    make watch

### Use postgresql database for testing:
run the following command once:
```
make create-postgres
```
to start the testserver with postgresql, run:
```
export DATABASE=postgresql
make start-postgres
make watch
```

Go to http://localhost:8004/ and login with admin@liqd.net | password

## Installation on a production system

You like adhocracy+ and want to run your own version? An installation guide for production systems can be found [here](./docs/installation_prod.md).

## Contributing or maintaining your own fork

If you found an issue, want to contribute, or would like to add your own features to your own version of adhocracy+, check out [contributing](./docs/contributing.md).

## Security
We care about security. So, if you find any issues concerning security, please send us an email at info [at] liqd [dot] net.
