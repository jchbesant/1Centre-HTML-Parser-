"""
20/01/21 - HTML Parser using Python - James Besant -  First Attempt (No importing of modules)
Accepts a string representation of an HTML document and prints
result "Valid" if all tags are paired (opening tags have a corresponding
closed tag) or "Invalid" if tags are not paired. Will also print "Invalid"
if the rule "closing the most recent tag before closing older tags" is not
followed.

Assumed that self-closing tags are in the format <br/> like in the example.

I also did not want to import any Python modules which helped with HTML validating or parsing.

"""
def html_parser(html_string):
    
    tags_list = []
    
    sc_tags = []
    
    #Names of all the self-closing tags which will be disregarded in the programme
    sc_tag_names = ["area", "base", "br", "col", "embed", "hr", "img", "input" \
                    "link", "meta", "param", "source", "track", "wbr"]
    
    previous = None
    
    valid = "Valid"
    invalid = "Invalid"
    
    #Loop through the string to until all tags are found
    for i in html_string.split():
        tag_count = i.count("<")
        while tag_count != 0:
            if i.find("<") == -1 or i.find(">") == -1 or i.find(">") == i.find("<") + 1:
                return invalid

            tag = i[i.find("<") + 1:i.find(">")]
            
            #Conditions to check and match closing tags to open tags
            if tag[0] == "/":
                if len(tags_list) > 0:
                    previous = tags_list[-1]
                else:
                    return invalid
                if previous == tag[1:]:
                    tags_list.pop()
                else:
                    return invalid
                
            #Check and store self-closing tags - removed from validity check
            elif tag[-1] == "/" and tag[:-1] in sc_tag_names:
                sc_tags.append(tag)
                
            #If tag is open add it to the list   
            else:
                tags_list.append(tag)
                
            #Resest counter and i for iteration
            tag_count -= 1
            i = i[i.find(">") + 1:]
            
    #Check if there are more tags left unmatched - if so return "Invalid"
    if len(tags_list) > 0:
        return invalid
    
    #If all conditions are met return Valid
    return valid

def main():
    """
    test = html_parser('HTML document')
    #print(test)
    
    """

main()
