#!/usr/bin/env python
# coding: utf-8

# # Neuroscience, Learning, Memory, Cognition Course
# ## Sharif University of Technology
# 

# In[1]:


#@title Enter your information & "RUN the cell!!"
student_id =  99102156 #@param {type:"integer"}
student_name = "Arsham Lolohari" #@param {type:"string"}

print("your student id:", student_id)
print("your name:", student_name)


# ##Exercise Outline : 
# This exercise consist of two parts: in part (I) we would practice our python skills and in part (II) we would get familiar with some neuron models which may hear before in the course. You have to complete and deliver this .ipynb file and a report describing your result. Grades will be given based on your report and your code.

# #** PART I: PYTHON PRACTICE**

# **1) Working with arrays using PyLab**
# 
# In Python, there are several different data structures that are designed to store more than one element. Here we will focus on the `array` data structure, but if you are curious to know how and when to use other structures, there is a good explanation <a href='http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html'>here</a>. Let's define an array:

# In[2]:


from pylab import *


# In[97]:


a = array([[1, 2, 3, 4]])
b = array( [[0, 4, 7, 6]] )
c = array([[10],
          [20],
          [30],
          [40]])
d = array([[1],
          [2],
          [3],
          [4]])


# In[98]:


print(a*b)
print(multiply(a,b))
print(c*a)
print(multiply(c,a))
#who
#%whos


# **Q.**
# 
# Search about pylab package and describe it shortly?
# 
# Multiply two defined arrays `a` and `b` using operator `*` and multiply(a,b). 
# What operation does `multiply()` perform?
# 
# To see a list of the variables you've defined, type `who` or `whos` in a code block by themselves. Notice `whos` provides more information.
# 
# *`5 Points`* 
# 

# **2) Defining a new function.**
# 
# Sometimes we'll need to write our own Python functions.  Let's do that now.
# 
# Our function will do something very simple: it will take as input a
# vector and return as output the vector elements squared plus an additive
# constant.
# 
# If have a vector, `v`, and a constant, `b`, we would like to call:
# 
#     vsq = my_square_function(v, b)
#     
# This won't work!  We first need to define `my_square_function`. Let's do so now,
# please complete the function below:
# 
# *`5 Points`*
# 

# In[99]:


def my_square_function(x, c):
    """Square a vector and add a constant.

    Arguments:
    x -- vector to square
    c -- constant to add to the square of x
    """
    
    output = x**2+c
    return   output


# The function begins with the keyword `def` followed by the function name and the inputs in parentheses. Notice that this first line ends with a colon `:`. All of the function components that follow this first line should be **indented one level**. This is just like the `for` loop we applied earlier; the operations performed by the for loop were indented one leve.

# <div class="python-note">
#     
# When defining the function, the code the function executes should be indented one level.
# 
# </div>

# The text inside triple quotes provides an optional documentation string that describes our function. While optional, including a '*doc string*' is an important part of making your code understandable and reuseable.
# 
# The keyword `return` exits the function, and in this case returns the expression `x * x + c`. Note that a return statement with no arguments returns `None`, indicating the absence of a value.
# 
# With the function defined, let's now call it. To do so we first define the inputs, and then run the function, as follows:

# To see the doc string that describes our function, type `my_square_function?`

# In[100]:


# Let's check that our docstring works
get_ipython().run_line_magic('pinfo', 'my_square_function')


# **3) Loading matlab data (.mat) and plot power spectrum**
# 
# 
# We consider data recorded in the scalp electroencephalogram or EEG. The EEG provides a measure of brain voltage activity with high temporal resolution (typically on the order of milliseconds) but poor spatial resolution (on the order of 10 cm2 of cortex). Here we will consider EEG activity recorded from a 
# single scalp electrode. We will analyze these data to determine what (if any) rhythmic activity is present. In doing so, we will learn about an important technique to characterize rhythms in data - the Fourier transform and power spectral density or “spectrum”. please fill in the code below and plot the power spectral density.
# 
# The EEG data is available [here](https://drive.google.com/file/d/1RGvi6Tr8qhLPfBwo0A-kCKedFDqdPxYv/view?usp=sharing).
# 
# *`5 Points`*
# 
# 

# In[4]:


##################################
# add all necessary packages here
##################################

from scipy.io import loadmat                    
from pylab import *                            
from numpy import where
from numpy.fft import fft, rfft, fftshift
from scipy.signal import spectrogram
rcParams['figure.figsize']=(12,3)              


# In[110]:


data = loadmat("EEG-1.mat")  # Load the EEG data
EEG = data['EEG'].reshape(-1)         # Extract the EEG variable
t = data['t'][0]                      # ... and the t variable

x = EEG                               # Relabel the data variable
dt = t[1] - t[0]                      # Define the sampling interval
N = x.shape[0]                        # Define the total number of data points
T = N * dt                            # Define the total duration of the data

