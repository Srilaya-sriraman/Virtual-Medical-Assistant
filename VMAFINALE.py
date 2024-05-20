print('*VIRTUAL MEDICAL ASSISTANT WELCOMES YOU*')


import mysql.connector as mysql
mycon=mysql.connect(host="localhost",user="root",passwd="Elakiya@1011",database="VMA")
cursor=mycon.cursor()
import datetime


#login function for doctor

def logind():
    
    email_no1=input("ENTER YOUR EMAIL ID (or) MOBILE NUMBER:")
    password1=input("ENTER YOUR PASSWORD:")
    cursor.execute("SELECT*FROM DOCTOR_PROFILE")
    list1=[]
    x=cursor.fetchall()
    
    for row in x:
        list1.append(row)
        
    for a in range (len(list1)):
        if list1[a][1]==email_no1 and list1[a][3]==password1:
            print()
            print("WELCOME HOME")
            print()
            homepage_doctor()
            break
        elif list1[a][2]==email_no1 and list1[a][3]==password1:
            print()
            print("WELCOME HOME")
            print()
            homepage_doctor()
            break
    else:
        logind()
        

#login function for patient

def loginp():

    email_no2=input("ENTER YOUR EMAIL ID (or) MOBILE NUMBER:")
    password2=input("ENTER YOUR PASSWORD:")
    cursor.execute("SELECT*FROM PATIENT_PROFILE")
    list2=[]
    y=cursor.fetchall()
    global accno
    for row in y:
        list2.append(row)
    for a in range (len(list2)):
        if list2[a][4]==email_no2 and list2[a][15]==password2:
            print()
            print("WELCOME HOME")
            print()
            accno=list1[a][0]
            homepage_patient()
            break
        elif list2[a][3]==email_no2 and list2[a][15]==password2:
            print()
            print("WELCOME HOME")
            print()
            accno=list1[a][0]
            homepage_patient()
            break
    else:
        loginp()

        
#signup function for doctors

