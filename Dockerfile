# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Asclepias Broker is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# Using the latest version of pipenv not requiring setuptools >= 67 to avoid the following runtime bug:
#   pkg_resources._vendor.packaging.requirements.InvalidRequirement:
#   Expected matching RIGHT_PARENTHESIS for LEFT_PARENTHESIS, after version specifier
#   pytz (>dev)
#   https://github.com/pypa/setuptools/issues/3889
RUN pip install pipenv==2023.2.4

RUN pipenv install --deploy --system --ignore-pipfile
ADD . /app
RUN pip install -e .

CMD ["asclepias-broker", "shell"]
