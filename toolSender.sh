#!/bin/bash

scp -v -r -i $1 ./hashcatTools $2@$3:~/

