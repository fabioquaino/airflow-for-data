This docker compose is a simplified version of Airflow's official docker compose quickstart.

* Install [Docker](https://docs.docker.com/engine/install/) and [Docker-compose](https://docs.docker.com/compose/install/)
* Run `mkdir ./logs ./plugins` to create the necessary folders.
* Run `sudo chmod -R 777 ./logs` to allow the container to write logs on that folder.
* Run `echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" >> .env` to add the appropiate values of Airflow UID and GID to the .env file.
* Run `docker compose up airflow-init` to migrate the metadatabase and create the user to access webserver the UI. (user:airflow, pass:airflow).
* Run `docker compose up -d` to start the scheduler, webserver and the workers in detached mode (this will take some minutes the first time it runs).

