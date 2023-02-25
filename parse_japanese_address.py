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
    elif re.match(pattern_7, remaining): # '1丁目9番地12号'
        matched = re.findall(pattern_7, remaining)[0]
        chome, block, building = matched
        block = block + '-' + building
    elif re.match(pattern_2, remaining): # '23丁目4'
        matched = re.findall(pattern_2, remaining)[0]
        chome, block = matched
    elif re.match(pattern_3, remaining): # '2丁目'
        matched = re.findall(pattern_3, remaining)[0]
        chome = matched
    elif re.match(pattern_4, remaining): # '22-2-2'
        matched = re.findall(pattern_4, remaining)[0]
        chome, block = matched
        chome = chome + '丁目'
    elif re.match(pattern_5, remaining): # '7643-12'
        matched = re.findall(pattern_5, remaining)[0]
        block = matched
    elif re.match(pattern_6, remaining): # '22'
        matched = re.findall(pattern_6, remaining)[0]
        block = matched
    else:
        pass
    
    return pref, city, town, chome, block

if __name__ == "__main__":
    
    address_test_list = [
        '群馬県高崎市倉渕町川浦3900-156',
        '群馬県高崎市倉渕町岩氷19-1',
        '兵庫県神戸市東灘区住吉本町１丁目２番９',
        '兵庫県神戸市東灘区岡本５丁目１',
        '兵庫県神戸市灘区摩耶山町2-2',
        '東京都港区麻布台1丁目9番地12号',
        '東京都港区麻布台1-9-12',
        '大阪府大阪市港区築港３丁目５-9',
        '群馬県伊勢崎市連取町2335-1'
    ]
    
    for address in address_test_list:
        print(parse_japanese_address(address))
