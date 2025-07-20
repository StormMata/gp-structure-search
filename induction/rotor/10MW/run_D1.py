"""
This file quickly demonstrates some of the capabilities of the project. 

@authors: David Duvenaud (dkd23@cam.ac.uk)
          James Robert Lloyd (jrl44@cam.ac.uk)
          Roger Grosse (rgrosse@mit.edu)
          
Created April 2013          
"""
import sys
import os
import getpass
import subprocess
import platform
import time

# Add the path to the directory containing experiment.py
# SOURCE_DIR = '/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/source'
SOURCE_DIR = '/work2/09909/smata/stampede3/gp-structure-search/source'
sys.path.append(SOURCE_DIR)
import experiment

case = 'D1'

print('----------------------- 10MW -----------------------')
# Set base path for log/output - adjust as needed
# base_path = "/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/10MW/results/rotor"
base_path = "/scratch/09909/smata/induction_modeling/gaussian_process/10MW/results/rotor"

# Construct the log file path
log_path = os.path.join(base_path,  f'{case}_search_log.txt')

# Open the log file for writing
log_file = open(log_path, 'w')

# Redirect stdout to the log file
sys.stdout = log_file

# experiment.run_experiment_file('/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/induction/rotor/10MW/10MW_rotor.py')
experiment.run_experiment_file(f'/work2/09909/smata/stampede3/gp-structure-search/induction/rotor/10MW/10MW_{case}_rotor.py', case)

sys.stdout = sys.__stdout__
log_file.close()

# Now print the final message to the screen
print(f'Log file written to : {log_path}')