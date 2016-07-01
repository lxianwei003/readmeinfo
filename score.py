#!/usr/bin/python3
import matplotlib.pyplot as plt  
import numpy as np


rcdmaxent = [  0.618195 ,       0.5 ,  0.499407 ,  0.475464 ,  0.291025 ,   0.64699 ,  0.533252 ,  0.630584 ,  0.582332 ,  0.714211 ,  0.446934 ,  0.836402 ,   0.43164 ,  0.495291 ,  0.750807 ,  0.897257 ,  0.736378 ,   0.72663 ,  0.341962 ,   0.54527 ,  0.715235 ,  0.579158 ,  0.442005 ,  0.490978 ,  0.546903 ,  0.721401 ,  0.914477 ,  0.673361 ,  0.608393 ,  0.518563 ,  0.556357 ,  0.507665 ,  0.547608 ,  0.524923 ,  0.590489 ,  0.324785 ,  0.579141 ,  0.723372 ,  0.528471 ,  0.752544 ,  0.610655 ,  0.560761 ,  0.592781 ,   0.45687 ,  0.605916 ,  0.593274 ,  0.666223 ,   0.48223 ,  0.807798 ,  0.560834 ,  0.561024 ,  0.548417 ,  0.613213 ,  0.625341 ,  0.636413 ,   0.73764 ,  0.740791 ,  0.582378 ,  0.616963 ,  0.742555 ,  0.498306 ,  0.488396 ,  0.744583 ,  0.442592 ,  0.583583 ,   0.58285 ,  0.319754 ,  0.727547 ,  0.696062 ,   0.70471 ,  0.663955 ,  0.656997 ,  0.728253 ,  0.539598 ,  0.862155 ,  0.488122 ,  0.604098 ,  0.559336 ,  0.885225 ,  0.681861 ,  0.483061 ,  0.683288 ,  0.607814 ,  0.597732 ,  0.594832 ,  0.517326 ,  0.778566 ,  0.799692 ,   0.83826 ,  0.730255 ,  0.491933 ,   0.75932 ,   0.48931 ,  0.620653 ,  0.773783 ,  0.502155 ,  0.795698 ,  0.897035 ,  0.531087 ,   0.62956 ,  0.633817 ,  0.634289 ,  0.370456 ,  0.624956 ,  0.442294 ,  0.676712 ,  0.595919 ,  0.768043 ,   0.68354 ,  0.572702 ,  0.709084 ,  0.645543 ,  0.718731 ,  0.513655 ,   0.79798 ,  0.624758 ,  0.558179 ,   0.76575 ,  0.687411 ,  0.640429 ,  0.662045 ,  0.523776 ,  0.586929 ,  0.506284 ,  0.687138 ,  0.407486 ,  0.719326 ,  0.828335 ,  0.520648 ,   0.83651 ,  0.512537 ,  0.525839 ,    0.7359 ,  0.814928 ,  0.585774 ,  0.511076 ,  0.632358 ]
 
rcdsvd = [  0.217293 , -0.001805 ,   0.01006 ,   0.00546 ,  0.012378 ,  0.007662 ,  0.008687 ,   0.00505 ,   0.00507 ,  0.165127 ,  0.008731 ,  0.190582 ,   0.01841 ,  0.015161 ,  0.008718 ,  0.129541 ,  0.028664 ,  0.057846 ,  0.007595 ,  0.006859 ,  0.004568 ,  0.001695 ,  0.002631 ,   0.00274 ,  0.004678 ,   0.00375 ,  0.004348 ,  0.003761 ,  0.078054 ,  0.011341 ,  0.015328 , -0.001326 ,   0.00321 ,  0.007048 ,  0.011829 ,  0.014786 ,  0.006148 ,  0.033559 ,  0.048803 ,  0.007238 ,  0.005134 ,   0.01144 ,  0.043573 ,  0.004994 ,  0.012046 ,  0.011426 ,  0.002046 ,  0.003603 ,  0.040453 ,  0.005679 ,  0.000086 ,  0.056968 ,  0.002005 ,  0.003761 ,  0.012561 ,  0.014637 ,  0.007501 ,  0.005075 ,  0.063614 ,  0.005551 ,  0.005936 ,  0.003213 ,  0.051848 ,  0.042358 ,   0.00288 ,  0.015557 ,  0.011628 ,  0.009848 ,  0.021417 ,  0.012157 ,  0.005069 ,  0.005552 ,  0.007558 ,   0.01103 ,  0.005019 ,  0.008788 ,  0.007548 ,  0.007484 ,  0.029173 ,  0.036732 ,  0.004584 ,  0.005592 ,  0.007696 ,  0.003937 , -0.000689 ,  0.027463 ,  0.094861 ,  0.007848 ,  0.078271 ,  0.005461 ,   0.00367 ,  0.065258 ,  0.008113 ,  0.002476 ,  0.006651 ,   0.00917 ,  0.005708 ,  0.213948 ,  0.031416 ,  0.010406 ,  0.001665 ,  0.003354 ,  0.025155 ,  0.056943 ,  0.044375 ,   0.00843 ,  0.010397 ,  0.031697 ,  0.029986 ,  0.005105 ,  0.006526 ,  0.009076 ,   0.06498 ,  0.071068 ,   0.14703 ,  0.008623 ,  0.080796 ,  0.130478 ,  0.125116 ,  0.036539 ,  0.008824 ,  0.006213 ,  0.006224 ,  0.002354 ,  0.008995 ,  0.007297 ,  0.010318 ,  0.107581 ,  0.011984 ,  0.136966 ,  0.006091 ,  0.017436 ,  0.027976 ,  0.073401 ,  0.038751 ,  0.058414 ,   0.00679 ]

x = np.linspace(0, len(rcdsvd), len(rcdsvd) )
y = np.array(rcdmaxent, dtype=np.double)
y = (y-np.min(y) ) / np.ptp(y)
y2 = np.array(rcdsvd, dtype=np.double)
y2 = (y2-np.min(y2) ) / np.ptp(y2)

plt.plot(x,  y, 'g', x,  y2+0.4, 'b')   #为了好看特定修正对齐的哦
plt.legend(('rcdmaxent', 'rcdsvd'),
           loc='upper right')

plt.show()