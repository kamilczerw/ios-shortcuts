import dialogs
import sys
import console
import webbrowser

def main():
	console.clear()
	hours = dialogs.input_alert('Worked hours', 'hours', '08:00')
	#print(hours)
	callback = sys.argv[-1] + '?x-source=Pythonista3&hours=' + hours
	
	print(callback)
	
	webbrowser.open(callback)
	

if __name__ == '__main__':
	main()
