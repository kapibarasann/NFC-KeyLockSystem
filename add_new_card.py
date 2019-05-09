import nfc
import csv

def connected(tag):
	print tag
	flag = True
	with open('/home/pi/Key/data.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if str(tag) == ''.join(row):
				flag = False
				print "This Card is already Registered"
				break
			else:
				continue
	f.close()

	if flag:
		with open('/home/pi/Key/data.csv', 'a') as f:
			writer = csv.writer(f, lineterminator='\n')
			writer.writerow(str(tag))
		f.close()

	return tag

def main():

	clf = nfc.ContactlessFrontend('usb')
	print "Touch a card"
	clf.connect(rdwr={'on-connect': connected}) # now touch a tag
	card_info = connected
	clf.close()



if __name__ == '__main__':
	main()
