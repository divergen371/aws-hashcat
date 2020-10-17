#!/bin/bash

scp -i ~/.ssh/AWS-Hashcat.pem -r ./tools $1@$2
