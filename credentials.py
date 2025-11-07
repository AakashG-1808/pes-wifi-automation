#file for accepting SRN and password
import os
import platform
import stdiomask
platform = platform.system()

class login():
    def accept_name_password(self):
        x=""
        if os.path.exists('credentials.txt'):
            a = open("credentials.txt", "r")

            if a.readlines()!=[]:
                print("Credentials are stored :)")
                x="dont_allow"
            else:
                a = open("credentials.txt", "w")
                srn = input("Enter SRN : ")
                pwd = stdiomask.getpass("Password: ", mask='*')
                a.write(srn + "\n")
                # a.write("\n")
                a.write(pwd + "\n")
        else:
            a = open("credentials.txt", "w")
            srn=input("Enter SRN : ")
            pwd=input("Enter Password : ")
            a.write(srn+"\n")
            #a.write("\n")
            a.write(pwd+"\n")
            x="allow"
        #a.write("\n")
        return x
    def change_password(self):
        file = open("credentials.txt", "r")
        l=file.readlines()
        srn=l[0]
        pwd=l[1]
        #c=l[2]-->driver name
        a=input("Enter Your SRN ")
        print(srn)
        if (a)!=srn:
            print("SRN entered is wrong")
        else:
            b= stdiomask.getpass("Password: ", mask='*')
            if (b)!=pwd:
                print("Password entered is wrong ")
            else:
                srn=input("Enter New SRN : ")
                pwd= stdiomask.getpass("Password: ", mask='*')
                l=[srn,pwd]
        file.close()
        file=open("credentials.txt", "w")
        for j in l:
            file.write(j+"\n")
n=0
while n<3:
    print("Enter the numbers for the following operations")
    print("1=Creating credentials")
    print("2=Change SRN/Password")
    print("3=Exit the menu")
    n=int(input(""))
    if n==1:
        login().accept_name_password()
    elif n==2:
        login().change_password()
    elif n==3:
        break
    else:
        break