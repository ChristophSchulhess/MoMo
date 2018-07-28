#!/bin/bash

set -x

source bin/activate

declare -rg CORE_URL="http://127.0.0.1:8000/"

declare -rg PSP_PATH="payment_service_provider/"
declare -rg SAAS_INSTANCE_PATH="saas_instance/"

http --json "${CORE_URL}${PSP_PATH}" fullname="Iron Bank of Bravos"
http --json "${CORE_URL}${PSP_PATH}" fullname="Gringots"

http --json "${CORE_URL}${SAAS_INSTANCE_PATH}" \
    fullname="Thomas Edison" \
    url="http://127.0.0.1:8042"
http --json "${CORE_URL}${SAAS_INSTANCE_PATH}" \
    fullname="Nicola Tesla" \
    url="http://127.0.0.1:8043"