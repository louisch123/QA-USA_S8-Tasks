"""
What exactly are locators and why are they used?
A locator is like an “address” that helps identify and locate elements within the HTML of a webpage.
It's like an instruction that says, "Look here to find this web element.” So, "locator" is a pretty apt name!

This comes into play because during automation testing, we need to find an element before interacting with it:
clicking a button, typing text, or reading text.

CSS Selector and XPath are the most popular methods for locating elements in HTML.
Using CSS selectors and XPath is like having two different routes to find the same element. Let’s focus on CSS selectors first.
"""

"""
Locator Strategy
1: Always use IDs if available: Using a unique ID is the fastest and most reliable way to locate an element. 
But sometimes elements do not have ids, or even if they do, they may be dynamic, that is, ids that change with each refresh; in this case, we cannot use ids.

2: Use class or name as a second alternative: Make sure the class name or name is not available or unique; 
if it is not, we will look at other alternatives.

3: Use CSS Selector as a custom locator: CSS Selector is faster than XPath, s
so it should be the first preferred custom locator. However, it has fewer features than XPath.

4: Use XPath as a final option: If you need to locate with text, use methods such as contains,
or move from a child element to a parent element, XPath will be a great final savior. 
Although XPath has a slower performance than CSS Selector, you can locate any element with XPath.
"""
# CSS Selector syntax when locating id elements
'tag[attribute="value"]'
#The most reliable way to locate an element is to use its id because the
# id attribute will be unique for every element.However, not all elements have ids. In such cases,
# other selectors, like class, might also be reliable.

# Locating Class elements.
'tag[class="value"]'

#Short notation to target elements by their class or id attributes
"""
. is used for classes. For example, .button selects all elements with the class “button.”
# is used for ids. For example, #header targets the single element with the id “header.”

Examples:
short notation for the locator div[class='dst-picker']
div.dst-picker
short notation for locator div[class='input-container']
div.input-container
input[id='from']  <!-- Long notation -->
input#from        <!-- Short notation -->
div[class='dst-picker']  <!-- Long notation -->
div.dst-picker           <!-- Short notation -->
"""
#Parent to child Selectors
"""
urpose: Locate elements by their relationship to parent elements

Structure: Use > symbol to indicate parent-child relationship

Example:

div.input-container>#from
"""
# Various Selector Types
"""
span.logo-disclaimer           <!-- Class selector -->
label[for='from']             <!-- Attribute selector -->
div#root                      <!-- ID selector -->
div.input-container>#from     <!-- Parent-child selector -->
"""

