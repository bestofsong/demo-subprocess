#!/usr/bin/env bash

ID=$1
N=${2:-10}
for ii in `seq 1 $N` ; do
    sleep 1
    echo "$ID: ${ii}s"
done
