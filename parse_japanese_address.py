from japanese_addresses import separate_address
import re

def parse_japanese_address(address):

    parsed = separate_address(address)
    
    pref = parsed.prefecture
    city = parsed.city
    
    unparsed = address.replace(pref+city, '') 
    town = ''
    remaining = ''
    for i, c in enumerate(unparsed):
        if c.isdigit():
            remaining = unparsed[i:]
            break
        town += c
        
    chome = ''
    block = ''
    
    pattern_1 = r'(\d+丁目)(\d+-\d+)'
    pattern_2 = r'(\d+丁目)(\d+)'
    pattern_3 = r'(\d+丁目)'
    pattern_4 = r'(\d+)-(\d+-\d+)'
    pattern_5 = r'(\d+-\d+)'
    pattern_6 = r'(\d+)'
    pattern_7 = r'(\d+丁目)(\d+)[番地]*[-]*(\d+)[号]*'
    
    if re.match(pattern_1, remaining): # '2丁目4-9'
        matched = re.findall(pattern_1, remaining)[0]
        chome, block = matched
    elif re.match(pattern_2, remaining): # '23丁目4'
        matched = re.findall(pattern_2, remaining)[0]
        chome, block = matched
    elif re.match(pattern_3, remaining): # '2丁目'
        matched = re.findall(pattern_3, remaining)[0]
        chome = matched
    elif re.match(pattern_4, remaining): # '22-2-2'
        matched = re.findall(pattern_4, remaining)[0]
        chome, block = matched
    elif re.match(pattern_5, remaining): # '7643-12'
        matched = re.findall(pattern_5, remaining)[0]
        block = matched
    elif re.match(pattern_6, remaining): # '22'
        matched = re.findall(pattern_6, remaining)[0]
        block = matched
    elif re.match(pattern_7, remaining): # ''1丁目9番地-12号''
        matched = re.findall(pattern_7, remaining)[0]
        chome, block, building = matched
        block = block + '-' + building
    else:
        pass
    
    return pref, city, town, chome, block
