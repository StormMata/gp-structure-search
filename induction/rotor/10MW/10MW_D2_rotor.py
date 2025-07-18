# An example experiment that will take a while, but will probably find a good solution.

Experiment( description             = '10MW turbine data in rotor-average form',
            # data_dir                = '/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/10MW/train_data/wrf_10MW_rot.mat',
            # results_dir             = '/Users/stormmata/Library/Mobile Documents/com~apple~CloudDocs/Courses/Research/Code/induction_modeling/gaussian_process/10MW/results/rotor',
            data_dir                = '/scratch/09909/smata/induction_modeling/gaussian_process/10MW/train_data/wrf_10MW_rot.mat',
            results_dir             = '/scratch/09909/smata/induction_modeling/gaussian_process/10MW/results/rotor',
            max_depth               = 2,                    # How deep to run the search.
            random_order            = False,                # Randomize the order of the datasets?
            k                       = 1,                    # Keep the k best kernels at every iteration.  1 => greedy search.
            debug                   = False,
            local_computation       = True,                 # Run experiments locally, or on the cloud.
            n_rand                  = 5,                    # Number of random restarts.
            sd                      = 4,                    # Standard deviation of random restarts.
            make_predictions        = False,                # Whether or not to forecast on a test set.
            skip_complete           = False,                 # Whether to re-run already completed experiments.
            iters                   = 25,                  # How long to optimize hyperparameters for.
            base_kernels            = 'SE,RQ,Per,Lin',
            zero_mean               = True,                # If false, use a constant mean function - cannot be used with the Const kernel
            verbose_results         = False,                 # Whether or not to record all kernels tested
            random_seed             = 0,
            alpha_heuristic         = -2,                   # Minimum alpha value for RQ kernel
            lengthscale_heuristic   = -4.5,                 # Minimum lengthscale
            use_constraints         = True,
            use_min_period          = False,
        )
