# An example experiment that runs quickly.

Experiment(description='An example experiment',
           data_dir='../data/1d_data/01-airline.mat',
           results_dir='/Users/stormmata/Downloads/gp_results_temp/',
           max_depth=2,                # How deep to run the search.
           k=1,                        # Keep the k best kernels at every iteration.  1 => greedy search.
           n_rand=2,                   # Number of random restarts.
           iters=100,                   # How long to optimize hyperparameters for.
           base_kernels='SE,Per,Lin',
           verbose=False,
           debug=False, 
           make_predictions=False,
           random_seed=0,
           skip_complete=False)