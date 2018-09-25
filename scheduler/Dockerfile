FROM python:3.6

ARG AIRFLOW_VERSION=1.10.0

ENV AIRFLOW_HOME=/usr/local/airflow

ENV SLUGIFY_USES_TEXT_UNIDECODE=yes

ENV USER=airflow USER_ID=1001

RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} --uid ${USER_ID} airflow 

RUN pip install --no-cache-dir apache-airflow['crypto','kubernetes','postgres']==${AIRFLOW_VERSION}

COPY ./scripts/entrypoint.sh /entrypoint.sh

RUN chown -R airflow: ${AIRFLOW_HOME}

USER ${USER_ID}
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
