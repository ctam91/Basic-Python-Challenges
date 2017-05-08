#Function to return initials 
def get_initials(str):
    """Given a person's name, returns the person's initials (uppercase)"""

    i = 0
    initials = str[0]
    while i < len(str)-1:
        if str[i] == " ":
            initials += str[i+1]
        i+=1
    return initials.upper()


#main function to group 'loose'statements
def main():
    """This groups all loose statements"""

    str = input("What is your full name? ")
    print(get_initials(str))

#the main function will not be called when someone imports the code
if __name__ == '__main__':
    main()

