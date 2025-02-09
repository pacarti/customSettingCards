import os
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the names from text file and save them into the list:
guestsFile = open('guests.txt')
readGuestsFromFile = guestsFile.readlines()

guests = []

for guest in readGuestsFromFile:
    guestTrimmed = guest.strip('\n')
    guests.append(guestTrimmed)


# Set the fonts:

qtMerryScriptFont = ImageFont.truetype('fonts/QTMerryScript.otf', 16)

nameFont = ImageFont.truetype('fonts/AntykwaTorunska-BoldItalic.otf', 20)

dateFont = ImageFont.truetype('fonts/AntykwaTorunska-Regular.otf', 20)


# Create an invitation for each guest:

for guest in guests:

    # Load the flower background:
    imTemp = Image.open('template.png')
    width, height = imTemp.size

    invitation = ImageDraw.Draw(imTemp)

    invitation.text((91,163), 'It would be a pleasure to have the company of', fill='black', font=qtMerryScriptFont)
    # Improve the centering if the length of the guest name is short:
    if len(guest) < 10:
        invitation.text((148,200), guest, fill='black', font=nameFont)
    else:
        invitation.text((138,200), guest, fill='black', font=nameFont)
    invitation.text((91,230), 'at 11010 Memory Lane on the Evening of', fill='black', font=qtMerryScriptFont)
    invitation.text((158,260), '1st April', fill='black', font=dateFont)
    invitation.text((168,290), 'at 7 o\'clock', fill='black', font=qtMerryScriptFont)

    imTemp.save('invitation for %s.png' % guest)

    imTemp.close()
