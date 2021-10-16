import numpy as np # Pre-requisite to run numpy
import math

def getMean(val_list):
    val_arr = np.array(val_list)
    
    # print("Return: ", np.sum(val_colMat)/np.size(val_colMat))
    return np.sum(val_arr)/np.size(val_arr)

def getVar(val_list, type_option):
    val_arr = np.array(val_list)
    
    val_mean = getMean(val_list)
    
    if type_option == 0: # Sample Variance
        return np.sum((val_arr -  val_mean)*(val_arr -  val_mean))/(np.size(val_arr) - 1) 
    elif type_option == 1:
        return np.sum((val_arr -  val_mean)*(val_arr -  val_mean))/(np.size(val_arr))
    else:
        print("Error - Option not found")
        return # return nothing

def getStdDev(val_list, type_option):

    var = getVar(val_list, type_option)
    
    if var >= 0:
        return math.sqrt(var)
    elif var < 0:
        return math.sqrt(math.abs(var))
    else:
        print("Error - Option not found")
        return # return nothing
    
def getCoVar(x_val_list, y_val_list, type_option):
    x_val_arr = np.array(x_val_list)
    y_val_arr = np.array(y_val_list)
    
    x_val_mean = getMean(x_val_list)
    y_val_mean = getMean(y_val_list)
    
    if np.size(x_val_arr) == np.size(y_val_arr):
        if type_option == 0: # Sample Variance
            return np.sum((x_val_arr - x_val_mean)*(y_val_arr - y_val_mean))/(np.size(x_val_arr) - 1) 
        elif type_option == 1:
            return np.sum((x_val_arr - x_val_mean)*(y_val_arr - y_val_mean))/(np.size(x_val_arr) - 1) 
        else:
            print("Error - Option not found")
            return # return nothing
    else:
        print("Error - Number of Variables from each side are not equal")
        return 
    
def linReg(x_list, y_list):
    x_colMat = np.array(x_list)
    y_colMat = np.array(y_list)
    
    x_mean = np.sum(x_colMat)/np.size(x_colMat)
    y_mean = np.sum(y_colMat)/np.size(y_colMat)
    
    #print(np.sum(x_colMat), np.sum(y_colMat))
    #print(np.size(x_colMat), np.size(y_colMat))
    #print(x_mean, y_mean)
    
    # Could be error - population based eqn rather than sample, but value matches benchmark. It is a simplified formuala.
    x_stdDev = np.sum(x_colMat*x_colMat) - (np.size(x_colMat))*x_mean*x_mean
    xy_stdDev = np.sum(x_colMat*y_colMat) - (np.size(y_colMat))*x_mean*y_mean
    y_stdDev = np.sum(y_colMat*y_colMat) - (np.size(y_colMat))*y_mean*y_mean
    
    var_x = (np.sum((x_colMat - x_mean)*(x_colMat - x_mean)))/(np.size(x_colMat) - 1)
    coVar_xy = (np.sum((x_colMat - x_mean)*(y_colMat - y_mean)))/(np.size(x_colMat) - 1)
    var_y = (np.sum((y_colMat - y_mean)*(y_colMat - y_mean)))/(np.size(y_colMat) - 1)
          
    #x_stdDev_sample = math.sqrt(var_x)
    #xy_stdDev_sample = math.sqrt(coVar_xy) # negative value cannot be square rooted. The alternate formula bypasses the squareroot problem.
    #y_stdDev_sample = math.sqrt(var_y)
    
    #print(x_stdDev - xy_stdDev_sample, xy_stdDev - xy_stdDev_sample, y_stdDev - y)
    
    #print(np.sum((x_colMat - x_mean)*(x_colMat - x_mean)), np.sum((y_colMat - y_mean)*(y_colMat - y_mean)))
    #print("CoVariance: ", coVar_xy)
    #print(var_x, var_y)
    
    #print("Correlation Factor, r: ", r)
    
    B_1 = xy_stdDev/x_stdDev # Linear Regression gradient
    B_0 = y_mean - B_1*x_mean # Linear Regression intercept
    
    r = coVar_xy/(math.sqrt(var_x*var_y)) # Coefficient of Correlation
    
    # REF: https://sites.chem.utoronto.ca/chemistry/coursenotes/analsci/stats/ErrRegr.html
    SS_e = math.sqrt((np.sum((y_colMat - y_mean)*(y_colMat - y_mean)))/(np.size(y_colMat) - 2)) 
    
    SS_grad = SS_e/(math.sqrt( np.sum((x_colMat - x_mean)*(x_colMat - x_mean)) ))
    SS_intercept = (SS_e*(math.sqrt(np.sum(x_colMat*x_colMat))))/((np.size(x_colMat))*(np.sum((x_colMat - x_mean)*(x_colMat - x_mean))))
    
    # print("Returns ", "B_1: ", B_1, ",B_0: ", B_0, ",SS_e: ", SS_e)
    return (B_1, B_0, r, SS_e, SS_grad, SS_intercept)

# def logReg(self, x_list, y_list):