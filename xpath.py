"""
XPath stands for "XML Path Language."
it describes where elements are located in the document's structure and
finds elements based on their relationship to others elements.  XPath is more flexible and can
select elements based on things like their text content.
"""
#Navigating Parent Elements
"""
In XPath, //.. is used to navigate up one level in the DOM tree to find the parent element of the current node. 
It can be helpful when you want to interact with or locate the parent of a specific child element.
 the <div> element with class="input-container" (which is the parent) by referencing its child <input> element with the id="from". So, this will be the XPath:

//input[@id='from']//..
"""
#XPath Syntax
'//tag[@attribute="value"]'
#// means that we are searching anywhere in the HTML document
#tag represents the HTML tag of the element you're looking for (div, input, a, etc.).
#[@attribute='value'] is called a predicate. It filters elements based on an attribute and its value.
# The @ symbol refers to an HTML attribute of an element (id, class, name, type, etc.).

#Line of code from Urban Routes for the "From" field
'<input id="from" class="input" type="text" placeholder="East 2nd Street, 601" value="">'
#Xpath locator
'//input[@id="from"]'
#Anoter example
'<div class="dst-picker">.'
#Xpath
'//div[@class="dst-picker"]'

#Xpath Search Techniques
"""
When searching for an element located in multiple parent containers. Create the 
parent container Xpath, then create the element expression next to it.
"""
#example
'//tag[@attribute="value"]//tag[@attribute="value"]'
#Task
'Parent Container //div[@class="payment-picker"] and Element Expression //div[@class="modal"]'
"//div[@class='payment-picker']//div[@class='modal']"

#Element by its Index
"""
The parent container holds multiple of the same element expression. To distinguish between the elements
use the index of the element at the end of the expression (e.g. "[1]", //tag[@attribute="value"][index] )
"""
#Example
"Finding a particular driver mode in Urbarn Routes app"
'For Fastest //div[@class="mode"][1] , and for Custom  //div[@class="mode"][2]'

#Finding a Link containing a URL
'//a[contains(@href, "https://www.google.com/intl")]'

#Other Methods to locate Elements
#text() - Finds elements based on the text they contain
"//label[text()='From']"
#contains() - Finds elements containing partial text; Finds multiply elements with the instance of the text
"//label[contains(text(),'From')]" # Also known as the Relative Path

#Absolute Path and Relative Path
#Absolute -  provides the full path from the root of the HTML <html> all the way to the target element.
# Very long, and fragile. Accidentally, adding or removing an element can break the path
#Example
"""/html/body/div[@id='root']/div[@class='app']/div[@class='workflow']/div[@class='dst-picker']' 
    '/div[@class='dst-picker-row']/div[@class='input-container']/input[@id='from']
"""
#Relative - Finds an element based on a simpler path, starting from a specific element in the HTML
#begining with // "search" followed by attribute and value, what you've been learning
#Example
'//input[@id="from"]'
