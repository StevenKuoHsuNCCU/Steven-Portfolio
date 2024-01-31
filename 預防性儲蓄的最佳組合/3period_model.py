from scipy.optimize import minimize
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import sympy as sy
import scipy.integrate as integrate




def normal_distribution_probability(x, mean, std):
    
    return (1/((2*std*np.pi)**0.5))*np.exp((-(x-mean)**2)/(2*std))


#def calculate_prob(mean, std, lower_bound, upper_bound):
    
    f = lambda x : normal_distribution_probability(x = x, mean= mean, std= std)
    
    return  integrate.quad(f, lower_bound , upper_bound)[0]



def period_23_expected_value( b1, cnt2, cnt3 ,beta, alpha, yt2, yt3,  ynt2, r, r1, r2, T, theta, phi_mean, phi_std):
    
    IR = (1+r)*T
    
    
    ct2 = (1/(1+beta))*(yt2 + (1+r1)*b1 +((yt3 + IR)/(1+r2)))
    ct3 = (beta/(1+beta))*(yt2*(1+r2)+ (1+r1)*(1+r2)*b1 + yt3 + IR)
    b2 =  (ct3 - yt3 - IR)/ (1+r2)
    p2 = (ct2*(1-alpha))/ (cnt2* alpha)
    
    phi_limit = (-theta*IR)/ (yt2 + p2*ynt2)
    phi_star = (-b2 - theta*IR) / (yt2 + p2*ynt2)
    
    
    
    

    f0 = lambda x : ((     beta*np.log(((yt2 + (1+r1)*b1 )**alpha)*(cnt2**(1-alpha))) +         beta*beta*np.log((((yt3  + IR))**alpha)*((cnt3)**(1-alpha)))) * normal_distribution_probability(x = x, mean=phi_mean, std= phi_std))

    
    f1 = lambda x : ((     beta*np.log(((yt2 + (1+r1)*b1 + x*(yt2 + p2*ynt2) +theta*IR)**alpha)*(cnt2**(1-alpha))) +             beta*beta*np.log((((yt3 - (1+r2)*(x*(yt2 + p2*ynt2) +theta*IR) + IR))**alpha)*((cnt3)**(1-alpha)))) * normal_distribution_probability(x = x, mean=phi_mean, std= phi_std))
    
    f2 = lambda x : ((     beta*np.log((((1/(1+beta))*(yt2 + (1+r1)*b1 +((yt3 + IR)/(1+r2))))**alpha)*(cnt2**(1-alpha))) +             beta*beta*np.log((((beta/(1+beta))*(yt2*(1+r2)+ (1+r1)*(1+r2)*b1 + yt3 + IR))**alpha)*(cnt3**(1-alpha)))) * normal_distribution_probability(x = x, mean=phi_mean, std= phi_std))
    
    
    
    
    
    
    expected_value =  (integrate.quad(f0, -np.inf , phi_limit)[0] + integrate.quad(f1, phi_limit , phi_star)[0] + integrate.quad(f2, phi_star, np.inf)[0])
    
    return expected_value





def objective_function(x, beta, alpha, yt2, yt3, ynt1, ynt2, ynt3, r, r1, r2, T, theta, phi_mean, phi_std):    
    ct1, b1 = x
    
    cnt1 = ynt1
    cnt2 = ynt2
    cnt3 = ynt3
    
    
    
    



    expected_value = period_23_expected_value( b1 = b1,
                                                cnt2 = cnt2,
                                                cnt3 = cnt3 ,
                                                beta = beta,
                                                alpha = alpha,
                                                yt2 = yt2,
                                                yt3 = yt3,
                                                ynt2 = ynt2,
                                                r = r, r1 = r1, r2 = r2,
                                                T = T, theta = theta, phi_mean = phi_mean, phi_std = phi_std)
    
    
    return -np.log((ct1**alpha)*(cnt1**(1-alpha))) - expected_value


def constraint_function(x, yt1, b0):
    ct1, b1  = x
    
    return  yt1 - ct1 - b1 + b0


def max(beta, alpha, yt1, yt2, yt3, ynt1, ynt2, ynt3, r, r1, r2, b0, T, theta, phi_mean, phi_std, ct1_bound, b1_bound):

    # Define the initial guess for c1 and c2
    x0 = np.array([yt1, 0])

    # Define the bounds for c1 and c2
    bounds = [ct1_bound, b1_bound]

    # Define the constraint
    constraint = {'type': 'ineq', 'fun': constraint_function, 'args': (yt1, b0)}

    # Solve the optimization problem
    result = minimize(lambda x: objective_function(x, beta, alpha, yt2, yt3, ynt1, ynt2, ynt3, r, r1, r2, T, theta, phi_mean, phi_std), x0, method='SLSQP', bounds=bounds, constraints=[constraint])
    
    data = dict()
    
    data["ct1"] = result.x[0]
    data["b1"] = result.x[1]
    
    data["max"] = - result.fun
    
    return data




data = max(beta = 0.98, alpha =0.5, yt1 = 10, yt2 = 20, yt3 = 30, ynt1 = 10, ynt2 = 10, ynt3 = 10, r = 0.01
           , r1 = 0.01, r2 = 0.01, b0 = 1, T = 1, theta = 1, phi_mean = 0.8, phi_std = 1
           , ct1_bound = (0, np.inf), b1_bound = (-np.inf, np.inf))
    
    
print(" Ct1 : ", data["ct1"])
print(" b1 : ", data["b1"])
print(" Max : ", data["max"])

    
    

























