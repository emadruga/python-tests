from lxml import etree
import re

parser = etree.HTMLParser()


page = "../sample-data/ventilador-americanas.html"

tree = etree.parse(page, parser)

root = tree.getroot();
print etree.tostring(root, pretty_print=True)

myList = tree.xpath("//td[@class='webkit-line-content' and text()='R$']/text()");

print "List: ", myList

count = 0
for str in myList:

	price = re.findall(r"[-+]?\d*\,\d+|\d+", str)

	if (len(price) > 0):
		count += 1
		if (count > 1) :
			print "Price: ", price[0]
