import pickle
import os as os

class members:
    def __init__(self, fname, lname, age, address, telNumber ):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
        self.telNumber = telNumber


## Define Vars
path=os.getcwd()+"\\"
membersDB='members.db'
member_addressDB='member_address.db'
member_educ='member_educ.db'

## memory files
memberDict=dict()
memberAddr_Dict=dict()
memberEduc_Dict=dict()

def drawBar(length):
    for i in range(int(length)):
        print ('|',end="")

def clearScreen():
    print ("\n" * 40)

def removeSpaces(urString):
    output=str(urString).strip()
    return output


def duplicate(data):
# Check the data if exist already 
    if data.upper() in memberDict:
        print ('Duplicate Name: ', '      '+'\t',data)
        return True
    else:
        for k in memberDict:
            if data.lower()==memberDict[k].lower():
                print ('Duplicate ID: ', "\t", data)
                return True
    return False

def addMember():
    
    def getKey(keyToTake,case):
        key=removeSpaces(input(str(keyToTake)+' :'))
        
        if len(key)==0 and case==0:
            return ""
        else:
            while len(key)==0 and case==1:
                print ('Blank Entry is now restricted! pls enter a valid ID Number')
                key=getKey(keyToTake,case)
                
            return key.upper()
    
    def getValue(valueToTake):
        value=removeSpaces(input(str(valueToTake)+' :'))
        
        while len(value)==0:
            print ('Invalid Entry, please try again. Try again')
            value=removeSpaces(input(str(valueToTake)+' :'))
        return value.upper()
    
    #=======================================
    clearScreen()
    print ('Add NEW Member')
    print ('Enter Blank @ Member ID to END')
    memDetail=list()
    
    while True:
                    
        nID=getKey('Id Number',0)
        if len(nID)==0:
            break
        
        elif duplicate(nID):
            while duplicate(nID):
                nID=getKey('ID Number',1)
                # Insist valid ID Number
        else:
            pass

        if len(nID)==0:
            #go back to the top
            pass
        else:
            # get Member's Detail
            nName=getValue('Member Name')

            if duplicate(nName) or len(nName)==0:
                while duplicate(nName):
                    nName=getValue('Member Name').strip()
                
            memberDict[nID]=nName
#} end of addMember    

def search2(source, searchBy):
    def printHeader():
        clearScreen()
        print ('Search Result...')
        print ('___________________________________________')
        print ('ID Number        |    Name                 ')
        print ('-------------------------------------------')
        return
    
    found=0
    if searchBy=='ID':
        searchFor=input('Enter ID Number:')
        printHeader()
        
        for key in source:
            if searchFor.lower() in str(key).lower():
                print  ('* '+  str(key).upper()  + '\t'+ str(source[key]).upper())
                found=1
                
    else:
        searchFor=input('Enter Name :')
        printHeader()
        
        for key in source:
            if searchFor.lower() in source[key].lower():
                print ('* '+ str(key).upper() + '\t', str(source[key]).upper())
                found = 1
    if found==0:
        print ('* Search Not found')
        return None
    else:
        return key, source[key]

def editMember(key):
    KEY=str(key).upper()
    if KEY in memberDict:
        # valid key
        print ('Editing details for:',memberDict[key])
        input("press any key...")
        # Then check if key already exist in addresses
        if KEY in  memberAddr_Dict:
            # already exist in Address Dictionary - do edit
            tempAddressDict=dict()
            tempAddressDict[KEY]=memberAddr_Dict[KEY]
            print ('editing: ' )
            input("press any key")
        else:
            # New Addition
            print("Adding New Data to address")
            input('press any key')
    else:
                # invalid key
            print ('invalid ID')
            displayMember(memberDict)
            input()
    return True # edit successful

def displayMember(members):
    ID_fsize = 15
    Name_fsize = 40
    def printHeader():
        print ('_'*70 +'\n')   
        print ('ID Number                Member Name')
        print ('_'*70+ '\n')
    printHeader()
    nLines=40
    pageNo=1
    counter=nLines
    TotalMembers=0
    for k in members:
        tab=ID_fsize-len(k)
        print (k.strip(), ' '*tab ,members[k].strip())
        counter=counter-1
        TotalMembers  +=1
        if counter==0:
            pageNo=pageNo+1
            ans=input("Continue to Page  "+str(pageNo)+" ?(y/n) >>")
            if ans.lower()=='y':
                clearScreen()
                printHeader()
                counter=nLines
                pass
            else:
                break
    if TotalMembers==0:
        print ('No Records to display'+'\n')
    else:
        print ('_'*70+'\n')
        print ('= END OF LIST. ')
        print ('Total of ', TotalMembers, ' Members on Record.')
        print ('='*70)
        
