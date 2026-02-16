print("""\n\n\t\t\t\t\t\t\t\tWelcome to MOODY MOVIE\n""")
print("="*150)
print()
print("Like so many things,it is not what's outside".center(150))
print()
print("="*150)
print('''
\t\t\t\t\t\tMOODY MOVIE is an online video streaming platform.
\t\t\t\t\tMOODY MOVIE currently offers over 100,000 hours of MOVIE content across 9 languages.
Highly evolved video streaming technology and a high attention to \
quality of experience across devices and platforms\
make MOODY MOVIE the most complete video destination for Over The Top (OTT) video consumers.
     ''')
          
def menu(count):
    print("Press 1. To login as an ADMIN\nPress 2. To login as an User\n")
    c=int(input("Enter your choice:"))
    if c==1:
        passwrd=input("Enter admin password:")
        if passwrd=="myadmin":
            print("Welcome to the Admin window")
            print("\nChoose your operation from the menu given below: ")
            print("\n1.Add new movie details.")
            print("2.Search for a movie.")
            print("3.Delete movie records.")
            print("4.Update the movie records.")
            print("5.View all movie details.")
            print("6.Exit from the Admin window.")
            a=int(input("\nEnter your choice:"))
            if a==1:
                addMovie()
            elif a==2:
                searchMovie()
            elif a==3:
                delMovie()
            elif a==4:
                updateMovie()
            elif a==5:
                viewMovie()
            elif a==6:
                print("Exit from the Admin window")
        else:
            count=count+1
            print(" ERROR: PASSWORD NOT MATCHED. Try again.")
            print("You have entered the password wrong ",count,"time(s)")
            a=input("Do you want to try again or not (y/n) :  ")
        while count<3:
            if a=="Y" or a=='y':
                menu(count)
            else:
                print("BYE")
                return None
        print("ERROR: PASSWORD NOT MATCHED.")
        print("You have entered the password wrong ",count,"time(s)")
        print("NOW YOU CANNOT LOGIN TO ADMIN WINDOW.")
            
    elif c==2:
        userM()

                
def addMovie():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='moviecs')
    cursor = db.cursor()
    while True:
        M_id= input("Enter the movie id: ")
        M_name= input("Enter the name of the movie to be added: ") 
        DOR= input("Enter the date of release of the movie: ")
        Duration= input("Enter the movie duration: ")
        M_country= input("Enter the country in which the movie was released: ")
        Production_company=input("Enter the production company name: ")
        M_language=input("Enter the lanugage of the movie: ")
        Tagline=input("Enter the famous tagline corresponding to the movie: ")
        Lead_actors=input("Enter the names of the lead actors of the movie: ")
        M_genre=input("Enter the type of movie genre: ")
        cursor.execute("insert into Movie values('"+M_id+"','"+M_name+"','"+DOR+"','"+Duration+"',\
'"+M_country+"','"+Production_company+"','"+M_language+"','"+Tagline+"','"+Lead_actors+"','"+M_genre+"')")
        db.commit()
        b=input("\n\nDo you want to enter more movie records (Y/N): ")
        if b == 'Y' or b == 'y':
            addMovie()
        else:
            print("\nMovie Records have been added successfully")
            return None

def searchMovie():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='moviecs')
    cursor = db.cursor()
    s=input("Enter the movie id whose record you want to search:\n")
    cursor.execute("select * from Movie where M_id= '"+s+"';")
    my_records=cursor.fetchall()
    for x in my_records:
        print()
        print("Movie id:",x[0],"\nname of the movie:",x[1],"\ndate of release of the movie:",x[2],\
              "\nmovie duration:",x[3],"\ncountry in which the movie was released:",x[4],\
              "\nproduction company name:",x[5],"\nlanugage of the movie:",x[6],\
              "\nfamous tagline corresponding to the movie:",x[7],\
              "\nnames of the lead actors:",x[8],"\ntype of movie genre:",x[9])
    return None

def delMovie():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='moviecs')
    cursor = db.cursor()
    d=input("Enter the name of the movie whose record you want to delete from the record :\n")
    #preparing sql statements to delete records as per conditions
    #sql= "DELETE FROM Movie WHERE Name = 'nm')"
    try:
        print("DELETE FROM Movie WHERE M_name='"+d+"';")
        cursor.execute("DELETE FROM Movie WHERE M_name='"+d+"';")
        print(cursor.rowcount,"record(s) deleted")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    b=input("\nDo you want to delete more data from movie records (Y/N):\n")
    if b == 'Y' or b == 'y':
        delMovie()
    else:
        print("\nMovie Records have been deleted successfully")
    return None

