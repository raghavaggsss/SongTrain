#! /usr/bin/env python

from aubio import source
from aubio import pitch as p

def freq_array(filename):
    downsample = 1
    samplerate = 44100 // downsample

    win_s = 4096 // downsample # fft size
    hop_s = 512  // downsample # hop size

    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = p("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    times=[]

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        pitch = pitch_o(samples)[0]
        pitch = int(round(pitch))
        #if confidence < 0.8: pitch = 0.
        time = total_frames / float(samplerate)
        #print("%f %f" % (time, pitch))
        times +=[time]
        pitches += [pitch]
        total_frames += read
        if read < hop_s: break
    return pitches , times
 