xf = fft(x)                             # Compute Fourier transform of x
xf = fftshift(xf)

df = 1 / T.max()                      # Determine frequency resolution
fNQ = 1 / dt / 2                      # Determine Nyquist frequency
faxis = arange(0,fNQ,df)              # Construct frequency axis

Sxx = (abs(xf)**2) /(N/dt/2)                           # Compute spectrum

Sxx = Sxx[round(N/2):N]                             # Ignore negative frequencies


plot(faxis, Sxx.real)                 # Plot spectrum vs frequency
xlim([0, 100])                        # Select frequency range
xlabel('Frequency [Hz]')              # Label the axes
ylabel('Power [$\mu V^2$/Hz]')
show()


# your result should be like below: 
# 
# ![download.png](data:image/png;base64,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)

# #** PART II: NEURON MODELS**

# ## Import necessary packages 
# 

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

##################################
# add all necessary packages here
##################################


# ---
# #The Leaky Integrate-and-Fire (LIF) model

# This video introduces the reduction of a biological neuron to a simple leaky-integrate-fire (LIF) neuron model.
# 
# Now, it's your turn to implement one of the simplest mathematical model of a neuron: the leaky integrate-and-fire (LIF) model. The basic idea of LIF neuron was proposed in 1907 by Louis Édouard Lapicque, long before we understood the electrophysiology of a neuron (see a translation of [Lapicque's paper](https://pubmed.ncbi.nlm.nih.gov/17968583/) ). More details of the model can be found in the book [**Theoretical neuroscience**](http://www.gatsby.ucl.ac.uk/~dayan/book/) by Peter Dayan and Laurence F. Abbott.
# 
# The subthreshold membrane potential dynamics of a LIF neuron is described by
# 
# \begin{eqnarray}
# C_m\frac{dV}{dt} = -g_L(V-E_L) + I,\quad (1)
# \end{eqnarray}
# 
# where $C_m$ is the membrane capacitance, $V$ is the membrane potential, $g_L$ is the leak conductance ($g_L = 1/R$, the inverse of the leak resistance $R$), $E_L$ is the resting potential, and $I$ is the external input current. 
# 
# Dividing both sides of the above equation by $g_L$ gives
# 
# \begin{align}
# \tau_m\frac{dV}{dt} = -(V-E_L) + \frac{I}{g_L}\,,\quad (2)
# \end{align}
# 
# where the $\tau_m$ is membrane time constant and is defined as $\tau_m=C_m/g_L$. 
# 
# Note that dividing capacitance by conductance gives units of time! 
# 
# Below, we will use Eqn.(2) to simulate LIF neuron dynamics. 
# 
# If $I$ is sufficiently strong such that $V$ reaches a certain threshold value $V_{\rm th}$, $V$ is reset to a reset potential $V_{\rm reset}< V_{\rm th}$, and voltage is clamped to $V_{\rm reset}$ for $\tau_{\rm ref}$ ms, mimicking the refractoriness of the neuron during an action potential:
# 
# \begin{eqnarray}
# \mathrm{if}\quad V(t_{\text{sp}})\geq V_{\rm th}&:& V(t)=V_{\rm reset} \text{  for } t\in(t_{\text{sp}}, t_{\text{sp}} + \tau_{\text{ref}}]
# \end{eqnarray}
# where $t_{\rm sp}$ is the spike time when $V(t)$ just exceeded $V_{\rm th}$.
# 
# </details>
# 
# 
# The LIF model captures the facts that a neuron:
# - performs spatial and temporal integration of synaptic inputs
# - generates a spike when the voltage reaches a certain threshold
# - goes refractory during the action potential
# - has a leaky membrane
# 
# The LIF model assumes that the spatial and temporal integration of inputs is linear. Also, membrane potential dynamics close to the spike threshold are much slower in LIF neurons than in real neurons.

# ## Coding Exercise 1: Python code to simulate the LIF neuron
# 
# We now write Python code to calculate our equation for the LIF neuron and simulate the LIF neuron dynamics. We will use the Euler method, to numerically integrate this equation:
# 
# \begin{equation}
# \tau_m\frac{dV}{dt} = -(V-E_L) + \frac{I}{g_L}\,
# \end{equation}
# 
# where $V$ is the membrane potential, $g_L$ is the leak conductance, $E_L$ is the resting potential, $I$ is the external input current, and $\tau_m$ is membrane time constant.
# 
# The cell below initializes a dictionary that stores parameters of the LIF neuron model and the simulation scheme. You can use `pars=default_pars(T=simulation_time, dt=time_step)` to get the parameters. Note that, `simulation_time` and `time_step` have the unit `ms`. In addition, you can add the value to a new parameter by `pars['New_param'] = value`.

