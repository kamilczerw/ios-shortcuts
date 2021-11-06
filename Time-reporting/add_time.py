import dialogs
import sys
import console
import webbrowser
import report_time

def main():
	console.clear()
	hours = dialogs.input_alert('Worked hours', 'hours', '08:00')
	# callback = sys.argv[-1] + '?x-source=Pythonista3&hours=' + hours

	date, hours = report_time.validate_args()
	
	# print(callback)
	
	# webbrowser.open(callback)
	

if __name__ == '__main__':
	main()
