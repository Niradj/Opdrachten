stemmen = int(input('Hoe oud ben je?'))
paspoort = str(input('Heb je een Nederlands paspoort?'))
if stemmen >= 18 and paspoort == 'ja':
    print('Je mag stemmen')
else:
    print('Je mag niet stemmen')