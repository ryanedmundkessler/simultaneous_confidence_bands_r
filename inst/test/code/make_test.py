import os, sys, subprocess, shutil

python_lib_path = '../../lib/python/'
shutil.copytree(python_lib_path, './python_lib/')
from python_lib.make_utils import * 

clear_dirs(['../output/'])

run_rbatch(program = 'monte_carlo.R')

shutil.rmtree('python_lib')