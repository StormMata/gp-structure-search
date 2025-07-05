"""
This file quickly demonstrates some of the capabilities of the project. 

@authors: David Duvenaud (dkd23@cam.ac.uk)
          James Robert Lloyd (jrl44@cam.ac.uk)
          Roger Grosse (rgrosse@mit.edu)
          
Created April 2013          
"""

import experiment
import postprocessing
import sys
import os

# Set base path for log/output - adjust as needed
base_path = "/Users/stormmata/Downloads/gp_results_temp"

# Construct the log file path
log_path = os.path.join(base_path, "search_log.txt")

# Open the log file for writing
log_file = open(log_path, 'w')

# Redirect stdout to the log file
sys.stdout = log_file

experiment.run_experiment_file('../examples/fast_example.py')

# To see the outcome of this experiment, look in examples/01-airline_result.txt

# postprocessing.make_all_1d_figures(folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', save_folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', rescale=False)
    
sys.stdout = sys.__stdout__
log_file.close()

# Now print the final message to the screen
print(f'Log file written to : {log_path}')