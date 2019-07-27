# gameandmine
Windows Python Script for gamers who wish to mine.

First Nicehash should be installed.
Now considering the mining process will be operating on computer which will be heavily used for gaming, it is required the process is stopped when they are being used for gaming. So a python script will be used to automate the mining process by closing the mining process when a game is being played.

The python script will achieve the following objectives:
1) The mining process is started only when:
A game is not being played ( i.e it is not started)
A game is present in the running process list of Task Manager but the computer is idle for more than 5 minutes ( i.e the game is ON but the nobody is playing it )
2) The mining process will be stopped:
When a new game is started
When the GPU is heavily being used for gaming ( i.e the computer is actively used for gaming )  