def saveData(toFile,fmDict):
    
            
    Qty_data=len(fmDict)
    
    f=open(toFile,"wb")
    #print f
    for i in fmDict:
        pickle.dump(i,f)
        pickle.dump(fmDict[i],f)
        drawBar(40/Qty_data)
        
    f.close()
    
def readData(frmFile,toDict):
    try:
        
        f=open(frmFile, "rb")
        while True:
            try:
                dataReadKey=pickle.load(f)
                if len(dataReadKey)==0:
                    break
                else:
                    dataReadValue=pickle.load(f)
                #print dataReadKey, '    '+'\t', dataReadValue
                toDict[dataReadKey]=dataReadValue
            except:
                break
        f.close()
    except:
        print ('Welcome to the System. This is the first time you RUN the program.')
        print ('Creating files and databases.....')
        print ('Please wait...')
        
        f=open(frmFile,"w")
        drawBar(40)
        f.close()
        print ('Done.'+'\n')
        input('Press Enter to continue')
        

##=========================================================================
def drawMenu():
    clearScreen()
    print ('                         ______________________________________')
    print ('                         |====================================|')
    print ('                         |                                    |' )  
    print ('                         |             Main Menu              |' )
    print ('                         |                            by:mjbr |')
    print ('                         |------------------------------------|')
    print ('                         |  (1)  Add New Member               |')
    print ('                         |  (2)  Search Database              |')
    print ('                         |  (3)  Display Members              |')
    print ('                         |  (4)  Edit Member' +"'"+'s Record         |')
    print ('                         |  (5)  Program Maintenance          |')
    print ('                         |  (0)  Exit Program                 |')
    print ('                         |  (9)  Open Console                 |')
    print ('                         |                                    |')
    print ('                         |____________________________________|')

    option=input('                          >>')
    return option

def cls():
    clearScreen()
def members():
    displayMember(memberDict)

def lookup():
    print ('lookup by?',)
    x=input('lookup | ')
    if x.lower()=='id':
        search2(memberDict, 'ID')
    elif x.lower()=='name':
        search2(memberDict,'Name')
    else:
        print ("Sorry can't understand.")
        return


def console():
        
    
    command=''
    while len(command)==0:
        command=input('>>')
        if command.lower()=='exit':
            return 'exit'
        elif len(command)!=0:
            return str(command)
        else:
            pass


#===============
# Main Program
#===============

clearScreen()

###################
# Load Datafile
# #################


readData(path+membersDB,memberDict)
readData(path+member_addressDB, memberAddr_Dict)
readData(path+member_educ, memberEduc_Dict)

while True:
    
    option=drawMenu()
     
    if option=='1':
        addMember()
                
    elif option =='2':
        clearScreen()
        print ('Search Members')
        x=''
        while len(x)==0:
            print ('Select Search Option:')
            print ('    (1) Search by ID Number')
            print ('    (2) Search by Name')
            print ('_________________________________')
            x=0
            while x!='1' or x!='2':
                x=input('Enter Searcth Option: ')

                if x=='1':
                    search2(memberDict,'ID')
                    break
                elif x=='2':
                    search2(memberDict,'Name')
                    break
                else:
                    print ('Invalid Option')
                
            input('Enter to Continue')
            clearScreen()
    elif option == '3':
        clearScreen()
        displayMember(memberDict)
        input('Enter to continue')
        clearScreen()
    elif option == '4':
        clearScreen()
        member2edit=input("Enter members' ID:")
        editMember(member2edit)
                
    elif option=='0':
        clearScreen()
      #  print '                     Exiting....','\n',
        print ('Saving Data ....')
        saveData(path+membersDB, memberDict)
        saveData(path+member_addressDB,memberAddr_Dict)
        saveData(path+member_educ, memberEduc_Dict)
        
        print ('Done')
        break
    elif option =='9':

        clearScreen()
        print ('Console mode. Enter your command')
        print ('Type "exit" or "Exit" to end.')
            
        result = True
        while True:
            result=console()
            if result=='exit':
                break
            else:
                print ('<<|>>' + 'executing ' + str(result) + '*')
                try:
                    eval(result)
                except:
                    print ('Command not found')
                    pass       
        
    else:
        print ('Invalid Input')
        clearScreen()
