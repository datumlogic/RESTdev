#!/bin/bash  
read -p "Commit description: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push origin master
ssh Administrator@datumlogic.com RESTdev.cmd