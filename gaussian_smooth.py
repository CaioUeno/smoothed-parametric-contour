import numpy as np

def correlation(signal, filter):
    '''
    Correlation of given signal by given filter.
    '''

    signal_size = signal.shape[0]
    filter_size = filter.shape[0]

    half_filter_size = filter_size // 2
    # padding the signal
    signal_padded = np.concatenate([np.zeros(half_filter_size), signal, np.zeros(half_filter_size)])

    signal_filtered = np.zeros(signal_size)
    for index in range(signal_size):
            signal_filtered[index] = signal_padded[index:index+filter_size] @ filter

    return signal_filtered

def gaussian_filter_1d(filter_size, sigma):
    '''
    Creates a gaussian filter with sigma parameter and shape equals to filter_size.
    '''
    x = np.linspace(-3*sigma, 3*sigma, filter_size)
    gaussian_filter = np.exp(-x**2 / (2*sigma**2))
    gaussian_filter = gaussian_filter / gaussian_filter.sum() # to ensure it sums up to 1

    return gaussian_filter

def gaussian_smooth_1d(signal, filter_size, sigma):
    '''
    It smooths a signal using a gaussian filter.
    signal: 1-dimensional numpy array.
    sigma: sigma parameter to gaussian filter.

    Returns also a 1-dimensional numpy array.
    '''

    gaussian_filter = gaussian_filter_1d(filter_size, sigma)
    return correlation(signal, gaussian_filter)