def doctor():
    
    email1=input("ENTER YOUR EMAIL ID:")
    no1=input("ENTER YOUR MOBILE NUMBER:")
    pass_word1=input("CREATE A STRONG PASSWORD OF 8-DIGITS:")
    recheck_password1=input("RE-ENTER PASSWORD:")
    if pass_word1==recheck_password1:
        print("YOUR PROFILE HAS BEEN CREATED")
        print()
        name1=input("ENTER YOUR NAME:")
        DOB11=input("ENTER YOUR DATE OF BIRTH (in DD/MM/YYYY):")
        DOB1=datetime.datetime.strptime(DOB11,"%d/%m/%Y").date()
        medno=input("ENTER YOUR MEDICAL LICENSE NUMBER:")
        field=input("ENTER THE FIELD YOUR SPECIALISE IN:")
        qualification=input("ENTER YOUR MEDICAL QUALIFICATION:")
        experience=input("ENTER YOUR EXPERIENCE(in yrs):")

        print()
        
        cursor.execute("SELECT*FROM DOCTOR_PROFILE")
        list3=[]
        z=cursor.fetchall()
        for row in z:
            list3.append(row)
            
        def acc_doc():
            import random
            global accs
            accs = random.randint(11111111,99999999)
            
            for a in range(len(list3)):
                if list3[a][0]==accs:
                    acc_doc()
                else:
                    break
    else:
        print("PASSWORD DOES NOT MATCH. PLEASE TRY AGAIN")
        print()
        doctor()

    acc_doc()
    sql1='''INSERT INTO DOCTOR_PROFILE (ACCOUNT_NO, EMAIL_ADDRESS, CONTACT_NO, PASSWORD,
    DOCTOR_NAME, DOB, LICENSE_NUMBER, FIELD, QUALIFICATION, EXPERIENCE)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val1=(accs,email1,no1,pass_word1,name1,DOB1,medno,field,qualification,experience)
    cursor.execute(sql1,val1)
    mycon.commit()
    
    print()
    print('YOUR DATA HAS BEEN ADDED TO OUR DATABASE!')
    print('YOUR ACCOUNT NUMBER IS:',accs)
    print('WELCOME HOME')
    print()
    homepage_doctor()


#signup function for patients

def patient():
    
    email2=input("ENTER YOUR EMAIL ID:")
    no2=int(input("ENTER YOUR CONTACT NUMBER:"))
    pass_word2=input("CREATE A STRONG PASSWORD OF 8-DIGITS:")
    recheck_password2 =input("RE-ENTER PASSWORD:")
    if pass_word2==recheck_password2:
        print("YOUR PROFILE HAS BEEN CREATED")
        print()
        name2=input("ENTER YOUR NAME:")
        address=input("ENTER YOUR ADDRESS:")
        DOB12=input("ENTER YOUR DATE OF BIRTH(in DD/MM/YYYY):")
        DOB2=datetime.datetime.strptime(DOB12,"%d/%m/%Y").date()
        age=int(input("ENTER YOUR AGE:"))
        gender=input("ENTER YOUR GENDER:")
        height=int(input("ENTER YOUR HEIGHT (in cm):"))
        weight=int(input("ENTER YOUR WEIGHT (in kg):"))
        bg=input("ENTER YOUR BLOOD GROUP:")
        occupation=input("ENTER YOUR OCCUPATION:")
        diagnosis=input("Your previous diagnosis (if none enter null):")
        treatment=input("Method of treatment (if none enter null):")
        allergies=input("Any allergies (if none enter null):")

        print()
        
        cursor.execute("SELECT*FROM PATIENT_PROFILE")
        list4=[]
        x=cursor.fetchall()
        for row in x:
            list4.append(row)
            
        def accp():
            import random
            global accl
            accl= random.randint(11111111,99999999)
            for a in range(len(list4)):
                if list4[a][0]==accl:
                    accp()
                else:
                    break
                    
    else:
        print('PASSWORD DOES NOT MATCH. PLEASE TRY AGAIN')
        patient()

    accp()
    sql2='''INSERT INTO PATIENT_PROFILE(ACCOUNT_NO,PATIENT_NAME,ADDRESS,CONTACT_NUMBER,EMAIL_ADDRESS,DATE_OF_BIRTH,AGE,
    GENDER,WEIGHT,HEIGHT,BLOOD_GROUP,OCCUPATION,DIAGNOSIS,TREATMENT,ALLERGIES,password)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    val2=(accl,name2,address,no2,email2,DOB2,age,gender,weight,height,bg,occupation,diagnosis,treatment,allergies,pass_word2)
    cursor.execute(sql2,val2)
    mycon.commit()
    
    global accno
    accno=accl
    
    print()
    print('YOUR DATA HAS BEEN ADDED TO OUR DATABASE!')
    print('YOUR ACCOUNT NUMBER IS:',accno)
    print('WELCOME HOME')
    print()
    homepage_patient()


# Main Function

# Ask if the login is for a doctor or a patient and if they want to login or Signup.
# They choose a number, provide login or signup details

def signorlog():
    print("1.LOGIN AS DOCTOR \n2.LOGIN AS PATIENT \n3.SIGNUP")
    opt=input("Select an option:")
    print()
    if opt=="1":
        logind()
    elif opt=="2":
        loginp()
    elif opt=="3":
        print("1.SIGNUP AS PATIENT \n2.SIGNUP AS DOCTOR \n3.LOGIN")
        opt2=input("Select an option:")
        print()
        if opt2=="1":
            patient()
        elif opt2=="2":
            doctor()
        elif opt2=="3":
            signorlog()
        else:
            print("Please enter a valid option:")
            print()
            signorlog()
    else:
        print("Please enter a valid option:")
        print()
        signorlog()

#Record Manager

#Patient's Side Program

