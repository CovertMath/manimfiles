from manim import *
import numpy as np #used for sin and cos function


class ArcLengthExp(Scene): #names the mp4 file "ArcLengthExp"
    def construct(self):
        ax = Axes(x_range=[-3, 3], y_range=[-4, 4], color=YELLOW, tips=True, axis_config={"numbers_to_include":[-2,-1,1,2]})
        curve = ax.plot(lambda x: 2*(x+1)*np.sin(x)*np.cos(x), x_range=[-2,2], color=RED) #defines the curve

        self.play(Create(ax)) #creates axes
        self.play(Create(curve)) #then plots the curve

        L = [1,2,4,8] #(1/4) the number of times to split interval [-2,2], so k = 1 splits into 4 pieces, k = 2 splits into 8 pieces, etc
        for k in L:
            for i in range(-2*k, 2*k): 
                point = Dot(ax.coords_to_point(i/k,2*(i/k+1)*np.sin(i/k)*np.cos(i/k)), radius=0.06, color=BLUE) #defines points that are plotted on curve
                point2 = Dot(ax.coords_to_point((i+1)/k,2*((i+1)/k+1)*np.sin((i+1)/k)*np.cos((i+1)/k)), radius=0.06, color=BLUE) #defiens right endpoint for each line
                line = Line(start=point, end=point2, color=GREEN) #creates line between these two points
                self.add(point)
                self.add(point2)
                self.play(Create(line), run_time=(1/2)**k) #runtime decreasing for succesive values of k
                self.wait(0.25)
            self.clear() #after each iteration, it erases previous lines
            self.add(ax, curve) #and adds in curve
            self.wait(2)