# -*- coding:utf-8 -*-
from korail2 import *
import sys
import smtplib
from time import sleep

def send(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s \n' % from_addr
    header += 'To: %s \n' % to_addr_list
    header += 'Cc: %s \n' % cc_addr_list
    header += 'Subject: %s \n' % subject
    message = header + '\r\n\r\n' + message

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(login, password)
    server.sendmail(from_addr, to_addr_list, message)
    server.close()

def sendEmail(reservation):
    receiver_email = "cksgh303@gmail.com"  # Enter your address
    sender_email = "test.cksgh303@gmail.com"    #emailId # Enter receiver address
    password = "vdmobile1@"
    message = "\r\n예약번호 : " + reservation.rsv_id + "\r\n"\
        "열차 : " + reservation.dep_name + " - " + reservation.arr_name + "\r\n"\
        "출발시간 : " + reservation.dep_date + " - " + reservation.dep_time + "\r\n"\
        "출발시간 : " + reservation.arr_date + " - " + reservation.arr_time + "\r\n"\

    send(sender_email, receiver_email, "", "코레일예매", message, sender_email, password)
    print("sent email to : " + receiver_email)

def reserveTrain(selectedTrain, pasengers, option):
    print("reserving...")
    while 1:
        sleep(1)

        #search trains
        trains = korail.search_train(dep, arr, date, time, passengers=psgrs, include_no_seats=True)
        temp = list(filter(lambda x: (selectedTrain.train_no == x.train_no) and (selectedTrain.dep_time == x.dep_time) , trains))

        if temp is None:
            return None

        train = temp[0]

        if train.has_seat(): 
            try:
                reservation = korail.reserve(train, pasengers, option)
                if not reservation is None:
                    print("Success to reserve")
                    return reservation
            except SoldOutError: 
                print("[Error] sold out!")


                import smtplib, ssl

# membership number
id = "1571612247"
pw = "skdlxm12"

korail = Korail(id, pw) # with membership number

# params to search trains
dep = '수원'
arr = '동대구'
date = '20190429'
time = '150000'
psgrs = [AdultPassenger(1)]
option = ReserveOption.GENERAL_ONLY

#search trains
trains = korail.search_train(dep, arr, date, time, passengers=psgrs, include_no_seats=True)
count = 1
for train in trains:
    print("[" + str(count) + "]" + str(train))
    count = count + 1

selectedTrainIndex = input('Select train number: ')
#emailId = input('Put your email that you will receive result of reservation: ')

ret = reserveTrain(trains[selectedTrainIndex - 1],psgrs, option)

if not ret is None :
    # send email or send text message on phone
    sendEmail(ret)
    print("Exit")
else :
    print("[error] Couldn't reserve the train !!")




