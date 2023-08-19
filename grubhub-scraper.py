import urllib.request
url = "file:///Users/christopherzaman/Desktop/un-grub.html"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response, "lxml")

#grubhub scrapper below
''' 
The following code stores three elements each in its own array from GrubHub:Item|Description|Price.
Then, it prints each array and html tags formatted so that the item, description and price are wrapped
by the html.
Finally, the printed result can be copy and pasted into an html file.
'''
#grubhub scrapper
# get all <a tag> elements with a class of 'menuItem-name', add it to a array 
itemList=[]
for tag in soup.find_all('a', class_=['menuItem-name']):
    item = tag.text
    if tag not in itemList:
        itemList.append(tag.text)
#print(itemList)

# get all <span> tag elements with a class of 'menuItem-displayPrice', add it to array
priceList=[]
for t in soup.find_all('span', class_=['menuItem-displayPrice']):
    price = t.text
    if t not in priceList:
        priceList.append(t.text)
#print(priceList)
#print(t.text)

# get all <p> tag elements with a class of 'u-text-secondary', add it to array
descripList=[]
for g in soup.find_all('p', class_=['u-text-secondary']):
    price = g.text
    if g not in descripList:
        descripList.append(g.text)

# get all titles for menu sections        
for tag in soup.find_all('h3', class_=['menuSection-title']):
    title = tag.text
#    print(title)

# write the html you'd need to wrap the lists with
html="<div class=\"col-lg-4 mb-4 mb-lg-0 col-md-6\" data-aos=\"fade-up\" data-aos-delay=\"20\"><ul class=\"border my-custom-list-item-styles\"><li><p class=\"text-black\">"
html2="</p></li><p class=\"my-custom-description-styles\">"
html3="</p><li><h6 class=\"card-price text-success\">"
html4="</h6></li></ul></div>"

#format the result by inserting the pieces where they belong to make an html file
res = "\n".join("{} {} {} {} {} {} {}".format(html, x, html2, z, html3, w, html4) for x, z, w in zip(itemList, descripList, priceList))
print(res) 
