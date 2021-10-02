def getMean(self, val_list):
    val_colMat = np.array(val_list)
    
    # print("Return: ", np.sum(val_colMat)/np.size(val_colMat))
    return np.sum(val_colMat)/np.size(val_colMat)
    
def linReg(self, x_list, y_list):
    x_colMat = np.array(x_list)
    y_colMat = np.array(y_list)
    
    x_mean = np.sum(x_colMat)/np.size(x_colMat)
    y_mean = np.sum(y_colMat)/np.size(y_colMat)
    
    x_stdDev = np.sum(x_colMat*x_colMat) - (np.size(x_colMat))*x_mean*x_mean
    xy_stdDev = np.sum(x_colMat*y_colMat) - (np.size(y_colMat))*x_mean*y_mean
    y_stdDev = np.sum(y_colMat*y_colMat) - (np.size(y_colMat))*y_mean*y_mean
    
    B_1 = xy_stdDev/x_stdDev # Linear Regression gradient
    B_0 = y_mean - B_1*x_mean # Linear Regression intercept
    SS_e = y_stdDev - B_1*xy_stdDev # Error Standard Deviation
    
    # print("Returns ", "B_1: ", B_1, ",B_0: ", B_0, ",SS_e: ", SS_e)
    return (B_1, B_0, SS_e)