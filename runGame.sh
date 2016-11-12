#!/bin/bash
make clean
./halite -d "10 10" "python3 MyBot.py" "python3 RandomBot.py" > log-script.log
