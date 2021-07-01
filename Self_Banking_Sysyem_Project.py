# ATM Project
import random
ac_no=0
pin=0
name=""
bal=0
mob=0
add=""
aadh=0
acc_det={"acc_no":ac_no,"pin":pin,"name":name,"acc_bal":bal,"mob_no":mob,"address":add,"aadhar":aadh}

def ac_create():
    print("Account Creation From")
    print("---------------------")
    acc_det["name"]=input("Enter Your Name - ")
    acc_det["mob_no"]=int(input("Enter Your 10 digit Mobile Number - "))
    acc_det["aadhar"]=int(input("Enter Your 12 digit Aadhar Card Number - "))
    acc_det["address"]=input("Enter Your Address - ")
    acc_det["acc_bal"]=int(input("Enter the initial deposit amount - "))
    acc_det["acc_no"]=random.randint(1000000000,9999999999)
    print(f'Account Number - {acc_det["acc_no"]}')
    acc_det["pin"]=int(input("Enter Your New Secret Pin - "))
    print("\nCongratulations! Your Account Has Been Created")
    print("\nThank you for banking with us\n")



def deposit():

        print(f'Welcome Mr./Ms.{acc_det["name"]}\n')
        depo_amnt=int(input("Enter The Deposit Amount -  "))
        acc_det["acc_bal"]=acc_det["acc_bal"]+depo_amnt
        print(f'Your Total Account Balance is - {acc_det["acc_bal"]}\n')


def withdraw():

        print(f'Welcome Mr./Ms.{acc_det["name"]}\n')
        withdraw_amnt = int(input("Enter The Withdraw Amount - "))
        if withdraw_amnt>acc_det["acc_bal"]:
            print("Insufficient Balance, Please Enter a Valid Amount")
        else:
            acc_det["acc_bal"] = acc_det["acc_bal"] - withdraw_amnt
            print(f'Your Total Account Balance is - {acc_det["acc_bal"]}\n')



def pin_change():

        print(f'Welcome Mr./Ms.{acc_det["name"]}\n')
        acc_det["pin"] = int(input("Enter Your New Secret Pin - "))
        print("Pin Changed Successfully, Please Remember Your Pin\n")


def bal_check():

        print(f'Welcome Mr./Ms.{acc_det["name"]}')
        print(f'Your Account balance - {acc_det["acc_bal"]}\n')


while True:


    print("------Welcome to Baral Bank------\n")
    print("1- Create Bank Account")
    print("2- Other Transactions\n")
    choice_1=int(input("Enter Your Choice - "))
    if choice_1==1:
        ac_create()
    elif choice_1==2:

        ac_no = int(input("\nEnter Your Account No. - "))
        pin = int(input("Enter Your Pin - "))
        if ac_no == acc_det["acc_no"] and pin == acc_det["pin"]:

            print("1- Cash Deposit")
            print("2- Cash Withdrawal")
            print("3- Balance Check")
            print("4- Pin Change")
            choice_2=int(input("\nEnter Your Choice - "))


            if choice_2==1:
                deposit()
            elif choice_2==2:
                withdraw()
            elif choice_2==3:
                bal_check()
            elif choice_2==4:
                pin_change()
            else:
                print("Enter a Valid Input\n")

        else:
            print("Sorry! You are not a Customer\n")

    else:
        print("Please Enter a Valid Choice\n")
