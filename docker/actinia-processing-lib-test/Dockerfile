# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest

ENV ACTINIA_CUSTOM_TEST_CFG=/etc/default/actinia-processing-lib-test
# TODO do not set DEFAULT_CONFIG_PATH if this is fixed
ENV DEFAULT_CONFIG_PATH=/etc/default/actinia-processing-lib-test

# hadolint ignore=DL3018
RUN apk add valkey
RUN pip3 install --no-cache-dir \
    iniconfig==2.0.0 pytest==8.3.5 pytest-cov==6.0.0

RUN grass -c EPSG:3358 /actinia_core/userdata/user/nc_spm_08 --text

# copy needed files and configs for test
COPY docker/actinia-processing-lib-test/actinia-processing-lib-test.cfg /etc/default/actinia
COPY docker/actinia-processing-lib-test/actinia-processing-lib-test.cfg /etc/default/actinia-processing-lib-test
COPY . /src/actinia-processing-lib/

WORKDIR /src/actinia-processing-lib/
RUN pip3 install --no-cache-dir -e .

# RUN make test
