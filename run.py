import logging
import os
import time

from game import Game

if __name__ == "__main__":
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    
    logging.basicConfig(filename=os.path.join("logs", time.strftime("%Y_%m_%d-%I_%M_%S.log")), level=logging.DEBUG, format="(%(levelname)s) %(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    game = Game()
