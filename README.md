# 1Centre - HTML-Parser - James Besant
20/01/21 

HTML Parser using Python - First Attempt (No importing of modules)
Accepts a string representation of an HTML document and prints
result "Valid" if all tags are paired (opening tags have a corresponding
closed tag) or "Invalid" if tags are not paired. Will also print "Invalid"
if the rule "closing the most recent tag before closing older tags" is not
followed.

Using a Stack and the LIFO concept if a closing tag is put in the list after a
matching opening tag they have therefore closed successfully it will remove both tags
from the list. The HTML document is therefore Valid if all the tags are popped and
the list is empty.


Assumptions:
- A tag must have a minimum length: 3 - since the smallest tags consist of
a less-than sign; charachter; greater-than sign e.g. <x> . Any length less
than this for a tag will give an Invalid output. This will also give tags with
extra whitespaces an Invalid output such as "<div >".
