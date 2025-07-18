#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=104
#SBATCH --time=16:00:00
#SBATCH -J 10MW_rotor_D5
#SBATCH --account=TG-ATM170028
#SBATCH -p spr
#SBATCH --mail-type=ALL
#SBATCH --mail-user=storm@mit.edu

module load matlab

conda run --no-capture-output -n gp_search_py3 python3 run_D5.py