# In[111]:


# @markdown Execute this code to initialize the default parameters


def default_pars(**kwargs):
  pars = {}

  # typical neuron parameters#
  pars['V_th'] = -55.     # spike threshold [mV]
  pars['V_reset'] = -75.  # reset potential [mV]
  pars['tau_m'] = 10.     # membrane time constant [ms]
  pars['tau_ou'] = 10.    #OU process time constant [ms]
  pars['g_L'] = 10.       # leak conductance [nS]
  pars['V_init'] = -75.   # initial potential [mV]
  pars['E_L'] = -75.      # leak reversal potential [mV]
  pars['tref'] = 2.       # refractory time (ms)

  # simulation parameters #
  pars['T'] = 400.  # Total duration of simulation [ms]
  pars['dt'] = .1   # Simulation time step [ms]

  # external parameters if any #
  for k in kwargs:
    pars[k] = kwargs[k]

  pars['range_t'] = np.arange(0, pars['T'], pars['dt'])  # Vector of discretized time points [ms]

  return pars

pars = default_pars()
print(pars)


# Complete the function below to simulate the LIF neuron when receiving external current inputs. You can use `v, sp = run_LIF(pars, Iinj)` to get the membrane potential (`v`) and spike train (`sp`) given the dictionary `pars` and input current `Iinj`. please describe the function completely in your report, this show that you understand other parts of the code
# 
# *`15 Points`*

# In[112]:


def run_LIF(pars, Iinj, stop=False):
  """
  Simulate the LIF dynamics with external input current

  Args:
    pars       : parameter dictionary
    Iinj       : input current [pA]. The injected current here can be a value
                 or an array
    stop       : boolean. If True, use a current pulse

  Returns:
    rec_v      : membrane potential
    rec_sp     : spike times
  """

  # Set parameters
  V_th, V_reset = pars['V_th'], pars['V_reset']
  tau_m, g_L = pars['tau_m'], pars['g_L']
  V_init, E_L = pars['V_init'], pars['E_L']
  dt, range_t = pars['dt'], pars['range_t']
  Lt = range_t.size
  tref = pars['tref']

  # Initialize voltage
  v = np.zeros(Lt)
  v[0] = V_init

  # Set current time course
  Iinj = Iinj * np.ones(Lt)

  # If current pulse, set beginning and end to 0
  if stop:
    Iinj[:int(len(Iinj) / 2) - 1000] = 0
    Iinj[int(len(Iinj) / 2) + 1000:] = 0

  # Loop over time
  rec_spikes = []  # record spike times
  tr = 0.  # the count for refractory duration

  for it in range(Lt - 1):

    if tr > 0:  # check if in refractory period
      v[it] = V_reset  # set voltage to reset
      tr = tr - 1 # reduce running counter of refractory period

    elif v[it] >= V_th:  # if voltage over threshold
      rec_spikes.append(it)  # record spike event
      v[it] = V_reset  # reset voltage
      tr = tref / dt  # set refractory time

    ########################################################################
    ## TODO for students: compute the membrane potential v, spike train sp #
    # Fill out function and remove
    #raise NotImplementedError('calculate the dv/dt and the update step!')
    ########################################################################

    # Calculate the increment of the membrane potential
    dv = dt/tau_m*(E_L-v[it]+Iinj[it]/g_L)

    # Update the membrane potential
    v[it + 1] = v[it] + dv

  # Get spike times in ms
  rec_spikes = np.array(rec_spikes) * dt

  return v, rec_spikes


# In[113]:


# Get parameters
pars = default_pars(T=500)

# Simulate LIF model
v, sp = run_LIF(pars, Iinj=100, stop=True)

# Visualize
fig = plt.figure(figsize =(10, 7))
plot(pars['range_t'], v)      

threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
title("Membrane Potential for current pulse with amplitude 100")
xlim([0, pars['T']])                        # Limit axes
ylim([pars['V_reset']-5,-40])
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')
plt.legend(['Membrane Potential', 'Threshold Vth'])
show()


# 
# *Example output:*
# 
# <img alt='Solution hint' align='left' width=820.0 height=539.0 src=https://raw.githubusercontent.com/NeuromatchAcademy/course-content/main/tutorials/W2D3_BiologicalNeuronModels/static/W2D3_Tutorial1_Solution_60a1e954_0.png>
# 
# 

# ---
# # Response of an LIF model to different types of input currents
# 
# 
# 
# In the following section, we will learn how to inject direct current and white noise to study the response of an LIF neuron.

# ### Parameter exploration of Direct current (DC) input amplitude 
# Please shows how the LIF neuron behavior changes for DC input (constant current) with different amplitudes.You may notice that the neuron generates a spike. But this is just a cosmetic spike only for illustration purposes. In an LIF neuron, we only need to keep track of times when the neuron hits the threshold so the postsynaptic neurons can be informed of the spike. 
# 
# How much DC is needed to reach the threshold (rheobase current)? How does the membrane time constant affect the frequency of the neuron?
# 
# *`10 Points`*

