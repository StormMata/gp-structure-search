# An example experiment that will take a while, but will probably find a good solution.

Experiment(description='10MW turbine data in rotor-average form',
           data_dir='/scratch/09909/smata/induction_modeling/gaussian_process/rotor/10MW/train_data/wrf_10MW_rot.mat',
           results_dir='/scratch/09909/smata/induction_modeling/gaussian_process/rotor/10MW/results/',
           max_depth=10,                # How deep to run the search.
           k=1,                         # Keep the k best kernels at every iteration.  1 => greedy search.
           n_rand=3,                    # Number of random restarts.
           iters=100,                   # How long to optimize hyperparameters for.
           base_kernels='SE,Per,Lin',
           verbose=True,
           make_predictions=False,
           skip_complete=True)