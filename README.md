# Airflow-Openshift
This project provides a basic example which can be used to get Airflow running in OpenShift. The provided template will set up an Airflow Scheduler and an Airflow Webserver in an OpenShift project by default running with the `SequentialExecutor`. Further work along the lines of setting up [Celery](http://www.celeryproject.org/) or [RabbitMQ](https://www.rabbitmq.com/) is not included. The setup draws from work done in the [puckel/docker-airflow](https://github.com/puckel/docker-airflow) and [mumoshu/kube-airflow](https://github.com/mumoshu/kube-airflow) projects.

## Instructions 
  1. Create an OpenShift project (`airflow` is the expected default).
  2. Build the Airflow Scheduler and Webserver images locally and push these to your project namespace on your OpenShift registry. The default tag details to use are `airflow-scheduler:latest` and `airflow-webserver:latest`.
  3. Push the Airflow template to your project namespace.
  4. Create a Postgresql db in your project. The following are the defaults to use:
    - Database Service Name: postgres
    - Username: airflow
    - Password: airflow
    - Database Name: airflow
  5. Process the Airflow template targeting your project using the default values or input those that 