# In[13]:


# Get parameters
pars = default_pars(T=500,tau_m=20)

# Simulate LIF model
i = 250
v, sp = run_LIF(pars, Iinj=i, stop=False)

# Visualize
fig = plt.figure(figsize =(10, 7))
plot(pars['range_t'], v)      

threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
title("Membrane Potential for DC Iinj = "+str(i) + " and tau_m = "+str(pars['tau_m']))
xlim([0, pars['T']])                        # Limit axes
ylim([pars['V_reset'],-40])
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')
plt.legend(['Membrane Potential', 'Threshold Vth'])
show()


# ## Gaussian white noise (GWN) current 
# 
# 
# Given the noisy nature of neuronal activity _in vivo_, neurons usually receive complex, time-varying inputs.
# 
# To mimic this, we will now investigate the neuronal response when the LIF neuron receives Gaussian white noise $\xi(t)$ with mean 0 ($\mu = 0$) and some standard deviation $\sigma$.
# 
# Note that the GWN has zero mean, that is, it describes only the fluctuations of the input received by a neuron. We can thus modify our definition of GWN to have a nonzero mean value $\mu$ that equals the DC input, since this is the average input into the cell. The cell below defines the modified gaussian white noise currents with nonzero mean $\mu$.

# ### LIF neuron Explorer for noisy input
# 
# 
# The mean of the Gaussian white noise (GWN) is the amplitude of DC. Indeed, when $\sigma = 0$, GWN is just a DC.
# 
# So the question arises how does $\sigma$ of the GWN affect the spiking behavior of the neuron. For instance we may want to know
# 1.  how does the minimum input (i.e., $\mu$) needed to make a neuron spike change with increase in $\sigma$
# 2.  how does the spike regularity change with increase in $\sigma$
# 
# Please fill the my_GWN function to generate the noisy input current and then answer the question above: `my_GWN(pars, mu, sig, myseed=False)`.  Note that fixing the value of the random seed (e.g., `myseed=2020`) will allow you to obtain the same result every time you run this. We then use our `run_LIF` function to simulate the LIF model.
# 
# *`15 Points`*

# In[26]:


from random import *
def my_GWN(pars, mu, sig, myseed=False):
    """
    Function that generates Gaussian white noise input

    Args:
    pars       : parameter dictionary
    mu         : noise baseline (mean)
    sig        : noise amplitute (standard deviation)
    myseed     : random seed. int or boolean
                 the same seed will give the same
                 random number sequence

    Returns:
    I          : Gaussian white noise input
    """

    # Retrieve simulation parameters
    dt, range_t = pars['dt'], pars['range_t']
    Lt = range_t.size

    # Set random seed
    if myseed:
        seed(myseed)

    # Generate GWN and convert units to sec.
    #I_gwn = np.random.normal(mu, sig, size=Lt)
    I_gwn = mu + sig * np.random.randn(1, Lt)[0]

    return I_gwn

help(my_GWN)


# In[115]:


# Get parameters
pars = default_pars(T=500)

mu = 150
sig = 400
# Simulate LIF model
i = my_GWN(pars, mu, sig, myseed=False)

v, sp = run_LIF(pars, Iinj=i, stop=False)

# Visualize
fig = plt.figure(figsize =(10, 7))
plot(pars['range_t'], v)      

threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
title("Membrane Potential for WGN Iinj with mu= "+str(mu) + " and sig = " + str(sig) + " and tau_m = "+str(pars['tau_m']))
xlim([0, pars['T']])                        # Limit axes
ylim([pars['V_reset'],-40])
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')
plt.legend(['Membrane Potential', 'Threshold Vth'])
show()


# ### Analyzing GWN Effects on Spiking
# - As we increase the input average ($\mu$) or the input fluctuation ($\sigma$), the spike count changes. How much can we increase the spike count, and what might be the relationship between GWN mean/std or DC value and spike count? 
# 
# - We have seen above that when we inject DC, the neuron spikes in a regular manner (clock-like), and this regularity is reduced when GWN is injected. The question is, how irregular can we make the neurons spiking by changing the parameters of the GWN? 
# 
# We will see the answers to these questions in the next section but discuss first!
# 
# *`5 Points`*
# 

# ### The interspike interval (ISI)
# The ISI is the time between subsequent action potentials (also known as spikes) of a single or group of neuron. 
# Please search a little bit about this concept and discuss it in your report. 
# *`5 Points`*