def updateMovie():
    import mysql.connector
    db = mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='moviecs')
    cursor = db.cursor()
    u=input("Enter the M_id of whose record you want to update: ")
    print("Choose field to be updated")
    print("1.update M_name\n2.update date of release\n3.update movie duration")
    print("4.update country in which the movie was released\n5.update production company name")
    print("6.update movie lanugage\n7.tagline\n8.update lead actors\n")
    ch=int(input("Enter your choice: "))
    if ch==1:
           M_name= input("\nEnter the name of the movie to be updated: ")
           cursor.execute("update Movie set M_name= '"+M_name+"' where M_id= '"+u+"';")
    if ch==2:
           DOR= input("\nEnter the date of release of the movie to be updated: ")
           cursor.execute("update Movie set DOR= '"+DOR+"' where M_id= '"+u+"';")
    if ch==3:
           Duration= input("\nEnter the movie duration to be updated: ")
           cursor.execute("update Movie set Duration= '"+Duration+"' where M_id= '"+u+"';")
    if ch==4:
           M_country= input("\nEnter the updated country in which the movie was released: ")
           cursor.execute("update Movie set M_cpuntry= '"+M_country+"' where M_id= '"+u+"';")
    if ch==5:
           Production_company=input("\nEnter the updated production company name: ")
           cursor.execute("update Movie set Production_company= '"+Production_company+"' where M_id= '"+u+"';")
    if ch==6:
           M_language=input("\nEnter the lanugage of the movie to be updated: ")
           cursor.execute("update Movie set M_language= '"+M_language+"' where M_id= '"+u+"';")
    if ch==7:
           Tagline=input("\nEnter the updated tagline corresponding to the movie: ")
           cursor.execute("update Movie set Tagline= '"+Tagline+"' where M_id= '"+u+"';")
    if ch==8:
           Lead_actors=input("\nEnter the updated names of the lead actors of the movie: ")
           cursor.execute("update Movie set Lead_actors= '"+Lead_actors+"' where M_id= '"+u+"';")
    if ch==9:
           M_genre=input("\nEnter the updated type of movie genre: ")
           cursor.execute("update Movie set M_genre= '"+M_genre+"' where M_id= '"+u+"';")
    print("Movie Records have been updated successfully")
    db.commit()
    b=input("\nDo you want to update more data from movie records (Y/N): ")
    if b == 'Y' or b == 'y':
        updateMovie()
    else:
        print("\nOkay then! Movie Records have been updated successfully.")
    return None

def viewMovie():
    import mysql.connector
    try:
        db = mysql.connector.connect(host='localhost',user='root',password='your_password_here',database='moviecs')
        cursor = db.cursor()
        cursor.execute("Select * from Movie;")
        myrecords = cursor.fetchall()
        for x in myrecords:
            print("Movie id:",x[0],"\nname of the movie:",x[1],\
                  "\ndate of release of the movie:",x[2],"\nmovie duration:",x[3],\
                  "\ncountry in which the movie was released:",x[4],\
                  "\nproduction company name:",x[5],"\nlanugage of the movie:",x[6],\
                  "\nfamous tagline corresponding to the movie:",x[7],\
                  "\nnames of the lead actors:",x[8],"\ntype of movie genre:",x[9])
            print()
    except:
        print("ERROR: unable to display movies")
    return None

def userM():
    # Import webbrowser module in the program
    import webbrowser 
    print("Welcome to MOODY MOVIE".center(150))
    print("="*150)
    print()
    print("Like so many things,it is not what's outside".center(150))
    print()
    print("="*150)
    print("\nYou are currently viewing the user window")
    print("\nYou can watch your favourite movies anytime and anywhere just by a click\n")
    print("Choose your current emotion from the following options: ")
    print("1.SAD")
    print("2.DISGUST")
    print("3.ANGER")
    print("4.ANTICIPATION")
    print("5.FEAR")
    print("6.ENJOYMENT")
    print("7.TRUST")
    print("8.SURPRISE")
    a=input("\nEnter your emotion from the above given choices: ")
    if a=='1':
    # IMDb Url for Drama genre of
    # movie against emotion Sad
        print("\nYOU HAVE CHOOSEN SAD EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='2':
    # IMDb Url for Musical genre of
    # movie against emotion Disgust
        print("\nYOU HAVE CHOOSEN DISGUST EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='3':
    # IMDb Url for Family genre of
    # movie against emotion Anger
        print("\nYOU HAVE CHOOSEN ANGER EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='4':
    # IMDb Url for Thriller genre of
    # movie against emotion Anticipation
        print("\nYOU HAVE CHOOSEN ANTICIPATION EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='5':
    # IMDb Url for Sport genre of
    # movie against emotion Fear
        print("\nYOU HAVE CHOOSEN FEAR EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='6':
    # IMDb Url for Thriller genre of
    # movie against emotion Enjoyment
        print("\nYOU HAVE CHOOSEN ENJOYMENT EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='7':
    # IMDb Url for Western genre of
    # movie against emotion Trust
        print("\nYOU HAVE CHOOSEN TRUST EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    elif a=='8':
        print("\nYOU HAVE CHOOSEN SURPRISE EMOTION\n")
        print("You will be directly redirected to the website where the movies are segregated according to your current emotion.")
        print("ENJOY!")
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
        webbrowser.open_new_tab(url)
    else:
        print("\nPLS ENTER VALID OPTION NO. TO VIEW THE MOVIE. TRY AGAIN .\n\n")
        userM()
    print("\nThank you for visiting MOODY MOVIE. Hope you had a great time watching your desired movie")
    print("Keep visiting!!")
        
if __name__=="__main__":
    count=0
    menu(count)
    
