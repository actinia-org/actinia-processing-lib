# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest

# pwgen is needed for the tests
RUN pip3 install --no-cache-dir pwgen==0.8.2.post0

COPY docker/actinia.cfg /etc/default/actinia
COPY src /src/actinia-processing-lib/src/
COPY setup.cfg /src/actinia-processing-lib/
COPY setup.py /src/actinia-processing-lib/
COPY requirements.txt /src/actinia-processing-lib/

RUN pip3 install --no-cache-dir -r /src/actinia-processing-lib/requirements.txt && \
    pip3 uninstall actinia-processing-lib.wsgi -y
# SETUPTOOLS_SCM_PRETEND_VERSION is only needed if in the plugin folder is no
# .git folder
ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.0

WORKDIR /src/actinia-processing-lib
RUN pip3 install --no-cache-dir -e .

WORKDIR /src/actinia_core
