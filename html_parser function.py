"""
20/01/21 - HTML Parser using Python - James Besant -  First Attempt (No importing of modules)
Accepts a string representation of an HTML document and prints
result "Valid" if all tags are paired (opening tags have a corresponding
closed tag) or "Invalid" if tags are not paired. Will also print "Invalid"
if the rule "closing the most recent tag before closing older tags" is not
followed.

Assumed that self-closing tags are in the format <br/> like in the example.

Also did not add a main() since I did not know the format it would be tested.

"""
def html_parser(html_string):
    
    tags_list = []
    sc_tags = []
    sc_tag_names = ["area", "base", "br", "col", "embed", "hr", "img", "input" \
                    "link", "meta", "param", "source", "track", "wbr"]
    
    previous = None
    
    valid = "Valid"
    invalid = "Invalid"
    
    for i in html_string.split():
        tag_count = i.count("<")
        while tag_count != 0:
            if i.find("<") == -1 or i.find(">") == -1 or i.find(">") == i.find("<") + 1:
                return invalid

            tag = i[i.find("<") + 1:i.find(">")]
            
            if tag[0] == "/":
                if len(tags_list) > 0:
                    previous = tags_list[-1]
                else:
                    return invalid
                if previous == tag[1:]:
                    tags_list.pop()
                else:
                    return invalid
                
            elif tag[-1] == "/" and tag[:-1] in sc_tag_names:
                sc_tags.append(tag)
                
            else:
                tags_list.append(tag)

            tag_count -= 1
            i = i[i.find(">") + 1:]
    
    if len(tags_list) > 0:
        return invalid

    return valid

