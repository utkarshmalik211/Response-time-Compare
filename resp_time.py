
import pycurl
from io import BytesIO
from random import randint
from time import sleep, gmtime, strftime
# Print iterations progress
print("This process is daunting at times..... Grab a coffee till it finishes.")
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    if iteration == total: 
        print()


rtimes = open("results.txt","a+")
queries=open("queries.txt","r").read().split("\n")
k=0
while(k<=80):
	#Api.ai test
	time_elapsed_api = 0
	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(pycurl.HTTPHEADER, ['Authorization:Bearer "api.ai key"'])
	count=0
	printProgressBar(count, len(queries), prefix = 'Progress:', suffix = 'Complete', length = 50)
	for i in queries:
		sleep(randint(0,2))
		curl="https://api.api.ai/v1/query?v=20150910&query="+i.replace(" ","%20")+"&lang=en&sessionId=456789032"
		c.setopt(c.URL, curl)
		c.setopt(c.WRITEDATA, buffer)
		c.perform()
		body = buffer.getvalue()
		# print(body)
		count+=1
		printProgressBar(count, len(queries), prefix = 'Progress:', suffix = 'Complete' + " Current : " + str(c.getinfo(c.TOTAL_TIME)), length = 50)
		time_elapsed_api = time_elapsed_api + float(c.getinfo(c.TOTAL_TIME))
		# print(c.getinfo(c.TOTAL_TIME))
	print("\n"+str(time_elapsed_api))
	c.close()

	#wit.ai test
	time_elapsed_wit = 0
	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(pycurl.HTTPHEADER, ['Authorization:Bearer wit.ai key'])
	count=0
	printProgressBar(count, len(queries), prefix = 'Progress:', suffix = 'Complete', length = 50)
	for i in queries:
		sleep(randint(0,2))
		curl="https://api.wit.ai/message?v=20170307&q="+i.replace(" ","%20")
		c.setopt(c.URL, curl)
		c.setopt(c.WRITEDATA, buffer)
		c.perform()
		body = buffer.getvalue()
		# print(body)
		count+=1
		printProgressBar(count, len(queries), prefix = 'Progress:', suffix = 'Complete' + " Current : " + str(c.getinfo(c.TOTAL_TIME)), length = 50)
		time_elapsed_wit = time_elapsed_wit + float(c.getinfo(c.TOTAL_TIME))
		# print(c.getinfo(c.TOTAL_TIME))
	print()	
	print("\n"+str(time_elapsed_wit))
	c.close()

	rtimes.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " Wit : "+str(time_elapsed_wit)+"| Api : "+str(time_elapsed_api)+"\n")
	k+=1