def view_patients():
    from tabulate import tabulate
    sql_access_query = 'SELECT FROM RECORD_MANAGER_2022 WHERE acc_no=%s ORDER BY Date'
    cursor.execute(sql_access_query, accno)
    x=cursor.fetchall()
    if x==[]:
        print('NO RECORDS AVAILABLE AS OF NOW')
    else:
        print('DISPLAYING THE MEDICAL RECORDS')
        print(tabulate(x, headers=["ACCOUNT NO.","DATE","CENTRE","AGE","HEIGHT","WEIGHT","BP","TEMPERATURE","BLOOD TEST","DIAGNOSIS","TREATMENT","SCAN","X-RAY"]))
        print()
    #Entire Patient's Table is Printed
    #Sorted by Date

#Doctor's Side Program

def doctors():

    choice=input('DO YOU WANT TO VIEW OR EDIT A PATIENT\'S RECORD? ENTER VIEW/ADD:')
    num=input('ENTER PATIENT\'S ACCOUNT NUMBER:')
    print()

    if choice=='VIEW':

        from tabulate import tabulate
        sql_daccess_query = 'SELECT FROM RECORD_MANAGER_2022 WHERE accno=%s ORDER BY Date'
        cursor.execute(sql_daccess_query, num)
        xd=cursor.fetchall()
        if xd==[]:
            print("NO RECORDS AVAILABLE AS OF NOW")
        else:
            print('DISPLAYING THE MEDICAL RECORDS')
            print(tabulate(xd, headers=["ACCOUNT NO.","DATE","CENTRE","AGE","HEIGHT","WEIGHT","BP","TEMPERATURE","BLOOD TEST","DIAGNOSIS","TREATMENT","SCAN","X-RAY"]))
            print()
            
    elif choice=='ADD':
       
        print('TAKING INPUT DATA')
        print('TO ADD A NEW RECORD OF CHECKUP INFO IN THE PATIENT\'S TABLE')
   
        Date=input('ENTER DATE OF CHECKUP (DD/MM/YYYY):')
        Centre=input('ENTER NAME OF THE CHECKUP CENTRE:')
        Age=int(input('ENTER PATIENT\'S AGE:'))
        Height=int(input('ENTER THE PATIENT\'S HEIGHT (in cms):'))
        Weight=int(input('ENTER THE PATIENT\'S WEIGHT (in Kgs):'))
        BP=input('ENTER BP LEVEL:')
        Temperature=float(input('ENTER BODY TEMPERATURE (in Fahrenheit):'))
        Blood_Test=input('ENTER BLOOD TEST REPORT:')
        Diagnosis=input('ENTER THE PROBLEM FACED BY THE PATIENT:')
        Treatment=input('ENTER THE TREATMENT SUGGESTED:')
        Scan=input('ENTER SCAN REPORT:')
        XRay=input('ENTER X-RAY REPORT:')

        print()
   
        sql3='''INSERT INTO RECORD_MANAGER_2022 (acc_no, Date, Centre, Age, Height, Weight, BP, Temperature, Blood_Test, Diagnosis, Treatment, Scan, XRay)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        val3=(num,Date,Centre,Age,Height,Weight,BP,Temperature,Blood_Test,Diagnosis,Treatment,Scan,XRay)
        cursor.execute(sql3,val3)
        mycon.commit()

        print('RECORD ADDED')
        print()
        
#Medical Prescription

def prescription_doctor():
    
    acc=int(input("ENTER PATIENT'S ACCOUNT NUMBER:"))
    print()
    cursor.execute("SELECT*FROM PATIENT_PROFILE")
    t=cursor.fetchall()
    list3=[]
    for row in t:
        list3.append(row)
    for a in range(len(list3)):
        if list3[a][0]==acc:
            print("WELCOME TO MEDICINE PRESCRIPTION PAGE")
            print()
            name=list3[a][1]
            email=list3[a][4]
            print("ENTER THE DETAILS")
            print()
            d=input('ENTER THE DATE OF PRESCRIPTION (DD/MM/YYYY):')
            dt=datetime.datetime.strptime(d,"%d/%m/%Y").date()
            pb=input('ENTER THE MEDICAL ISSUE FACED BY THE PATIENT:')
            mn=input("ENTER THE MEDICINE NAME:")
            sth=input("ENTER THE STRENGTH OF THE MEDICINE:")
            dose=input("ENTER THE DOSE TO BE TAKEN:")
            st_on=input("ENTER THE STARTING DATE (DD/MM/YYYY):")
            ston=datetime.datetime.strptime(st_on,"%d/%m/%Y").date()
            dr=input("ENTER THE DURATION OF THE MEDICINAL COURSE:")

            print()

            break

    else:
        print('ENTERED ACCOUNT NUMBER DOES NOT MATCH WITH EXISTING RECORDS')
        print('PLEASE TRY AGAIN')
        print()
        prescription_doctor()

    sql4='''INSERT INTO PRESCRIPTIONS (ACC_NO,NAME,DATE_OF_PRESCRIPTION,MEDICAL_ISSUE,MEDICINE,STRENGTH,DOSE,START_ON,DURATION)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    val4=(acc,name,dt,pb,mn,sth,dose,ston,dr)
    cursor.execute(sql4,val4)
    mycon.commit()

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    m1,m2,m3,m4,m5,m6,m7,m8=name,d,pb,mn,sth,dose,st_on,dr
    mail ="""Hello {0}, This is a prescription from your doctor through the VMA Application
    Prescription Details
    Date of Prescription: {1}
    Medical Issue: {2}
    Medicine Name: {3}
    Strength: {4}
    Dose: {5}
    Start On: {6}
    Duration: {7}

    Do Follow the Medicinal Routine, and Keep in Touch:)"""
    mail_content=mail.format(m1,m2,m3,m4,m5,m6,m7,m8)
