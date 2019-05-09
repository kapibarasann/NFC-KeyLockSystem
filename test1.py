import nfc
import csv

def connected(tag):
	print tag
	card_info = tag
	with open('data.csv', 'a') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(str(tag))
#		print str(tag)
	f.close()
	return tag

def main():

	clf = nfc.ContactlessFrontend('usb')
	clf.connect(rdwr={'on-connect': connected}) # now touch a tag
#	card_info = connected
	print "card_info: "
	print(card_info)
	clf.close()



if __name__ == '__main__':
	main()
