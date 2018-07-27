import os, sys

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PROJ_DIR = os.path.join(TEST_DIR, "..")
sys.path.insert(0, os.path.join(PROJ_DIR, 'src'))
