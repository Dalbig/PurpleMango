# -*- coding:utf-8 -*-

import smtplib

def test():
    gmail_user = 'cksgh303@gmail.com'
    gmail_pw = 'Skdlxmskdlxm1@'

    sent_from = gmail_user  
    to = ['test.cksgh303@gmail.com']  
    subject = 'OMG Super Important Message'  
    body = 'Hey, whats up?'

    email_text = """\  From: %s  To: %s  Subject: %s%s""" % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_pw)
    server.sendmail(sent_from, to, email_text)
    server.close()

    # try:  
    #     server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     server.ehlo()
    #     server.login(gmail_user, gmail_pw)
    #     server.sendmail(sent_from, to, email_text)
    #     server.close()

    # except:  
    #     print ('Something went wrong...')

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s' % from_addr
    header += 'To: %s' % ','.join(to_addr_list)
    header += 'Cc: %s' % ','.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

test()
print("sent email!")