import numpy as np
class BinomialPricingModel:
    def __init__(self, stock_price, strike_price, days_to_expiry, time_steps, interest_rate, volatility):
        self.price = stock_price
        self.strike = strike_price
        self.dte = days_to_expiry
        self.rate = interest_rate
        self.vol = volatility
        self.N = time_steps
        
    def european_option(self):
        # calling a later defined function, for the purposes of modularity
        price_of_european_option = self.calculate_european_option_price()
        return price_of_european_option
    
    def calculate_european_option_price(self):
        #precompute constants
        dt = self.dte / (365 * self.N)
        u = np.exp(self.vol * np.sqrt(dt))
        d = 1/u
        q = (np.exp(self.rate*dt) - d) / (u-d) # risk neutral probability
        disc = np.exp(-self.rate*dt)

        # initialise asset prices at maturity
        C = self.price * d**(np.arange(self.N, -1, -1)) * u ** np.arange(0, self.N+1, 1)

        # initialise derivative values at maturity
        C = np.maximum( C - self.strike, np.zeros(self.N+1))
            
        # stepbackwards through tree
        for i in np.arange(self.N, 0, -1):
            C = disc * ( q * C[1: i+1] + (1-q) * C[0:i])
        return C[0]
# Usage example:
# model = BinomialPricingModel(stock_price, strike_price, days_to_expiry, interest_rates, time_steps, volatility)
# european_price = model.european_option()
# american_price = model.american_option()
