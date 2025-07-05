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

# Open a log file for writing
log_file = open('/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/debug_log.txt', 'w')

# Redirect stdout to the log file
sys.stdout = log_file

experiment.run_experiment_file('../examples/fast_example.py')

# To see the outcome of this experiment, look in examples/01-airline_result.txt

#postprocessing.make_all_1d_figures(folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', save_folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', rescale=False)

sys.stdout = sys.__stdout__
log_file.close()
