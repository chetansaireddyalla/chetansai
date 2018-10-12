import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("allachetansai143@gmail.com", "chetanreddy")
#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("allachetansai143@gmail.com", "viraaat786@gmail.com", msg)
server.quit()