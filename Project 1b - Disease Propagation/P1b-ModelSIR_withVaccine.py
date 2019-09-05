import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

alpha = 0.1
beta = 0.7
gamma = 0.1

susceptible_0 = [1000, 20]
infected_0 = [100, 0]


nb_cities = len(susceptible_0)
recovered_0 = [0]*nb_cities
state_0 = susceptible_0 + infected_0 + recovered_0 #suscept, infect, recov

w = [[0.01]*nb_cities]*nb_cities


def SIR(state, t):
    susceptible = state[:nb_cities]
    infected = state[nb_cities:2*nb_cities]
    recovered = state[2*nb_cities:]
    d_suscept = [0]*nb_cities
    d_infect = [0]*nb_cities
    d_recov = [0]*nb_cities

    for n in range(nb_cities):
        d_suscept[n] = -(beta*susceptible[n]*infected[n])/(susceptible[n]+infected[n]+recovered[n]) - gamma*susceptible[n]
        d_infect[n] = (beta*susceptible[n]*infected[n])/(susceptible[n]+infected[n]+recovered[n]) - alpha*infected[n]
        d_recov[n] = gamma*susceptible[n] + alpha*infected[n]
        for m in range(nb_cities):
            if m != n:
                d_suscept[n] += w[m][n]*susceptible[m] - w[n][m]*susceptible[n]
                d_infect[n] += w[m][n]*infected[m] - w[n][m]*infected[n]
                d_recov[n] += w[m][n]*recovered[m] - w[n][m]*recovered[n]
    return(d_suscept + d_infect + d_recov)

t= np.linspace(0,50,300)
sol = scipy.integrate.odeint(SIR, state_0, t)


sol_suscept = sol[:,:nb_cities]
sol_infect = sol[:,nb_cities:2*nb_cities]
sol_recov = sol[:,2*nb_cities:]

for n in range(nb_cities):
    plt.plot(t, sol_infect[:,n], label='infected in city n'+str(n))
    plt.plot(t, sol_suscept[:,n], label='suscept in city n'+str(n))
    plt.plot(t, sol_recov[:,n], label='recov in city n'+str(n))
plt.legend()
plt.show()
print(sol[0])
print(sol[-1])
