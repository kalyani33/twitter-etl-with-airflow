# twitter-etl-with-airflow
## Project Architecture
<img width="1000" height="500" alt="image" src="https://github.com/kalyani33/twitter-etl-with-airflow/assets/37569003/8c00f673-acd9-43df-899d-033ed661ca25">

## Apache Airflow Installation steps
###  Installation in windows without using Docker,using WSL(Ubuntu)
- Open a command prompt and update wsl with following commands
  ```
  wsl --update
  wsl --install -d ubuntu
  ```
- Now open WSL2 or Ubuntu terminal and run the following commands
  ```
  sudo apt-get update
  sudo apt-get install python-pip
  sudo apt-get install python3-venv
  python3 -m venv airflow-env
  source airflow-env/bin/activate
  nano ~/.bashrc
  #Type the following
  AIRFLOW_HOME=/c/Users/vjadhav/airflow
  #Press Ctrl+S and Ctrl+X to exit the editor
  pip install apache-airflow
  airflow db init
  airflow users create \
      --username admin \
      --password admin  \
      --firstname <YourFirstName> \
      --lastname <YourLastName> \
      --role Admin \
      --email admin@example.com
  airflow webserver --port 8080
  #open one more terminal and run scheduler
  airflow scheduler
  ```
- The Airflow web server will be accessible at http://localhost:8080 in your web browser and log in using the above-created User.