# ---
# # Firing rate and spike time irregularity
# 
# 
# When we plot the output firing rate as a function of GWN mean or DC value, it is called the input-output transfer function of the neuron (so simply F-I curve).
# 
# Spike regularity can be quantified as the **coefficient of variation (CV) of the interspike interval (ISI)**:
# 
# \begin{equation}
# \text{CV}_{\text{ISI}} = \frac{std(\text{ISI})}{mean(\text{ISI})}
# \end{equation}
# 
# A Poisson train is an example of high irregularity, in which $\textbf{CV}_{\textbf{ISI}} \textbf{= 1}$. And for a clocklike (regular) process we have $\textbf{CV}_{\textbf{ISI}} \textbf{= 0}$ because of **std(ISI)=0**.

# ## F-I Explorer for different `sig_gwn`
# 
# How does the F-I curve of the LIF neuron change as we increase the $\sigma$ of the GWN? We can already expect that the F-I curve will be stochastic and the results will vary from one trial to another. But will there be any other change compared to the F-I curved measured using DC?
# 
# write a simple code and show how the F-I curve of a LIF neuron changes for different levels of fluctuation $\sigma$.
# 
# *`10 Points`*

# In[17]:


# Get parameters
T = 500 #total time of simulation
pars = default_pars(T=T)

max_meanI = 225 #maximum DC part for wgn current
meanI_step = 5
total_samps = round(max_meanI/meanI_step) + 1 #total samples to plot

max_sig = 500
sig_step = 100


fig = plt.figure(figsize =(20, 10))

for i in range(0, max_sig+sig_step, sig_step):
    sig = i
    meanI_arr = np.zeros(total_samps)
    firingRate_arr = np.zeros(total_samps)
    
    for j in range(0,max_meanI+meanI_step,meanI_step):
        mu = j
        # Simulate LIF model
        current = my_GWN(pars, mu, sig, myseed=False)

        v, sp = run_LIF(pars, Iinj=current, stop=False)
        
        firingRate = len(sp)/T
        firingRate_arr[round(j/meanI_step)] = firingRate
        meanI_arr [round(j/meanI_step)] = mu
        
    # Visualize
    subplot(1, round(max_sig/sig_step)+1 , round(i/sig_step)+1)
    plot(meanI_arr, firingRate_arr)      
    title("Firing rate vs current mean for WGN Iinj with sig = " + str(sig))
    xlim([0, max_meanI+meanI_step])                        # Limit axes
    xlabel("current's DC value")              # Label the axes
    ylabel('Firing rate (per ms)')
    show()
        
        


# ## Compute $CV_{ISI}$ values
# 
# The fluctuation can also change the irregularity of the spikes. Let's investigate the effect of $\mu=250$ with $\sigma=0.5$ vs $\sigma=3$. 
# 
# Fill in the code below to compute ISI, then plot the histogram of the ISI and compute the $CV_{ISI}$. Note that, you can use `np.diff` to calculate ISI.
# 
# *`10 Points`*

# In[140]:


import statistics as stat
def isi_cv_LIF(spike_times):
    """
    Calculates the interspike intervals (isi) and
    the coefficient of variation (cv) for a given spike_train

    Args:
    spike_times : (n, ) vector with the spike times (ndarray)

    Returns:
    isi         : (n-1,) vector with the inter-spike intervals (ms)
    cv          : coefficient of variation of isi (float)

    """
    ########################################################################
    ## TODO for students: compute the membrane potential v, spike train sp #
    # Fill out function and remove
    #  raise NotImplementedError('Student Exercise: calculate the isi and the cv!')
    ########################################################################
    if len(spike_times) >= 2:
        # Compute isi
        isi = np.diff(spike_times)
        # Compute cv
        cv = stat.stdev(isi) / stat.mean(isi)
    else:
        isi = np.nan
        cv = np.nan

    return isi, cv


# Set parameters
pars = default_pars(T=1000.)
mu_gwn = 250
sig_gwn1 = 50.0
sig_gwn2 = 300

# Run LIF model for sigma = 0.5
I_GWN1 = my_GWN(pars, mu=mu_gwn, sig=sig_gwn1, myseed=2030)
_, sp1 = run_LIF(pars, Iinj=I_GWN1)

# Run LIF model for sigma = 3
I_GWN2 = my_GWN(pars, mu=mu_gwn, sig=sig_gwn2, myseed=2030)
_, sp2 = run_LIF(pars, Iinj=I_GWN2)

# Compute ISIs/CV
isi1, cv1 = isi_cv_LIF(sp1)
isi2, cv2 = isi_cv_LIF(sp2)

# Visualize
fig = plt.figure(figsize =(15, 7))

subplot(1,2,1)
hist(isi1,bins = np.arange(10,30,0.5), rwidth=0.9)
title("$\u03C3_{GWN}$ = "+ str(sig_gwn1) + ", $CV_{isi}$ = " + str(cv1))
# xlim([0,30])
xlabel('ISI (ms)')              # Label the axes
ylabel('count')

