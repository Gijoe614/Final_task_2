
class color:
    def __init__(self):
        pass


selection = 0


def returningcust():
    print '\nYou have selected the Returning Customer Option'
    return

def newcust():
    print '\nYou have selected the New Customer Option'
    return

def guestcust():
    print '\nYou have selected the Guest Customer Option\n'
    print 'Welcome to "To Chilis!" where it is our goal to serve you the best food and beverages!'
    return


def wrongnumber():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return

while selection >= 0:
    { '<<=====================================================>>'
                  '<<===                                               ===>>'
                  '\n<<===             1. Returning Customer             ===>>'
                  '\n<<===             2. New Customer                   ===>>'
                  '\n<<===             3. Guest Customer                 ===>>'
                  '<<=====================================================>>'}

    selection = int(raw_input('\n\nPlease make the appropriate customer selection: '))

    try:
        if selection < 1 or selection > 3:
            selection = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

        if selection == 1:
            returningcust()
            selection = - 1

        elif selection == 2:
            newcust()
            selection = - 1

        elif selection == 3:
            guestcust()
            selection = - 1

        else:
            wrongnumber()

    except ValueError:
        print ('Enter 1, 2, or 3!')
