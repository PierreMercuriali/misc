import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import math

# The parametrized function to be plotted
#def f(t, amplitude, frequency):
    #return amplitude * np.sin(2 * np.pi * frequency * t)
    
def path(t, A1, f1, p1, d1, A2, f2, p2, d2):
	return A1 * math.sin(t * f1 + p1) * math.exp( (-1) * d1 * t) + A2 * math.sin(t * f2 + p2) * math.exp( (-1) * d2 * t)


TIME	= np.arange(0,10,.001)

# Define initial parameters
#init_amplitude = 5
#init_frequency = 3
init_AMPLITUDE1	= 1
init_AMPLITUDE2	= 0
init_DAMPING1	= 1
init_DAMPING2	= 1
init_FREQUENCY1	= 60
init_FREQUENCY2	= 5
init_PHASE1		= 0
init_PHASE2		= 0

init_AMPLITUDE3	= 1
init_AMPLITUDE4	= 0
init_DAMPING3	= 1
init_DAMPING4	= 1
init_FREQUENCY3	= 50
init_FREQUENCY4	= 5
init_PHASE3		= 0
init_PHASE4		= 0

# Create the figure and the line that we will manipulate
plt.rcParams['axes.facecolor'] = (.1,.1,.1)
fig, ax = plt.subplots()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
X	= [path(x, init_AMPLITUDE1, init_FREQUENCY1, init_PHASE1, init_DAMPING1, init_AMPLITUDE2, init_FREQUENCY2, init_PHASE2, init_DAMPING2) for x in TIME]
Y	= [path(x, init_AMPLITUDE3, init_FREQUENCY3, init_PHASE3, init_DAMPING3, init_AMPLITUDE4, init_FREQUENCY4, init_PHASE4, init_DAMPING4) for x in TIME]
line, = plt.plot(X,Y, lw=.4, color='red')
#ax.margins(x=0)
axcolor = 'lightgoldenrodyellow'
# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.3, bottom=0.3)

#
#	FREQUENCIES
#

# Make a horizontal slider to control the frequency 1.
axfreq1 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
freq1_slider = Slider(
    ax=axfreq1,
    label='Frequency 1 [Hz]',
    valmin=0,
    valmax=100,
    valinit=init_FREQUENCY1,
)
# Make a horizontal slider to control the frequency 2.
axfreq2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
freq2_slider = Slider(
    ax=axfreq2,
    label='Frequency 2 [Hz]',
    valmin=0,
    valmax=100,
    valinit=init_FREQUENCY2,
)
# Make a horizontal slider to control the frequency 3.
axfreq3 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
freq3_slider = Slider(
    ax=axfreq3,
    label='Frequency 3 [Hz]',
    valmin=0,
    valmax=100,
    valinit=init_FREQUENCY3,
)
# Make a horizontal slider to control the frequency 4.
axfreq4 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
freq4_slider = Slider(
    ax=axfreq4,
    label='Frequency 4 [Hz]',
    valmin=0,
    valmax=100,
    valinit=init_FREQUENCY4,
)

#
#	AMPLITUDES
#


# Make a vertically oriented slider to control the amplitude 1.
axamp1 = plt.axes([0.1, 0.3, 0.0225, 0.63], facecolor=axcolor)
amp1_slider = Slider(
    ax=axamp1,
    label='Amp1',
    valmin=0,
    valmax=2,
    valinit=init_AMPLITUDE1,
    orientation="vertical"
)
axamp2 = plt.axes([0.15, 0.3, 0.0225, 0.63], facecolor=axcolor)
amp2_slider = Slider(
    ax=axamp2,
    label='Amp2',
    valmin=0,
    valmax=2,
    valinit=init_AMPLITUDE2,
    orientation="vertical"
)
axamp3 = plt.axes([0.2, 0.3, 0.0225, 0.63], facecolor=axcolor)
amp3_slider = Slider(
    ax=axamp3,
    label='Amp3',
    valmin=0,
    valmax=2,
    valinit=init_AMPLITUDE3,
    orientation="vertical"
)
axamp4 = plt.axes([0.25, 0.3, 0.0225, 0.63], facecolor=axcolor)
amp4_slider = Slider(
    ax=axamp4,
    label='Amp4',
    valmin=0,
    valmax=2,
    valinit=init_AMPLITUDE4,
    orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val):
	X	= [path(x, amp1_slider.val, freq1_slider.val, init_PHASE1, init_DAMPING1, amp2_slider.val, freq2_slider.val, init_PHASE2, init_DAMPING2) for x in TIME]
	Y	= [path(x, amp3_slider.val, freq3_slider.val, init_PHASE3, init_DAMPING3, amp4_slider.val, freq4_slider.val, init_PHASE4, init_DAMPING4) for x in TIME]
	line.set_xdata(X)
	line.set_ydata(Y)
    #line.set_ydata(f(t, amp_slider.val, freq_slider.val))
	fig.canvas.draw_idle()


# register the update function with each slider
freq1_slider.on_changed(update)
freq2_slider.on_changed(update)
freq3_slider.on_changed(update)
freq4_slider.on_changed(update)
amp1_slider.on_changed(update)
amp2_slider.on_changed(update)
amp3_slider.on_changed(update)
amp4_slider.on_changed(update)

plt.show()
