import numpy as np
from scipy.stats import norm

class BSM:
    
    norm = norm.cdf
    
    def __init__(self, stock_price, strike_price, days_to_expiry, interest_rate, volatility):
        self.price = stock_price
        self.strike = strike_price
        self.dte = days_to_expiry
        self.rate = interest_rate
        self.vol = volatility
      
    def bsm_call(self):
        ''' Computing the call option price '''
        d1 = (np.log(self.price/self.strike) + self.dte*(self.rate + 
                            (self.vol ** 2)/2))/(self.vol*(np.sqrt(self.dte)))
        d2 = d1 - (self.vol*(np.sqrt(self.dte)))
        call = self.stock * norm(d1) - norm(d2) * self.strike * np.exp(-self.rate*self.dte)
        return call
    
    def bsm_put(self):
        ''' Computing the put option price'''
        d1 = (np.log(self.price/self.strike) + self.dte*(self.rate + 
                            (self.vol ** 2)/2))/(self.vol*(np.sqrt(self.dte)))
        d2 = d1 - (self.vol*(np.sqrt(self.dte)))
        put = norm(-d2) * self.strike * np.exp(-self.rate * self.dte) - norm(-d1) * self.stock
        return put
        
