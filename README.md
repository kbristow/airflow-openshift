# Airflow-Openshift
This project provides a basic example which can be used to get [Apache Airflow](https://airflow.apache.org/) running in OpenShift. The provided template will set up an Airflow Scheduler and an Airflow Webserver in an OpenShift project by default running with the `SequentialExecutor`. Further work along the lines of setting up [Celery](http://www.celeryproject.org/) or [RabbitMQ](https://www.rabbitmq.com/) is not included. The setup draws from work done in the [puckel/docker-airflow](https://github.com/puckel/docker-airflow) and [mumoshu/kube-airflow](https://github.com/mumoshu/kube-airflow) projects.

## Instructions 
  1. Create an OpenShift project (`airflow` is the expected default).
  2. Build the Airflow Scheduler and Webserver images locally and push these to your project namespace on your OpenShift registry. The default tag details to use are `airflow-scheduler:latest` and `airflow-webserver:latest` including your project namespace and docker registry address.
  3. Push the Airflow template to your project namespace.
  4. Create a Postgresql db in your project. The following are the defaults to use:
    - Database Service Name: postgres
    - Username: airflow
    - Password: airflow
    - Database Name: airflow
  5. Process the Airflow template targeting your project using the default values or change these values to match the custom values you have chosen.

This will deploy an Airflow Webserver with 1 pod and an Airflow Scheduler with 0 pods. This allows for the Webserver to start up and initialise the database before the Scheduler connects to it. Once the Webserver is up and has initialised the database, you can copy DAG's into the `${AIRFLOW_HOME/dags}` directory in the shared PVC mounted in the Scheduler and Webserver deployments. Scale the Scheduler to 1 pod and the system is ready to process DAG runs. You can access the Webserver dashboard through the route created to in your OpenShift project.