subplot(1,2,2)
hist(isi2, bins = np.arange(10,30,0.5), rwidth=0.9)
title("$\u03C3_{GWN}$ = "+ str(sig_gwn2) + ", $CV_{isi}$ = " + str(cv2))
xlabel('ISI (ms)')              # Label the axes
ylabel('count')
show()


# 
# *Example output:*
# 
# <img alt='Solution hint' align='left' width=1078.0 height=378.0 src=https://raw.githubusercontent.com/NeuromatchAcademy/course-content/main/tutorials/W2D3_BiologicalNeuronModels/static/W2D3_Tutorial1_Solution_27d69c89_0.png>
# 
# 

# ## Spike irregularity explorer for different `sig_gwn`
# 
# How different levels of fluctuation $\sigma$ affect the CVs for different average injected currents ($\mu$)?
# 
# 1. Does the standard deviation of the injected current affect the F-I curve in any qualitative manner?
# 2. Why does increasing the mean of GWN reduce the CV$_{\rm ISI}$?
# 3.  If you plot spike count (or rate) vs. CV$_{\rm ISI}$, should there be a relationship between the two? Try out yourself.
# 
# *`15 Points`*

# In[151]:


# Get parameters
T = 500 #total time of simulation
pars = default_pars(T=T)

sig_arr = np.array([3,30,100])
max_meanI = 300 #maximum DC part for wgn current
meanI_step = 5
total_samps = round(max_meanI/meanI_step) + 1 #total samples to plot

cv_arr = np.zeros(total_samps)
firingRate_arr = np.zeros(total_samps)

fig = plt.figure(figsize =(20, 10))
for s in sig_arr:
    for j in range(0,max_meanI+meanI_step,meanI_step):
        mu = j
        # Simulate LIF model
        current = my_GWN(pars, mu, s, myseed=2022)

        v, sp = run_LIF(pars, Iinj=current, stop=False)

        isi, cv = isi_cv_LIF(sp)

        firingRate = len(sp)/T
        firingRate_arr[round(j/meanI_step)] = firingRate
        cv_arr [round(j/meanI_step)] = cv
    # Visualize
    plot(cv_arr, firingRate_arr)      


title("Firing rate vs current mean for WGN Iinj with mu values from 0 to " + str(max_meanI))
#xlim([0, max_meanI+meanI_step])                        # Limit axes
xlabel("CV")              # Label the axes
ylabel('Firing rate (per ms)')
plt.legend(['sig = '+str(sig_arr[0]), 'sig = '+str(sig_arr[1]), 'sig = '+str(sig_arr[2])])
show()
        
        


# ---
# ## Ornstein-Uhlenbeck Process
# 
# When a neuron receives spiking input, the synaptic current is Shot Noise -- which is a kind of colored noise and the spectrum of the noise determined by the synaptic kernel time constant. That is, a neuron is driven by **colored noise** and not GWN.
# 
# We can model colored noise using the Ornstein-Uhlenbeck process - filtered white noise. 

# We next study if the input current is temporally correlated and is modeled as an Ornstein-Uhlenbeck process $\eta(t)$, i.e., low-pass filtered GWN with a time constant $\tau_{\eta}$: 
# 
# \begin{equation}
# \tau_\eta \frac{d}{dt}\eta(t) = \mu-\eta(t) + \sigma_\eta\sqrt{2\tau_\eta}\xi(t)
# \end{equation}
# 
# **Hint:** An OU process as defined above has
# 
# \begin{equation}
# \mathbb{E}[\eta(t)]=\mu
# \end{equation}
# 
# and autocovariance 
# 
# \begin{equation}
# [\eta(t)\eta(t+\tau)]=\sigma_\eta^2e^{-|t-\tau|/\tau_\eta}
# \end{equation}
# 
# which can be used to check your code. 

# In the following, we will check how a neuron responds to a noisy current that follows the statistics of an OU process. please fill the my_OU function and run your LIF model with OU process input current, then answer question below:
# 
# -  How does the OU type input change neuron responsiveness? 
# -  What do you think will happen to the spike pattern and rate if you increased or decreased the time constant of the OU process?
# 
# *`15 Points`*

# In[51]:


import math
def my_OU(pars, mu, sig, myseed=False):
    """
    Function that produces Ornstein-Uhlenbeck input

    Args:
    pars       : parameter dictionary
    sig        : noise amplitute
    myseed     : random seed. int or boolean

    Returns:
    I_ou       : Ornstein-Uhlenbeck input current
    """

    # Retrieve simulation parameters
    dt, range_t = pars['dt'], pars['range_t']
    Lt = range_t.size
    tau_ou = pars['tau_ou']  # [ms]

    # set random seed
    if myseed:
        np.random.seed(seed=myseed)
    else:
        np.random.seed()

    # Initialize
    noise = np.random.randn(Lt)
    I_ou = np.zeros(Lt)
    I_ou[0] = noise[0] * sig

    # generate OU
    for it in range(Lt-1):
        I_ou[it+1] = I_ou[it] + dt/tau_ou * (mu - I_ou[it] + sig * math.sqrt(2*tau_ou) * noise[it])

    return I_ou


