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
SOURCE_DIR = '/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/source'
sys.path.append(SOURCE_DIR)
import experiment

def kill_matlab():
    user = getpass.getuser()
    process_names = [
        "MATLAB",
        "MATLAB_maci64",
        "MathWorksServiceHost",
        "CrashReporter"
    ]
    for name in process_names:
        subprocess.call(["pkill", "-u", user, "-f", name])
    # pass

kill_matlab()
print('Waiting for 7 seconds')
time.sleep(7)

# ## ----------------------- 10MW -----------------------
# print('----------------------- 10MW -----------------------')
# # Set base path for log/output - adjust as needed
# base_path = "/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/10MW/results/annulus"

# # Construct the log file path
# log_path = os.path.join(base_path, "search_log.txt")

# # Open the log file for writing
# log_file = open(log_path, 'w')

# # Redirect stdout to the log file
# sys.stdout = log_file

# experiment.run_experiment_file('/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/induction/annulus/10MW/10MW_annulus.py')

# kill_matlab()

# sys.stdout = sys.__stdout__
# log_file.close()

# # Now print the final message to the screen
# print(f'Log file written to : {log_path}')
# print('Waiting for 7 seconds')
# time.sleep(7)

# ## ----------------------- 15MW -----------------------

# print('----------------------- 15MW -----------------------')
# base_path = "/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/15MW/results/rotor"
# log_path = os.path.join(base_path, "search_log.txt")
# log_file = open(log_path, 'w')
# sys.stdout = log_file
# experiment.run_experiment_file('/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/induction/rotor/15MW/15MW_rotor.py')
# kill_matlab()
# sys.stdout = sys.__stdout__
# log_file.close()
# print(f'Log file written to : {log_path}')
# print('Waiting for 7 seconds')
# time.sleep(7)

# ## ----------------------- 22MW -----------------------

# print('----------------------- 22MW -----------------------')
# base_path = "/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/22MW/results/rotor"
# log_path = os.path.join(base_path, "search_log.txt")
# log_file = open(log_path, 'w')
# sys.stdout = log_file
# experiment.run_experiment_file('/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/induction/rotor/22MW/22MW_rotor.py')
# kill_matlab()
# sys.stdout = sys.__stdout__
# log_file.close()
# print(f'Log file written to : {log_path}')
# print('Waiting for 7 seconds')
# time.sleep(7)

# ## ----------------------- ALL -----------------------

print('----------------------- ALL -----------------------')
base_path = "/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/all_turbines/results/annulus"
log_path = os.path.join(base_path, "search_log.txt")
log_file = open(log_path, 'w')
sys.stdout = log_file
experiment.run_experiment_file('/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/gp-structure-search/induction/annulus/all_turbines/all_rotor.py')
kill_matlab()
sys.stdout = sys.__stdout__
log_file.close()
print(f'Log file written to : {log_path}')