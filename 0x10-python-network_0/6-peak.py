#!/usr/bin/python3
""" method that get the max peak in teh list of integers """


def find_peak(list_of_integers):
    """ return the peak """
    l = list_of_integers
    peaks = []
    for i in range(1, len(list_of_integers)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            peaks.append(l[i])
        if l[i] < l[i-1] and l[i] < l[i+1]:
            peaks.append(l[i])
        if l[i] == l[i-1] and l[i] == l[i+1]:
            peaks.append(l[i])
    if len(peaks) == 0:
        return None
    return max(peaks)
