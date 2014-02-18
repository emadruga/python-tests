from lxml import etree
import re

parser = etree.HTMLParser()


page = "ventilador-walmart.html"

tree = etree.parse(page, parser)

#root = tree.getroot();
#print etree.tostring(root, pretty_print=True)

#myList = tree.xpath("//span[@class='webkit-html-attribute-value' and text()='int']/text()");
#myList = tree.xpath("/html/body/div/table/tbody/tr[4]/td[2]/text()[197]");
myList = tree.xpath("//tr/td/text()");

#print "List: ", myList

i = 0
while i < len(myList) :
    	start = re.findall(r"De:", myList[i])
	if (len(start) > 0):
            print  myList[i+6], myList[i+7]
        i += 1