help(my_OU)


# In[56]:


# Get parameters
pars = default_pars(T=500,tau_ou = 5)

mu = 150
sig = 200
# Simulate LIF model
i_ou = my_OU(pars, mu, sig, myseed=2022)
i_gwn = my_GWN(pars, mu, sig, myseed=2022)
v_ou, sp_ou = run_LIF(pars, Iinj=i_ou, stop=False)
v_gwn, sp_gwn = run_LIF(pars, Iinj=i_gwn, stop=False)

# Visualize
fig = plt.figure(figsize =(20, 7))
subplot(1,2,1)
plot(pars['range_t'], v_ou)      
threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
title("Membrane Potential for OU Iinj with mu= "+str(mu) + " and sig = " + str(sig) + " and tau_ou = "+str(pars['tau_ou']))
xlim([0, pars['T']])                        # Limit axes
ylim([pars['V_reset'],-40])
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')
plt.legend(['Membrane Potential', 'Threshold Vth'])


subplot(1,2,2)
plot(pars['range_t'], v_gwn)      
threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
title("Membrane Potential for GWN Iinj with mu= "+str(mu) + " and sig = " + str(sig) + " and tau_m = "+str(pars['tau_m']))
xlim([0, pars['T']])                        # Limit axes
ylim([pars['V_reset'],-40])
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')
plt.legend(['Membrane Potential', 'Threshold Vth'])



show()


# In[70]:


#The effect of tau_ou on spiking pattern and firing rate
mu = 200
sig = 200

fig = plt.figure(figsize =(25, 25))
tau_ou_init = 5 #initial value
tau_steps = 10
tau_final = 125
total_steps = round((tau_final-tau_ou_init)/tau_steps + 1) #=13
for i in range(total_steps):
    tau_ou = tau_ou_init + i*tau_steps
    # Get parameters
    pars = default_pars(T=500,tau_ou = tau_ou)

    # Simulate LIF model
    i_ou = my_OU(pars, mu, sig, myseed=2023)
    v_ou, sp_ou = run_LIF(pars, Iinj=i_ou, stop=False)

    # Visualize
    subplot(ceil(total_steps/2),2,i+1)
    plot(pars['range_t'], v_ou)      
    threshold_plt = plt.axhline(y = pars['V_th'], color = 'black', linestyle = '--')
    title("Membrane Potential for OU Iinj with mu= "+str(mu) + " and sig = " + str(sig) + " and tau_ou = "+str(pars['tau_ou']))
    xlim([0, pars['T']])                        # Limit axes
    ylim([pars['V_reset'],-40])
    xlabel('Time (ms)')              # Label the axes
    ylabel('V (mV)')
    plt.legend(['Membrane Potential', 'Threshold Vth'])


# ---
# ## Extensions to Integrate-and-Fire models
# 
# 
# LIF model is not the only abstraction of real neurons. If you want to learn about more realistic types of neuronal models, please search about "Generalized Integrate-and-Fire models" and discuss it in your report. 
# 
# *`5 Points`*

# ---
# #The Hodgkin-Huxley model

# The Hodgkin–Huxley model, or conductance-based model, is a mathematical model that describes how action potentials in neurons are initiated and propagated. It is a set of nonlinear differential equations that approximates the electrical characteristics of excitable cells such as neurons and muscle cells. It is a continuous-time dynamical system.
# 
# Alan Hodgkin and Andrew Huxley described the model in 1952 to explain the ionic mechanisms underlying the initiation and propagation of action potentials in the squid giant axon.They received the 1963 Nobel Prize in Physiology or Medicine for this work. [link text](https://en.wikipedia.org/wiki/Hodgkin%E2%80%93Huxley_model)
# 
# 4 eqs of Hodgkin-Huxley model  
# * $C_M\displaystyle \frac{dV}{dt}=-g_{Na}(V-V_{Na})-g_k(V-V_K)-g_l(V-V_l)+I$ ($V$: Membrane Potential)  
# * $\displaystyle \frac{dh}{dt}=\alpha_h{(V)}(1-h)-\beta_h(V)h$ ($h$: Na Inactivation)  
# * $\displaystyle \frac{dm}{dt}=\alpha_m{(V)}(1-m)-\beta_m(V)m$ ($m$: Na Activation)  
# * $\displaystyle \frac{dn}{dt}=\alpha_n{(V)}(1-n)-\beta_n(V)n$ ($n$: K Activation)  