#The email addresses and password
    sender_address = 'assistantvirtualmedical@gmail.com'
    sender_pass = 'vma#1011'
    receiver_address = email
#Set up MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Medical Reminder from Doctor\'s prescription' 
#The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
#login with mail_id and password
    session.starttls() 
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('~PRESCRIPTION REPORT SENT SUCCESSFULLY~')
    print()

def prescription_patient():

    from tabulate import tabulate
    sql5='SELECT * FROM PRESCRIPTIONS WHERE ACC_NO=%s'
    cursor.execute(sql5,accno)
    pp=cursor.fetchall
    print('DISPLAYING PREVIOUS DOCTOR PRESCRIPTIONS')
    print(tabulate(pp, headers=["ACCOUNT NO","NAME","PRESCRIPTION DATE","ISSUE","MEDICINE","STRENGTH","DOSE","START ON","DURATION"]))
    print()
    


#Homepage

#Patients Home page
    
def homepage_patient():
    print("VMA FEATURES")
    print("1.RECORD MANAGER")
    print("2.MEDICAL PRESCRIPTION REPORT ")
    response=int(input("SELECT AN OPTION:"))
    print()
    
    if response==1:
        print('WELCOME TO RECORD MANAGER')
        print('CHECK YOUR MEDICAL RECORDS HERE')
        view_patients()
        print()
        
        print('BACK TO HOMEPAGE')
        print()
        homepage_patient()
        
    elif response==2:
        print('WELCOME TO MEDICAL PRESCRIPTION REPORT')
        prescription_patient()
        print()
        
        print('BACK TO HOMEPAGE')
        print()
        homepage_patient()
        
    else:
        print("CHOOSE A VALID OPTION NUMBER")
        homepage_patient()
        
#Doctors Home page
        
def homepage_doctor():
    print("VMA FEATURES")
    print("1.RECORD MANAGER")
    print("2.MEDICAL PRESCRIPTION REPORT ")
    response=int(input("SELECT AN OPTION:"))
    print()
    
    if response==1:
        print('WELCOME TO RECORD MANAGER')
        print('PATIENTS\' MEDICAL RECORDS')
        doctors()
        print()

        print('BACK TO HOMEPAGE')
        print()
        homepage_doctor()
        
    elif response==2:
        print('WELCOME TO MEDICAL PRESCRIPTION REPORT')
        prescription_doctor()
        print()

        print('BACK TO HOMEPAGE')
        print()
        homepage_doctor()
        
    else:
        print("CHOOSE A VALID OPTION NUMBER")
        homepage_doctor()

#_MAIN_

signorlog()
