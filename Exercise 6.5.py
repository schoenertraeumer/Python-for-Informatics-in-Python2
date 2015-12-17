import string

str = 'X-DSPAM-Confidence: 0.8475'

pos = str.find(":")
number = str[pos+1:]
float(number)
print number
