Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> fig, ax= plt.subplots()
>>> data={
	"Abby":3.7,
	"Benjamin":3.5,
	"Claire":3.8
	"Dennis":3.1
	
SyntaxError: invalid syntax
>>> data={
	"Abby":3.7,
	"Benjamin":3.5,
	"Claire":3.8,
	"Dennis":3.1,
	"Eleanor":2.8,
	"Fiona": 3.0
	}
>>> x_axis_data=data.keys()
>>> y_axis_data=data.values()
>>> ax.bar(x_axis_data, y_axis_data)
<BarContainer object of 6 artists>
>>> ax.set(ylim=[0,4.0],
       ylabel= 'Grade Point Average',
       xlabel= 'Student',
       title= 'GPAs for Junior Class')
[(0.0, 4.0), Text(0, 0.5, 'Grade Point Average'), Text(0.5, 0, 'Student'), Text(0.5, 1.0, 'GPAs for Junior Class')]
>>> plt.show
<function show at 0x7fbd74b8d8b0>
>>> plt.show()
