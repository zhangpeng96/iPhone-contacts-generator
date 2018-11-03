import json, time, csv, pprint

def parseContactLine(fieldName, value):
    switcher = {
        "ORG": "ORG:" + value + ";",
        "ORG2": value + "\n",
        "TITLE": "TITLE:" + value + "\n",
        "FN": "FN:" + value + "\n",
        "N": "N:" + value + ";",
        "N2": value + ";;;\n",
        "TWORK": "TEL;TYPE=WORK;TYPE=VOICE:" + value + "\n",
        "TWORK2": "TEL;TYPE=WORK;TYPE=VOICE:" + value + "\n",
        "THOME": "TEL;TYPE=HOME;TYPE=pref;TYPE=VOICE:" + value + "\n",
        "TEL": "item1.TEL:" + value + "\nitem1.X-ABLABEL:集团号\n",
        "TEL2": "item2.TEL:" + value + "\nitem2.X-ABLABEL:内线固话\n",
        "IMPP": "IMPP;X-SERVICE-TYPE=即时通;TYPE=HOME;TYPE=pref:x-apple:" + value + "\n",
        "IMPP2": "IMPP;X-SERVICE-TYPE=微信;TYPE=HOME;TYPE=WeChat:" + value + "\n"
    }
    return switcher.get(fieldName, "")

string = ''
string_head = "BEGIN:VCARD\n\
VERSION:3.0\n"
string_tail = "PRODID:-//Apple Inc.//iCloud Web Address Book 1820B23//EN\n\
REV:2018-11-01T08:00:00Z\n\
END:VCARD\n"

with open('csv-test.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for line in data:
        vcard = ''
        vcard = vcard + string_head
        for key in line:
            # print(parseContactLine(key, line.get(key)))
            vcard = vcard + parseContactLine(key, line.get(key))
        vcard = vcard + string_tail
        # 
        string = string + vcard + '\n'

print(string)

with open('f.vcf', 'w', newline='\n') as f:
    f.write(string)
    f.close()

    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        # print(','.join(line))

        # output.append(line)
    # print(data.fieldnames)
    # print(type(spamreader))
    # for row in spamreader:
        # print(', '.join(row))
        # print(row)