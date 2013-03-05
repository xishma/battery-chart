battery-chart
=============

A python script which monitors your laptop battery status, and draws a battery-level-per-time chart with html.
Current project, works with opening create_log.py, which takes battery status and time delta, and puts it in a file. when you open log_to_chart.py, it opens the created logs, and puts them in a JS file with proper format, and you can see the charts with opening Chart.htm .

ToDo:
	*use a single file for all logs.
	*use a date-time for log names, instead of a number.
	*extend project for linux and mac platforms.
	*develop a dashbord in chart.htm .
	

=============
to use this project, you should have python 2.7, and pywin32 (for windows) installed.
you can find them in this addresses:
Python 2.7:	http://www.python.org/download/releases/2.7/
pywin32:	http://sourceforge.net/projects/pywin32/files/pywin32/

for drawing the charts, project uses HighCharts JS library, which exsits in project files.