# Please fill the code below and discuss the whole code step by step in your report. 
# 
# *`5 Points`*

# In[ ]:


import numpy as np
import math


# In[200]:


def alphaM(V):
    return (2.5-0.1*(V+65)) / (np.exp(2.5-0.1*(V+65)) -1)

def betaM(V):
    return 4*np.exp(-(V+65)/18)

def alphaH(V):
    return 0.07*np.exp(-(V+65)/20)

def betaH(V):
    return 1/(np.exp(3.0-0.1*(V+65))+1)

def alphaN(V):
    return (0.1-0.01*(V+65)) / (np.exp(1-0.1*(V+65)) -1)

def betaN(V):
    return 0.125*np.exp(-(V+65)/80)

def HH(I0,T0):
    dt = 0.01;
    T  = math.ceil(T0/dt)  # [ms]
    gNa0 = 120   # [mS/cm^2]
    ENa  = 115;  # [mV]
    gK0  = 36;   # [mS/cm^2]
    EK   = -12;  # [mV]
    gL0  = 0.3;  # [mS/cm^2]
    EL   = 10.6; # [mV]
    

    t = np.arange(0,T)*dt
    V = np.zeros([T,1])
    m = np.zeros([T,1])
    h = np.zeros([T,1])
    n = np.zeros([T,1])
    gL = np.ones([T,1])*gL0
    gNa = np.zeros([T,1])
    gK = np.zeros([T,1])

    V[0]=-70.0
    m[0]=0.05
    h[0]=0.54
    n[0]=0.34
    
    gNa[0]=gNa0 * m[0]**3
    gK[0]=gK0 * n[0]**4

    for i in range(0,T-1):
        V[i+1] = V[i] + dt* (-(gNa0 * (m[i]**3) * h[i]) * (V[i] + 65 - ENa)-(gK0 * (n[i]**4)) * (V[i]+65- EK) - gL0 * (V[i]+65- EL) + I0 )
        m[i+1] = m[i] + dt* (alphaM(V[i]) * (1-m[i]) - betaM(V[i]) * m[i])
        h[i+1] = h[i] + dt* (alphaH(V[i]) * (1-h[i]) - betaH(V[i]) * h[i])
        n[i+1] = n[i] + dt* (alphaN(V[i]) * (1-n[i]) - betaN(V[i]) * n[i])
        
        gNa[i+1]=gNa0 * m[i+1]**3
        gK[i+1]=gK0 * n[i+1]**4


        
    return V,m,h,n,t,gL,gNa,gK


# ## At low input current (`I0`), examine the HH dynamics.
# 
#   To understand how the HH model works, we'll start by focusing on the
#   case when `I0` is small. Let's fix the input current to zero,

# In[194]:


I0 = 10


# and let's simulate the model for 100 ms,

# In[183]:


T0 = 100


# We've now defined both inputs to the `HH` function, and can execute it, as follows,

# In[201]:


[V,m,h,n,t,gL,gNa,gK]=HH(I0,T0)


# Notice that the function returns five outputs, which we assign to the variables `V`, `m`, `h`, `n`, and `t`.

# 
# What are the dynamics of the voltage (variable `V`) resulting
# from this simulation?<br>
# HINT:  Plot `V` vs `t`.
# 
# What are the dynamics of the gating variables (`m`, `h`, `n`)
# resulting from this simulation?<br>
# 
# What are the final values (after the 100 ms of simulation) of
# `V`, `m`, `h`, and `n`?
# 
# *`15 Points`*
# 
# Answer the above question using (`I0=10`).
# *`5 Points`*

# In[197]:


# Visualize
fig = plt.figure(figsize =(20, 7))

subplot(2,2,1)
plot(t, V)  
title("Membrane Potential for HH model Iinj with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('V (mV)')

subplot(2,2,2)
plot(t, m)   
title("m vs time with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('m')

subplot(2,2,3)
plot(t, h)    
title("h vs time with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('h')

subplot(2,2,4)
plot(t, n)      
title("n vs time with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('n')


show()


# Now, in the figure, you may use the pan/zoom tool to adjust the linked subplots.

# ##Bonus (+10 points):
# At (`I0=10`), describe the dynamics of the conductances.
# 
# please visualize how the *conductances* evolve during a single spike (plot gNa, gK, gL through time)   

# In[202]:


# Visualize
fig = plt.figure(figsize =(20, 7))

subplot(2,2,1)
plot(t, gL)  
title("gL with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('gL(t)')

subplot(2,2,2)
plot(t, gNa)   
title("gNa vs time with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('gNa(t)')

subplot(2,2,3)
plot(t, gK)    
title("gK vs time with I0= "+str(I0))
xlabel('Time (ms)')              # Label the axes
ylabel('gK(t)')

show()

