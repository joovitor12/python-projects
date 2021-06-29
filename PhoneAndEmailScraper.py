#! python3
import pyperclip
import re

# Create a regex obj for phone numbers
phoneRegex = re.compile(r''' 
#1234-5678, 91234-5678, (81) 91234-5678, 81 91234-5678, (81) 1234-5678

(((\d\d) | (\(\d\d\)))?      #area code(optional) // 81 or +55 
(\s)?            #first separator
\d?\d\d\d\d         #first 4 or 5 digits
-?               #dash
\d\d\d\d)         #last 4 digits
''', re.VERBOSE)
# Create a regex for email addresses
emailRegex = re.compile(r'''
                          #
[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+                          
''', re.VERBOSE)
#  Get the text off the clipboard
text = pyperclip.paste()
#  Extract the information from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted information to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
