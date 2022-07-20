# https://github.com/Ankit404butfound/PyWhatKit/wiki/Sending-WhatsApp-Messages
import pywhatkit 

numbers = ['+5491158647139', '+5491130738877','+5491158017971','+5491132825317']
msg = 'puto'

for phoneNumber in numbers:
    pywhatkit.sendwhatmsg_instantly(phoneNumber, msg, 5, True, 5)


# pywhatkit.sendwhatmsg('+5491158647139', msg, 5)

# pywhatkit.sendwhatmsg_instantly('+5491158647139', msg, 5)