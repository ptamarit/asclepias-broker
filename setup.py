# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (c) 2017 Thomas P. Robitaille.
#
# Asclepias Broker is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Scholarly link broker for the Asclepias project."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('asclepias_broker', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='asclepias-broker',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='scholarly link broker',
    license='MIT',
    author='CERN, Thomas Robitaille',
    author_email='info@inveniosoftware.org',
    url='https://github.com/asclepias/asclepias-broker',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'asclepias-broker = invenio_app.cli:cli',
        ],
        'flask.commands': [
            'metadata = asclepias_broker.metadata.cli:metadata',
            'events = asclepias_broker.events.cli:events',
            'search = asclepias_broker.search.cli:search',
            'harvester = asclepias_broker.harvester.cli:harvester',
            'monitor = asclepias_broker.monitoring.cli:monitor',
        ],
        'invenio_config.module': [
            'asclepias_broker = asclepias_broker.config',
        ],
        'invenio_base.apps': [
            # Not enabling flask-breadcrumbs to avoid the following error when starting uswgi:
            # ERROR in app: Failed to initialize entry point: invenio_theme = invenio_theme:InvenioTheme
            # Traceback (most recent call last):
            #   File "/usr/local/lib/python3.8/site-packages/invenio_app/wsgi.py", line 13, in <module>
            #     application = create_app()
            #   File "/usr/local/lib/python3.8/site-packages/invenio_base/app.py", line 110, in _create_app
            #     app_loader(
            #   File "/usr/local/lib/python3.8/site-packages/invenio_base/app.py", line 173, in app_loader
            #     _loader(app, lambda ext: ext(app), entry_points=entry_points,
            #   File "/usr/local/lib/python3.8/site-packages/invenio_base/app.py", line 233, in _loader
            #     init_func(ep.load())
            #   File "/usr/local/lib/python3.8/site-packages/invenio_base/app.py", line 173, in <lambda>
            #     _loader(app, lambda ext: ext(app), entry_points=entry_points,
            #   File "/usr/local/lib/python3.8/site-packages/invenio_theme/ext.py", line 37, in __init__
            #     self.init_app(app, **kwargs)
            #   File "/usr/local/lib/python3.8/site-packages/invenio_theme/ext.py", line 47, in init_app
            #     self.menu_ext.init_app(app)
            #   File "/usr/local/lib/python3.8/site-packages/flask_menu/__init__.py", line 51, in init_app
            #     raise RuntimeError("Flask application is already initialized.")
            # RuntimeError: Flask application is already initialized.

            # 'flask_breadcrumbs = flask_breadcrumbs:Breadcrumbs',
            ('asclepias_harvester = '
             'asclepias_broker.harvester.ext:AsclepiasHarvester'),
        ],
        'invenio_base.api_apps': [
            # TODO: Fix this in Flask-Menu/Breadcrumbs (i.e. make it possible
            # to skip menus/breadcrumbs registration if the extensions aare not
            # loaded/enabled...)
            'flask_breadcrumbs = flask_breadcrumbs:Breadcrumbs',
            ('asclepias_harvester = '
             'asclepias_broker.harvester.ext:AsclepiasHarvester'),
        ],
        'invenio_base.api_blueprints': [
            ('asclepias_broker_events = '
             'asclepias_broker.events.views:blueprint'),
            ('asclepias_broker_search = '
             'asclepias_broker.search.views:blueprint'),
        ],
        'invenio_celery.tasks': [
            'asclepias_broker_graph_tasks = asclepias_broker.graph.tasks',
            'asclepias_broker_search_tasks = asclepias_broker.search.tasks',
            'asclepias_harvester_tasks = asclepias_broker.harvester.tasks',
            'asclepias_monitoring_tasks = asclepias_broker.monitoring.tasks'
        ],
        'invenio_db.models': [
            'asclepias_broker_core = asclepias_broker.core.models',
            'asclepias_broker_events = asclepias_broker.events.models',
            'asclepias_broker_graph = asclepias_broker.graph.models',
            'asclepias_broker_metadata = asclepias_broker.metadata.models',
        ],
        'invenio_pidstore.fetchers': [
            'relid = asclepias_broker.pidstore:relid_fetcher',
            'meta = asclepias_broker.pidstore:relid_fetcher',
        ],
        'invenio_pidstore.minters': [
            'relid = asclepias_broker.pidstore:relid_minter',
            'meta = asclepias_broker.pidstore:relid_minter',
        ],
        'invenio_search.mappings': [
            'relationships = asclepias_broker.mappings',
        ],
        'invenio_queues.queues': [
            ('asclepias_harvester_queues = '
             'asclepias_broker.harvester.queues:declare_queues'),
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
