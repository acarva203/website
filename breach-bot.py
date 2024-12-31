#Breach Bot Starter Code
breachYear = 2014

#Greets user
print("Hello! I'm BreachBot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Yahoo data breach!")



#Introduces breach
print("Would you like to learn about the 2014 Yahoo Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("In 2014, state sponsored hackers likely hired by a foreign government broke into the Yahoo database and acquired the emails, names, phone numbers, dates of birth and passwords of over 500 million accounts; however, the company has admitted to the discovery of the breach in 2016.")
  
  elif topic.lower() == "b":
    print("After the data breach occurred, it took 2 years for Yahoo to discover and admit this to the public and the company simply recommended people who haven’t changed their passwords since 2014 to change them now.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach destroyed the confidentiality of the identities of the 500 million accounts of Yahoo.")
  
  elif topic.lower() == "b":
    print("We disagree with the organization's response because there should have been a greater proactive response from Yahoo, promising to upgrade their security systems and automate some systems that could provide better protection. Also, suggesting to just change your password to fix the breach devalues the potential problems created by the stolen passwords as people usually repeat them across sites.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by suing Yahoo for breach of California law. It is frankly ridiculous that they only admitted to discovering the breach 2 years later and it could have cost victims serious money by then. My advice would be to activate 2 factor authentication and change passwords on all sites.")
    
  elif topic.lower() == "d":
    break
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")