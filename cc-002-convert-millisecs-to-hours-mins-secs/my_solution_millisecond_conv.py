def millisecond_conv():
    x = True
    while x :
      decimal_num = (input('###  This program converts milliseconds into hours, minutes, and seconds ### \
  \n(To exit the program, please type "exit") \
  \nPlease enter the milliseconds (should be greater than zero) : '))
      conv_list = {3600000: ' hour(s), ', 60000: ' minute(s), ', 1000: ' second(s).'} 
      output = ''
      try:
        if str(decimal_num).lower() == 'exit':
          return ('Exiting the program... Good Bye!')
          x = False
        elif int(decimal_num) < 1000:
          if int(decimal_num) > 0:
            return (f'Just {decimal_num}' + ' millisecond(s).')
        for i in conv_list.keys():
            if (int(decimal_num) // i) > 0:
              output +=  str(int(decimal_num) // i) + conv_list[i]
              decimal_num = int(decimal_num) % i
        return output
        continue
      except (ValueError, KeyError):
            print('Not Valid Input !!!')

print(millisecond_conv())

