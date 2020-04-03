from secretsharing import PlaintextToHexSecretSharer
import pyqrcode

def main():
    
    global scale, threshold

    # Select number of shares 
    numofShares = int(input("How many Shares do you want? "))
    # Select revealing threshold
    if numofShares > 2:
        min_threshold = 2
        max_threshold = numofShares
        thresholds = [x for x in range(min_threshold, max_threshold+1)] #shows the choices
        print(["Threshold limit is: ", thresholds])
        threshold = int(input("How many shares should be enough to decrypt? (Most secure is: " + str(max_threshold) + ")\n"))


    # Select type of shares output
    format = input("Select the format of the output images\n-png\n-svg\n-terminal\n")

    # Select size of shares output
    if format != 'terminal':
        scale = input("Size of the output\nS\nM\nL\n")
        if scale == 'S':
            scale = 2
        elif scale == 'M':
            scale = 4
        elif scale == 'L':
            scale = 8

    secret = input('Enter your message: ')

    # Secret-share the message using Shamir's secret sharing scheme.
    shares = PlaintextToHexSecretSharer.split_secret(secret, threshold, numofShares)
    print(shares)

    for share in shares: # Create png for each share
        img = pyqrcode.create(share)
        if format == 'png':
            img.png(share[0]+'.png', scale=scale)
        elif format == 'svg':
            img.svg(share[0]+'.svg', scale=scale)
        elif format == 'terminal':
            print(img.terminal())

if __name__ == '__main__':
    main()
