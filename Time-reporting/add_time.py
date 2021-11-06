import dialogs
import sys
import console
import webbrowser
import report_time
import argparse

def update_popup():
	dialogs.input_alert('Update', '')

def insert_popup():
	dialogs.input_alert('Worked hours', 'hours', '08:00')

def main():
	console.clear()
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--update', action='store_true')
	parser.add_argument('callback', type=str)
	
	args = parser.parse_args()
	
	print(args)
	
	if args.update:
		update_popup()
	else:
		insert_popup()
	
	#hours = dialogs.input_alert('Worked hours', 'hours', '08:00')
	# callback = sys.argv[-1] + '?x-source=Pythonista3&hours=' + hours

	#date, hours = report_time.validate_args()
	
	# print(callback)
	
	# webbrowser.open(callback)
	

if __name__ == '__main__':
	main()
