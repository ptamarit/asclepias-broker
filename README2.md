pyenv shell 3.14
python -m venv .venv
source .venv/bin/activate.fish
pip install pipenv
pipenv install --dev
# pipenv install --system --dev
docker compose up -d es db cache mq
#docker-services-cli up --db postgresql --search opensearch2
# ./scripts/setup
# ./scripts/bootstrap
#pipenv run pip install -e .
docker/wait-for-services.sh
./run-tests.sh

