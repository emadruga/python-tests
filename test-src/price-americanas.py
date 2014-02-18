#!/usr/bin/python
from lxml import etree
import re

def str2float(str) :
	response = float(str)
	return response


parser = etree.HTMLParser()


page = "../sample-data/ventilador-americanas.html"

tree = etree.parse(page, parser)

#root = tree.getroot();
#print etree.tostring(root, pretty_print=True)

tree.write("out.xml")

myList = tree.xpath("//td[@class='webkit-line-content' and text()='R$']/text()");

print "List: ", myList

prices = []
for str in myList:

	price = re.findall(r"[-+]?\d*\,\d+|\d+", str)
	if (len(price) > 0):
		prices.append(price[0])
			
priceStr = prices[-1].replace(",",".")
priceFloat = str2float(priceStr)
print "Price (float): %+10.3f" % priceFloat
