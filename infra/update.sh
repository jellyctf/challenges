#!/usr/bin/env bash
cd ~/challenges
git pull
cd
docker compose up --build -d
# dns entries can shuffle around and nginx needs to restart to pick them up
#docker compose restart nginx
