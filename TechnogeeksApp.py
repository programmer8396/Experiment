'''
Inquiry form <name, course, date, isweekday>
  |=> insert
  |=> specific Student details
  |=> Dump all student details

Payment <s_id, course>
  |=> insert
  |=> specific Student details
  |=> Dump all student details


Trainer <name, course, payment, ?>
  |=> insert
  |=> specific Student details
  |=> Dump all student details

  '''


import datetime

class Technogeeks:
  BATCH_DETAILS = {'Python':100,'DS': 200,'Hadoop':300}
  STUDENT_DETAILS = list()
  TRAINER_DETAILS = list()

  def __init__(self,name, course, is_weekday,is_student):
      
      self.name = name
      self.course = course
      self.is_weekday = is_weekday
      self.is_student = is_student

      
  
  def id_gen(self, is_student):

      """
      base on is_student generate id
      ex: stu_geeks<datetimestamp>
      tra_geeks<datetimestamp>
      """
      account_no = datetime.datetime.now()
      if is_student:
        return account_no.strftime("TGS%d%H%M%S")
      else:
        return account_no.strftime("TGT%d%H%M%S")

      
     
  def batch_id_gen(self, course, is_weekday):

    if is_weekday:

      return self.BATCH_DETAILS[self.course] + 1

    else:

      return self.BATCH_DETAILS[self.course] + 2
      
 
  def setdata(self):

    id = self.id_gen(self.is_student)
    batch_id = self.batch_id_gen(self.course, self.is_weekday)

    if self.is_student:
      student  = {'id': id ,'name':self.name,'course':self.course,'is_weekday':self.is_weekday,'is_student':self.is_student,'batch_id':batch_id,'current_status':False}
      Technogeeks.STUDENT_DETAILS.append(student)
      print(Technogeeks.STUDENT_DETAILS)
    else:
      
      trainer = {'id': id ,'name':self.name,'course':self.course,'is_weekday':self.is_weekday,'is_student':self.is_student,'batch_id':batch_id,'current_status':False}
      Technogeeks.TRAINER_DETAILS.append(trainer)
      print(Technogeeks.TRAINER_DETAILS)

    """
      Set current student data
    """            

