def main():
    #get the data
    dateStr = input('Enter a date (mm/dd/yyyy): ')

    #split date into comppnents
    monthstr, daystr, yearstr = dateStr.split('/')

    #convert monthstr into month name
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
    
    monthstr = months[int(monthstr)-1]

    #ouput results
    print('The converted date is: ', monthstr, daystr+',',yearstr)

main()
