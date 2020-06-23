from ProgramFiles import University
while(True):
    action=int(input("Press\n1.Add Record\n2.Search Record\n3.Exit\nAction:"))
    if action==1:
        University.addRecord()
    if action==2:
        University.checkRecord()
    if action==3:
        University.exit()
        break