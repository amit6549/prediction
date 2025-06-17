#!/bin/bash

# Navigate to bot directory
cd /root/tashan_bot

# Run the bot and broadcast loop in background with logging
nohup python3 bot.py > bot.log 2>&1 &
nohup python3 broadcast_loop.py > broadcast.log 2>&1 &
