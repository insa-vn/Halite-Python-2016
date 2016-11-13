#!/bin/bash
make clean
./halite -d "30 30" "python3 MyBot.py" "python3 RandomBot.py" > log-script.log
