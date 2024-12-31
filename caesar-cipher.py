
# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""

# Introduction
print(
  "Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: "
  + possibleCharacters + "\n\nLet's get started!\n")

# prompts user input for message, key, and mode
initialMessage = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 25. "))
mode = input("Do you want to encrypt or decrypt? ")

# loop that goes through each letter to encrypt/decrypt the message

for a in initialMessage:
  #encrypt/decrypt message if all are capital letters
  if possibleCharacters.find(a) != -1:
    initialPosition = possibleCharacters.find(a)
    if (mode.lower() == "encrypt"):
      shiftedPosition = initialPosition + key
    elif (mode.lower() == "decrypt"):
      shiftedPosition = initialPosition - key
    if shiftedPosition >= len(possibleCharacters):
      shiftedPosition = shiftedPosition - len(possibleCharacters)
    elif shiftedPosition < 0:
      shiftedPosition = shiftedPosition + len(possibleCharacters)
    shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
  #if any are lowercase, make them uppercase, then encrypt/decrypt message
  elif possibleCharacters.find(a.upper()) != 1:
    initialPosition = possibleCharacters.find(a.upper())
    if (mode.lower() == "encrypt"):
      shiftedPosition = initialPosition + key
    elif (mode.lower() == "decrypt"):
      shiftedPosition = initialPosition - key
    if shiftedPosition >= len(possibleCharacters):
      shiftedPosition = shiftedPosition - len(possibleCharacters)
    elif shiftedPosition < 0:
      shiftedPosition = shiftedPosition + len(possibleCharacters)
    shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
  else:
    shiftedMessage = shiftedMessage + a

# Print the shifted message
print("Your " + mode.lower() + "ed message is: " + shiftedMessage)
