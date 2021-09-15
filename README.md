# Fourier-Application

This application was developed in order to be able to calculate the Fourier Series coefficients more easily and to see the wave graph. It was developed toghether with Draghici Andrei under the supervision of Dr. Ing. Philip Coanda. The graphical interface was created using the Tkinter framework, which allows the placement of text boxes, input, dropdown and buttons. To make all the necessary calculations, the application needs the user to enter the necessary data: frequency, number of samples, number of waves, number of periods, amplitude and signal type (Sawtooth, Rectified, Cosine, Pulse, Square, Triangle). The application also allows you to display a desired wave by entering its number in the "Afiseaza unda" box, and the application will create a separate graph with the desired wave. 
</br></br>
The functions "fierastrau()", "rectificat()", "cosinus()", "pulse()", "square()" and "triangle()"  represent the calculations for each type of wave, returning the calculated an and bn vectors. The plot function creates the three graphs: the first five waves, the sum of the waves and the wave chosen by the user.
</br></br>
In the "aplicatie()" function we check what kind of signal it is and call the functions that make the necessary calculations for that signal. In the "update()" function we reset all the values received from the user and call the "aplicatie()" function. The variable "root" is the foundation of the application over which we can put the text and inputs from the user.
</br></br>
The application has seven inputs through which the user enters data into the application. Frequency input represents the frequency in Hz, the sample rate represents the number of samples per second, the number of waves, the number of periods, the amplitude and the wave display represents a function that displays a certain selected wave.

### The result:
![FourierApp](https://github.com/brittleru/Fourier-Application/blob/master/aplicatie.png?raw=true)
