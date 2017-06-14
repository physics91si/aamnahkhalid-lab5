#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def wavepacket(x, k, sigma):
    """This function creates a wavepacket on the interval defined by x with
    wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
    """This function sould call noisy_packet() to get a Gaussian wave
    packet, call clean_data() to apply a low pass filter to the data and
    finally plot the result."""
   
    x_vals= np.arange(0, 4*np.pi)
    packet = noisy_packet(x_vals, 5,1,0.2)
    packet_plot= plt.figure()
    plt.plot(x_vals, packet)
    plt.savefig("noisy_packet.png")
    clean_data(x_vals, packet)




def noisy_packet(x_values, k, sigma, noise_amplitude):
    """This function returns a noisy Gaussian wavepacket with wave
    vector k, standard deviation sigma and Gaussian noise of standard
    deviation noise_amplitude."""
    clean_y = wavepacket(x_values,k,sigma)
    noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
    return noisy_y

def clean_data(x_values,y_values):
    """This function should take a set of y_values, perform the Fourier
    transform on it, filter out the high frequency noise, transform the
    signal back into real space, and return it."""

    clean_plot= plt.figure()
    
    Fourier_transform= np.fft.rfft(y_values)
    print(Fourier_transform)
   

    freq= np.fft.fftfreq(len(Fourier_transform))
    print(freq)
    filter_fourier = [filter_with_freq(x,f) for x, f in zip(Fourier_transform,freq)]
    new_y = np.fft.irfft(filter_fourier, len(y_values))


    plt.plot(x_values, y_values)
    """plt.plot(x_values, [x+1 for x in new])"""
    plt.plot(x_values, new_y)

    plt.savefig("clean_plot.png")
    plt.show()



def filter_with_freq(fourier, freq):
    amp = 0.2 ##noise amplitude
    if abs(freq)>amp:
        return 0
    else:
        return fourier



main()  # calls your main function
