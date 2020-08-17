import numpy as np, scipy, matplotlib
import matplotlib.pyplot as pl

def plot_area_under_curve(x, y, conf_int = 0.95, xlabel = r"$\cal{R}$$_{\rm tot}$ Myr$^{-1}$", ylabel = r'P($\cal{R}$$_{\rm tot}$)', color_fill = 'g', color_line = 'r', color_marker = 'b', label = '', display_conf_lines = True):
    
    #Script to plot the confidence intervals:
    #Calculate 95% limits from the posterior plot
    
    y_norm = y / scipy.integrate.simps(y, x)
    total_area_under_post = scipy.integrate.simps(y_norm, x)
    
    peak_rate = x[np.argmax(y_norm)]
    
    #5 percent of this area:
    percent_5 = (1 - conf_int) * total_area_under_post / 2
    print(percent_5)
    #Integrate starting from R = 0 till we hit 5 percent area and find that value of R
    for ii in range(1, len(y_norm) + 1):

        integral_ll = scipy.integrate.simps(y_norm[: ii], x[: ii])

        if integral_ll >= percent_5:
            lower_limit_ind = ii

            break
            
    lower_limit = x[lower_limit_ind]
    
    reverse_post_R = y_norm[:: -1]
    reverse_possible_R = x[:: -1]

    for ii in range(1, len(reverse_post_R) + 1):

        integral_ul = scipy.integrate.simps(reverse_post_R[: ii], x[: ii])

        if integral_ul >= percent_5:
            upper_limit_ind = len(y_norm) - ii

            break
    
    upper_limit = x[upper_limit_ind]
    
    #print "lower limit: ", peak_rate - lower_limit
    #print "upper limit: ", upper_limit - peak_rate

    pl.plot(x, y_norm, color = color_line, label = label)

    pl.fill_between(x[lower_limit_ind: upper_limit_ind], y_norm[lower_limit_ind: upper_limit_ind], color = color_fill, alpha = 0.2)
    if display_conf_lines:
        pl.axvline(x = lower_limit, ls = '--', color = color_marker, label = r"Lower limit = {:.2f}".format(lower_limit))
        pl.axvline(x = peak_rate, ls = '--', color = color_marker, label = "Peak = {:.2f}".format(peak_rate))
        pl.axvline(x = upper_limit, ls = '--', color = color_marker, label = "Upper limit = {:.2f}".format(upper_limit))

    pl.xlabel(xlabel, fontsize = 22)
    pl.ylabel(ylabel, fontsize = 22)

    pl.legend(loc = 'best')
    #pl.show()
    #return peak_rate, lower_limit, upper_limit