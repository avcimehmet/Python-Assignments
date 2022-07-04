# This is my phonebook app with find, add, delete and exit functions

ph_book = {}

def phonebook():
  y = True
  while y == True:
    x = input('Welcome to the phonebook application\
    \n1. Find phone number\
    \n2. Insert a phone number\
    \n3. Delete a person from the phonebook\
    \n4. Terminate \nSelect operation on Phonebook App (1/2/3/4): ')

    def phb_1():
      f = input('Find the phone number of: ')
      if f in ph_book.keys():
        return print(f"Phone number of '{f}' is '{ph_book[f]}'. \n")
      else:
        return print(f"Couldn't find phone number of '{f}'. \n")

    
    def phb_2():
      n = input('Insert name of the person: ')
      p = input('Insert phone number of the person: ')
      if p.isdecimal():
        ph_book[n] = p
        return print(f"Phone number of '{n}' is inserted into the phonebook. \n")
      else:
        return print('Invalid input format, cancelling operation ... \n')

    def phb_3():
      d = input('Whom to delete from phonebook: ')
      if d in ph_book.keys():
        del ph_book[d]
        return print(f"'{d}' is deleted from the phonebook. \n")
      else:
        return print(f"Couldn't find phone number of '{d}'. \n")

    
    if int(x) == 1:
      phb_1()
    
    elif int(x) == 2:
      phb_2()

    elif int(x) == 3:
      phb_3()

    elif int(x) == 4:
      return print('Exiting Phonebook.')
      y = False

phonebook()