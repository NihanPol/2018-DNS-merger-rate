# Future prospects for ground-based gravitational wave detectors --- The Galactic double neutron star merger rate revisited

Hello world!

This GitHub repository is built to hold the code and data generated in the production of the research paper *Future prospects for ground-based gravitational wave detectors --- The Galactic double neutron star merger rate revisited* by Pol, McLaughlin and Lorimer (insert link to paper here). The repo holds the data products generated at every step of the analysis described in the paper, such that the scripts, and especially notebooks, can be directly executed without the need for installing PsrPopPy and starting the analysis from scratch.

To perform a similar analysis from scratch:
1. Download and install the latest version of [PsrPopPy](https://github.com/devanshkv/PsrPopPy2). This repository also has a tutorial and documentation describing how to use the software. 
2. Replace the dosurvey.py file in PsrPopPy2/lib/python with the one provided in this repository. Also add the survey files given in this repo to PsrPopPy2/lib/surveys.
3. If running the same analysis as the above paper, all degradation factors due to Doppler smearing of DNS orbits are already included in the dosurvey.py file.
  - If performing a new analysis, add the new pulsars and their degradation factors as a dictionary as shown in the dosurvey.py file provided in the repo. The scripts to calculate the degradation factors are given [here](https://github.com/NihanPol/SNR_degradation_factor_for_BNS_systems).
4. Run the python script *find_alpha_xxxx.py* for the DNS system whose population you want to generate.
  - If performing a new analysis, generate a python script similar to that shown in *find_alpha_xxxx.py* for your pulsar.
  - **Preferably run these scripts on a node or cluster as they can take some time to execute**.
5. The above python script should produce multiple output .npy files that hold the number of detections of the DNS system. We provide the files generated in our analysis as tar files. Please extract them in the directory from which you want to execute the code. The notebook *calculate_alpha_and_population_numbers.ipynb* can be used to read in these files and calculate lambda, alpha and the detectable population of the DNS system.
  - This process will need to be done for each DNS/BNS system for which this analysis is to be performed.
6. Once alpha and the detectable population are known for every DNS/BNS system, enter them into the appropriate variable in the notebook *calculate_merger_rates.ipynb* to calculate the merger rates, and execute the notebook. This should calculate the merger rates.

The above process provides the workflow for carrying out similar analyses. There are a number of points in this analysis with room for customization, particularly when generating the populations for the different BNS systems. The scripts provided have the parameters fixed to those used in the analysis.

A few additional scripts/notebooks provided here:
1. *KKL_and_KPM_merger_rate_ref.ipynb*: This notebook implements the analytical expressions to calculate the merger rate from two and three DNS systems. See the references in the notebook for their origin.
2. *calculate_spin_down_age_DNS.ipynb*: This notebook calculates the modified spin-down age for BNS systems where the assumptions in defining the characteristic age are not valid.
3. *THE_scale_ht_program.py*: Python script which generates populations of DNS systems towards calculating the vertical scale height of DNS systems in the Galaxy. This discussion is presented in Sec. 2.3 in the paper.
4. *z_scale_distribution.ipynb*: The notebook to analyze the output of the above script and produce the plots shown in Fig. 1 and 2 in the paper.
5. *plot_conf_int.py*: Convenience plotting function.

Please feel free to get in contact with me (nspol@mix.wvu.edu) if you have any questions about the material here or would like to expand the ideas developed here and in this paper.
