pyenv shell 3.14
python -m venv .venv
source .venv/bin/activate.fish
pip install pipenv
pipenv install --dev
#docker-compose up -d
#docker-compose up -d es db cache mq
docker-services-cli up --db postgresql --search opensearch2
./run-tests.sh

    $ ./scripts/bootstrap
    $ ./scripts/setup
