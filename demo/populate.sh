#!/bin/bash

set -x

source bin/activate

declare -rg CORE_URL="http://127.0.0.1:8000/"

declare -rg PAYMENT_PATH="payment/"
declare -rg PSP_PATH="payment_service_provider/"
declare -rg PSP_ADAPTER_PATH="psp_adapter/"
declare -rg SAAS_INSTANCE_PATH="saas_instance/"

http --json "${CORE_URL}${PSP_PATH}" fullname="Bank of Africa"
http --json "${CORE_URL}${PSP_PATH}" fullname="Gringots"