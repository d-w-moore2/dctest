FROM ubuntu:20.04
CMD touch /host-base/y ; echo "(.${MY_ENV_VAR}.)" ; tail -f '/dev/null'