class Payment(Technogeeks):

  PAYMENTS = []
  TRAINER_SALARY = []

  def __init__(self):
    STUDENT_DETAILS_LIST = Technogeeks.STUDENT_DETAILS
    TRAINER_DETAILS_LIST = Technogeeks.TRAINER_DETAILS

    
  def make_payment(self,id):
    #payment = []
    
    
    for values in Technogeeks.STUDENT_DETAILS:
      if values['id'] == id:
        id = values['id']
        if values['is_student']:
          fee = int(input("Enter the amount to pay \n"))
          if values['is_weekday']:
            if values['course'] == 'Python':
              if values['current_status'] == False:
                paid = 16000
                
                current_payment = [id,(fee),16000,paid - fee]
                Payment.PAYMENTS.append(current_payment)
                print(Payment.PAYMENTS)
                values['current_status'] = True
                print(Technogeeks.STUDENT_DETAILS)
                print("TOTAL FEE:",paid,"\n")
                print("Fee Paid:",fee,"\n")
                print("Remaining Fee:",paid - fee,"\n")

              elif values['current_status'] == True:
                last_payment_list = [i[3] for i in Payment.PAYMENTS if i[0] == id]
                print("Payment",Payment.PAYMENTS)
                print("ID",id)
                print("Last________>>>>>>>>>.",last_payment_list)
                last_payment = last_payment_list[-1]
                if last_payment > 0:
                  current_payment = [id,(fee),16000,last_payment - fee]
                  print("TOTAL FEE:16000\n")
                  print("Fee Paid:",fee,"\n")
                  print("Remaining fee", last_payment - fee,"\n")
                  
                  Payment.PAYMENTS.append(current_payment)
                elif last_payment <= 0:
                    print("Congratulations Your Payment is already Completed")
            elif values['course'] == 'DS':
              if values['current_status'] == False:
                paid = 20000
                current_payment = [id,(fee),20000,paid - fee]
                Payment.PAYMENTS.append(current_payment)
                values['current_status'] = True
                print("TOTAL FEE:",paid)
                print("Fee Paid:",fee)
                print("Remaining Fee:",paid - fee,"\n")
              elif values['current_status'] == True:
                last_payment_list = [i[3] for i in Payment.PAYMENTS if i[0] == id]
                last_payment = last_payment_list[-1]
                if last_payment > 0:
                  current_payment = [id,(fee),20000,last_payment - fee]
                  print("TOTAL FEE:20000")
                  print("Fee Paid:",fee)
                  print("Remaining fee", last_payment - fee,"\n")
                  Payment.PAYMENTS.append(current_payment)
                elif last_payment <= 0:
                    print("Congratulations Your Payment is already Completed")
            elif values['course'] == 'Hadoop':
              if values['current_status'] == False:
                paid = 25000
                current_payment = [id,(fee),25000,paid - fee]
                Payment.PAYMENTS.append(current_payment)
                print("Remaining fee", paid - fee)
                values['current_status'] = True
                print("TOTAL FEE:",paid)
                print("Fee Paid:",fee)
                print("Remaining Fee:",paid - fee,"\n")
              elif values['current_status'] == True:
                last_payment_list = [i[3] for i in Payment.PAYMENTS if i[0] == id]
                last_payment = last_payment_list[-1]
                if last_payment > 0:
                  current_payment = [id,(fee),25000,last_payment - fee]
                  print("TOTAL FEE: 25000")
                  print("Fee Paid:",fee)
                  print("Remaining fee", last_payment - fee,"\n")
                  Payment.PAYMENTS.append(current_payment)
                elif last_payment <= 0:
                    print("Congratulations Your Payment is already Completed")
        else:
          salary  = int(input("Enter Employee Salary "))
          current_salary = id,salary
          Payment.TRAINER_SALARY.append(current_salary)


class Trainers(Technogeeks):
  def __init__(self,name,course,is_weekday,is_student):
    super().__init__(name,course,is_weekday,is_student)
  
  # def make_payment(self,):
  #   return super().make_payment()

  
    

 
class Student(Technogeeks):
  """
  1] call id generator
  2] call make payment
  """
  def __init__(self,name,course,is_weekday,is_student):
    super().__init__(name,course,is_weekday,is_student)


# class <>:
#   """
#   Dump specific student/trainer details
#   Dump all student/trainer details
#   Dump specific batch details based on
#   """

def main():
    #studentdetails = {}
    while True:

      print("1] Inquiry <name> <course> <isweekday>")
      print("2] Make Payment <account_no> <amount>")
      user_input = int(input("Enter your choise\n"))

      if user_input == 1:
        candidate = input("Enter T for Trainer Inquiry and S for Student Inquiry\n")
        name = input("Enter name of the candidate \n")
        checkcourse = input("Enter course wanted to enroll in  P for Python DS for Data Science H for Hadoop? \n")
        isweekday = input("Enter WD for Weekday classes and WE for Weekend classes\n")

        if checkcourse == 'P' or checkcourse == 'p':
          course = "Python"
        elif checkcourse == 'DS' or checkcourse == 'ds':
          course = 'DS'
        elif checkcourse == 'H' or checkcourse == 'h':
          course == 'Hadoop'
        if isweekday == 'WD' or isweekday == 'wd':
          isweekdaybool = True

        elif isweekday == 'WE' or isweekday == 'we':
          isweekdaybool = False

        if candidate == 'T' or candidate == 't':
          t1 = Trainers(name,course, isweekdaybool,False)
          t1.setdata()
        elif candidate == 'S' or candidate == 's':
          s1 = Student(name,course,isweekdaybool,True)
          s1.setdata()
          #s1.student_info()
      elif user_input == 2:
        getid = input("Enter StudentID or TrainerID\n")
        pay = Payment()
        pay.make_payment(getid)
        

      else:
        break
    
 
if __name__ == "__main__":
  main()