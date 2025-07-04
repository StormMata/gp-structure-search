"""
This file quickly demonstrates some of the capabilities of the project. 

@authors: David Duvenaud (dkd23@cam.ac.uk)
          James Robert Lloyd (jrl44@cam.ac.uk)
          Roger Grosse (rgrosse@mit.edu)
          
Created April 2013          
"""

import experiment
import postprocessing

experiment.run_experiment_file('../examples/fast_example.py')

# To see the outcome of this experiment, look in examples/01-airline_result.txt

postprocessing.make_all_1d_figures(folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', save_folder='/scratch/09909/smata/induction_modeling/gaussian_process/gp_test/', rescale=False)
    
