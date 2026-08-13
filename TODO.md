# Migration of DB column types to UTC?

https://github.com/inveniosoftware/invenio-records/commit/13c7fb05bd4ad039a0c4c549791faeb307adbd6b
https://github.com/inveniosoftware/invenio-rdm-records/commit/63cdadb69962570af2ed5c57557dcabd4b072ba5
https://github.com/inveniosoftware/invenio-github/commit/1975f431986610adcb484f3c6b6c5909ab8562e4

# CI snippets



install:
  - "./scripts/bootstrap --ci"


# TODO: docker-compose with a DASH?

#docker-services-cli up --db postgresql --search opensearch2
./run-tests.sh

    $ ./scripts/bootstrap
    $ ./scripts/setup






      - name: Install uv
        uses: astral-sh/setup-uv@v8.2.0
        with:
          python-version: ${{ matrix.python-version }}
          enable-cache: true
          activate-environment: true

      - name: Pre-install
        uses: ./.github/actions/pre-install
        if: ${{ hashFiles('.github/actions/pre-install/action.yml') != '' }}

      - name: Install dependencies
        run: |
          uv pip install ".[$EXTRAS]"
          #uv sync --locked
          uv pip list
          docker version

  # Start docker services
  - "docker-compose up -d es db cache mq"
  - "travis_retry pip install --upgrade pip setuptools py pipenv"
  - "travis_retry pip install twine wheel coveralls"
  - "travis_retry pip install -U numpy"

install:
  - "./scripts/bootstrap --ci"
  # Output installed packages
  - "pipenv lock --requirements"

before_script:
  # Allow services running inside docker to start
  - "./docker/wait-for-services.sh"

script:
  - ./run-tests.sh