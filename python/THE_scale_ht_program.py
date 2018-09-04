import numpy as np, scipy
import matplotlib.pyplot as pl
import pandas as pd

import populate, dosurvey
import plot_conf_int

surveys = ['PALFA_one_v_older', 'PHSURV', 'HTRU_low_1757', 'AODRIFT', 'GBNCC', 'PMSURV', '1534_survey']
npop = 200    #10 times the current population
model_name = './dns_zdist.model'

n_runs = 100
zscale = np.arange(0.1, 2.1, 0.1)

op_z_hts = np.full(len(zscale), 0.0)
err_z_hts = np.full(len(zscale), 0.0)
op_dm_signb = np.full(len(zscale), 0.0)
err_dm_signb = np.full(len(zscale), 0.0)


for jj, zzscale in enumerate(zscale):
    
    print "On run:", jj
    
    mean_z_hts = np.full(n_runs, 0.0)
    mean_z_hts_err = np.full(n_runs, 0.0)
    mean_dm_singb = np.full(n_runs, 0.0)
    mean_dm_singb_err = np.full(n_runs, 0.0)
    
    for ii in range(n_runs):
        
        #Make sure to change the zscale!
        pop = populate.generate(npop, pDistType = 'unif', surveyList = surveys, pDistPars = [15, 70], orbits = False, nostdout = True, zscale = zzscale, siDistPars=[-1.4, 1.0])
        
        #I set the allsurveyfile = True to combine detected PSR properties into single numpy array
        op = dosurvey.run(pop, surveys, nostdout = True, allsurveyfile = True)
        
        #Here I make use of the allsurveyfile, i.e. op[3]
        mean_z_hts[ii] = np.nanmedian(np.abs(op[-1][1].make_plotting_dicts()[1]['Gal Z']))
        mean_z_hts_err[ii] = np.std(np.abs(op[-1][1].make_plotting_dicts()[1]['Gal Z'])) / np.sqrt(npop)
        mean_dm_singb[ii] = np.nanmedian(op[-1][1].make_plotting_dicts()[1]['DM'] * np.abs(np.sin(op[-1][1].make_plotting_dicts()[1]['gb'] * np.pi / 180.)))
        mean_dm_singb_err[ii] = np.std(op[-1][1].make_plotting_dicts()[1]['DM'] * np.abs(np.sin(op[-1][1].make_plotting_dicts()[1]['gb'] * np.pi / 180.))) / np.sqrt(npop)
        
    op_z_hts[jj] = np.nanmedian(mean_z_hts)
    err_z_hts[jj] = np.nanmedian(mean_z_hts_err)
    
    op_dm_signb[jj] = np.nanmedian(mean_dm_singb)
    err_dm_signb[jj] = np.nanmedian(mean_dm_singb_err)



filename1 = "z_ht.npy"
np.save(filename1, op_z_hts)
filename2 = "z_ht_err.npy"
np.save(filename2, err_z_hts)
filename3 = "dm_signb.npy"
np.save(filename3, op_dm_signb)
filename4 = 'dm_signb_err.npy'
np.save(filename4, err_dm_signb)
