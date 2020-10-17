#!/bin/bash

scp -v -r -i $1 ./tools $2@$3:~/

