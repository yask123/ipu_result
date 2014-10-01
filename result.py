"""This application has been written by Yask Srivastava! """
import os
from urllib.request import urlopen
data =''
link=''
for line in urlopen('http://ggsipuresults.nic.in/ipu/results/resultsmain.htm'):
	data = data+str(line)

run = True
start=0
while(run):
	try :
		branch = input('What branch ?')
		start_Branch=data.find(branch,start)

		end_row=data.find('</td>',start_Branch)
		start_search_pdf=data.find('<a href="',end_row)+9

		Sem_check=data.find('8th Sem',end_row)
		if Sem_check < start_search_pdf:
			print ('Voila!')
			print ('Your result declared , Generating Link :')
			end_search_pdf=data.find('"',start_search_pdf+9)
			print ('http://ggsipuresults.nic.in/ipu/results/'+data[start_search_pdf:end_search_pdf])
			link='http://ggsipuresults.nic.in/ipu/results/'+data[start_search_pdf:end_search_pdf]
			break
		else:
			start=end_row+5
			if  start > len(data)-10:

				break	




	except:
		print ('Result Not yet Declared')
		break	
print('Starting Automatic Download , Please wait while Download finishes.')
command='wget '+'http://ggsipuresults.nic.in/ipu/results/'+data[start_search_pdf:end_search_pdf]
os.system(command)


