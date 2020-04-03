from secretsharing import PlaintextToHexSecretSharer

def main():
    
    # Enter shares
    shares = [input('Enter your share: ')]
    while True:
        numofSHares = input("Still have more?\tYes\tNo\n").upper()
        if numofSHares == "Y":
            shares.append(input('Enter your share: '))
        elif numofSHares == "N":
            break
        else:
            print("You haven't answered correctly, try again\n")

    # Recover
    message = PlaintextToHexSecretSharer.recover_secret(shares)
    print('Original message:\n'+message)

if __name__ == '__main__':
    main()
