FROM ubuntu:20.04
CMD touch /host-base/y ; echo "(.${MY_ENV_VAR}.)" ; for x in 1 2 3 4 5; do echo $x; sleep 1; done
