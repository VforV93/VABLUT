# Intelligent Agent for the [AI @ Unibo Competition](http://ai.unibo.it/games/boardgamecompetition/tablut/1819INF)
VABLUT project made for the AI competition - Master Degree in Computer Engineering - Bologna 2018-2019

Instructions to install the Vablut Agent
required packages:
- python 3.5.# o higher
[
    sudo apt update
    sudo apt install python3-pip
    pip3 --version  #pip 9.0.1 ... (python 3.5)
]
- pip3

in TABBRUTT folder:
- pip3 install -r requirements.txt
- pip3 install pytest
- py.test

Instructions to use the Vablut Agent
This project doesn't include any web interface, the Server project is possible to download here: https://github.com/AGalassi/TablutCompetition.git
- Download the java Server project and open it in eclipse(or similar)
- Run the Server.java(more information about the server's execution in the github project description)
- Run the Human.java agent

- Run the Vablut AI
    - python/python3 tabbrutt.py black|white [max_sec_mossa=60 max_thread=4 verbose=False]
[
	es: python3 tabbrutt.py black|white 60 4 False|True
]
