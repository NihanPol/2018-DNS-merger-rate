import numpy as np, astropy, scipy
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit
from scipy.misc import factorial

import dosurvey, populate

#Create a number of populations and see how many 1757-like binaries we would detect

log_p_1102 = np.log10(27.28500685)
log_p_1946 = 1.2278867046136734
log_p_0737A = 1.3560258571931227
log_p_1757 = 1.3324384599156054
log_p_1534 = 1.5786392099680724
log_p_1913 = 1.7709992051639407
log_p_0737B = 3.4471580313422194

#survey_dict = {'1946': 'PALFA_one_v_older', '0737A': 'PHSURV', '1757': 'HTRU_low_1757', '1534': '1534_survey', '1913': '1913_survey', '0737B': 'PHSURV', '1102': 'PALFA_one_v_older'}

surveys = ['PALFA_one_v_older', 'PHSURV', 'HTRU_low_1757', '1534_survey', 'PMSURV']

pops = np.arange(10, 6000, 100)
runs_of_pop = 100
runs_per_pop = 100

lum_params = [-1.5, 0.94]     #From Bagchi, Lorimer, Jayanth, 2011

detections = np.full((runs_of_pop, runs_per_pop), 0)

model_name = './0737A_z330.model'

for xx, npop in enumerate(pops):
    
    print "On population:{}".format(npop)
    
    for ii in range(runs_of_pop):
        
        pop = populate.generate(npop, pDistPars = [log_p_0737A, 0.0], duty_percent = 27., orbits = False, nostdout = True, zscale = 0.33, siDistPars=[-1.4, 1.0], lumDistPars = lum_params)
        pop.write(outf = model_name)
        
        for jj in range(runs_per_pop):
            
            population = dosurvey.loadModel(model_name)
            
            output = dosurvey.run(population, surveys, nostdout = True)
            
            detections[ii][jj] = output[0][2].ndet + output[1][2].ndet + output[2][2].ndet + output[3][2].ndet + output[4][2].ndet
            
    filepath = "./pop_result_z330_0737A_varlum/npop={:5d}.npy".format(npop)
    np.save(filepath, detections)
    
print "All Done!"

