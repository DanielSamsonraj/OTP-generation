# sample OTP generation code
import random
import time
def generate_OTP(s):
         temp=""
         for i in range(4):
                temp+=random.choice(s)
         return temp                
s=list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
otp=generate_OTP(s)
print("The OPT for your transaction is ",otp)
flag=True
while flag:
         input_number=input("Enter the 4 digit OTP generated to your mobile : ")
         if(input_number==otp):
                  print("OTP matched, successfull transaction")
                  flag=False
         else:
                  print("The OPT you have entered is wrong please try again after 5 seconds ")
                  time.sleep(5)
