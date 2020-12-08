import mysql.connector

# Source: https://mysql.wisborg.dk/2019/03/03/using-sqlalchemy-with-mysql-8/

import mysql.connector
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:' + 'Birdgirl1!' + '@localhost:3306/project',
    echo=True)
cnx = mysql.connector.connect(user='root', password='Birdgirl1!', host='localhost', database = 'project')
cursor = cnx.cursor()

num_buyers = 0
num_carts = 0
num_payments = 0

cursor.execute("DROP TABLE IF EXISTS Payment")
cursor.execute("DROP TABLE IF EXISTS Buyer")
cursor.execute("DROP TABLE IF EXISTS Cart")
cursor.execute("DROP TABLE IF EXISTS Make")
cursor.execute("DROP TABLE IF EXISTS Vehicle_Brand")
cursor.execute("DROP TABLE IF EXISTS Accessories")
cursor.execute("DROP TABLE IF EXISTS Color")
cursor.execute("DROP PROCEDURE IF EXISTS minPriceCars")


# Define and create the table
Base = declarative_base()


class Color(Base):
    __tablename__ = 'Color'

    Color_id = sqlalchemy.Column(sqlalchemy.String(length=50), primary_key=True)
    Color_price = sqlalchemy.Column(sqlalchemy.INTEGER)
    Color = sqlalchemy.Column(sqlalchemy.String(length=10))

    def __repr__(self):
        return "<Color(Color_id='{0}', Color_price='{1}', Color='{2}')>".format(
            self.Color_id, self.Color_price, self.Color)


class Accessories(Base):
    __tablename__ = 'Accessories'

    Accessories_id = sqlalchemy.Column(sqlalchemy.String(length=4), primary_key=True)
    Accessories_price = sqlalchemy.Column(sqlalchemy.INTEGER)
    Accessory = sqlalchemy.Column(sqlalchemy.String(length=10))

    def __repr__(self):
        return "<Accessories(Accessories_id='{0}', Accessories_price='{1}', Accessory='{2}')>".format(
            self.Accessories_id, self.Accessories_price, self.Accessory)


class Vehicle_Brand(Base):
    __tablename__ = 'Vehicle_Brand'

    Brand_id = sqlalchemy.Column(sqlalchemy.String(length=5), primary_key=True)
    Brand_name = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return "<Vehicle_Brand(Brand_id='{0}', Brand_name='{1}')>".format(
            self.Brand_id, self.Brand_name)


class Make(Base):
    __tablename__ = 'Make'

    Make_id = sqlalchemy.Column(sqlalchemy.String(length=6), primary_key=True)
    Model_Shape = sqlalchemy.Column(sqlalchemy.String(length=50))
    Engine_Power = sqlalchemy.Column(sqlalchemy.String(length=50))
    zero_to_sixty_mph = sqlalchemy.Column(sqlalchemy.INTEGER)
    Price = sqlalchemy.Column(sqlalchemy.INTEGER)
    Brand_id = sqlalchemy.Column(sqlalchemy.String(length=5), ForeignKey(Vehicle_Brand.Brand_id))

    def __repr__(self):
        return "<Make(Make_id='{0}', Model_Shape='{1}', Engine_Power='{2}', zero_to_sixty_mph='{3}', Price='{4},', " \
               "Brand_id='{5}')>".format(self.Make_id, self.Model_Shape, self.Engine_Power, self.zero_to_sixty_mph,
                                         self.Price, self.Brand_id)


class Cart(Base):
    __tablename__ = 'Cart'

    Cart_id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    Make_id = sqlalchemy.Column(sqlalchemy.String(length=5), ForeignKey(Make.Make_id))
    Addon_leather = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    Addon_bt = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    Addon_tint = sqlalchemy.Column(sqlalchemy.BOOLEAN)
    car_color = sqlalchemy.Column(sqlalchemy.String(length=50), ForeignKey(Color.Color_id))
    total_price = sqlalchemy.Column(sqlalchemy.INTEGER)

    def __repr__(self):
        return "<Cart(Cart_id='{0}', Make_id='{1}', Addon_leather='{2}', Addon_bt='{3}', " \
               "Addon_tint='{4}', total_price='{5}')>".format(self.Cart_id, self.Make_id,
                                                              self.Addon_leather, self.Addon_bt, self.Addon_tint,
                                                              self.total_price)


# Class Store(name, headquarter, storeType)  <--> Pricelist.stores(name, headquarter, storeType)
class Buyer(Base):
    __tablename__ = 'Buyer'

    Customer_id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    Name = sqlalchemy.Column(sqlalchemy.String(length=50))
    Address = sqlalchemy.Column(sqlalchemy.String(length=50))
    Phone_number = sqlalchemy.Column(sqlalchemy.INTEGER)
    Cart_id = sqlalchemy.Column(sqlalchemy.INTEGER)

    def __repr__(self):
        return "<Buyer(Customer_id='{0}', Name='{1}', Address='{2}', Phone_number='{3}', Cart_id='{4}')>".format(
            self.Customer_id, self.Name, self.Address, self.Phone_number, self.Cart_id)



Base.metadata.create_all(engine)  # creates the stores table

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

newColor = Color(Color_id='BLA', Color_price=0, Color='Black')
session.add(newColor)
newColor = Color(Color_id='WHI', Color_price=0, Color='White')
session.add(newColor)
newColor = Color(Color_id='RED', Color_price=500, Color='Red')
session.add(newColor)
newColor = Color(Color_id='GRE', Color_price=500, Color='Green')
session.add(newColor)

newAcc = Accessories(Accessories_id='LEA', Accessories_price=2000, Accessory='Leather')
session.add(newAcc)
newAcc = Accessories(Accessories_id='BLU', Accessories_price=1000, Accessory='Bluetooth')
session.add(newAcc)
newAcc = Accessories(Accessories_id='TIN', Accessories_price=3000, Accessory='GlassTint')
session.add(newAcc)

new_brand = Vehicle_Brand(Brand_id='BMW', Brand_name='BMW')
session.add(new_brand)
new_brand = Vehicle_Brand(Brand_id='MER', Brand_name='Mercedes')
session.add(new_brand)
new_brand = Vehicle_Brand(Brand_id='AUD', Brand_name='Audi')
session.add(new_brand)

new_make = Make(Make_id='GWAG', Model_Shape='GWagon', Engine_Power='SixCyl', zero_to_sixty_mph=5, Price=80000, Brand_id='MER')
session.add(new_make)
new_make = Make(Make_id='GLK', Model_Shape='GLK-Class', Engine_Power='SixCyl', zero_to_sixty_mph=6, Price=70000, Brand_id='MER')
session.add(new_make)
new_make = Make(Make_id='6SER', Model_Shape='Six Series', Engine_Power='SixCyl', zero_to_sixty_mph=4, Price=85000, Brand_id='BMW')
session.add(new_make)
new_make = Make(Make_id='4SER', Model_Shape='Four Series', Engine_Power='FourCyl', zero_to_sixty_mph=5, Price=55000, Brand_id='BMW')
session.add(new_make)
new_make = Make(Make_id='A4', Model_Shape='A4', Engine_Power='SixCyl', zero_to_sixty_mph=3, Price=40000, Brand_id='AUD')
session.add(new_make)
new_make = Make(Make_id='R8', Model_Shape='R8', Engine_Power='SixCyl', zero_to_sixty_mph=2, Price=100000, Brand_id='AUD')
session.add(new_make)



session.commit()

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

cursor.execute("Create index idx1 on Color (Color_price);")
cursor.execute("Create index idx2 on Make (Price);")

print ("Do you want to buy a car? Please type YES or NO")
answer = input()
if (answer == 'NO'):
        print ("Goodbye")
        quit()
elif (answer == 'YES'):
    print ("Okay. What's your maximum budget?")
    budget = int(input())
    cursor.execute("Select min(Price) from Make")
    min_price = 0
    for Price in cursor:
        min_price = int(Price[0])
    if (min_price > budget):
        print ("sorry, nothing in your price range. goodbye.")
        quit()
    else:
        print ("Great. Do you want to go cheaper or expensive?")
        response = input()
        if (response == 'cheaper'):
            print ("Here are our cheaper options for each brand. Choose one model by typing in the make_id to start your cart.")
            cursor.execute("Select Make_id, Model_Shape, Brand_id, min(Price) from Make Group by Brand_id")
            results = cursor.fetchall()
            for result in results:
                print ("Make_id: " + str(result[0]) + " Model: " + str(result[1]) + " Brand: " + str(result[2]) + " Price: " + str(result[3]))
            choice = input()
            bt = False
            tint = False
            leather = False
            price = 0
            print ("This is the price of Bluetooth. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'BLU'")
            arr = cursor.fetchall()
            print (arr[0][0])
            answer = input()
            if (answer == 'Y'):
                bt = True
                price = price + int(arr[0][0])
            print("This is the price of leather. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'LEA'")
            arr = cursor.fetchall()
            print(arr[0][0])
            answer = input()
            if (answer == 'Y'):
                leather = True
                price = price + int(arr[0][0])
            print("This is the price of window tint. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'TIN'")
            arr = cursor.fetchall()
            print(arr[0][0])
            answer = input()
            if (answer == 'Y'):
                tint = True
                price = price + int(arr[0][0])
            print ("Here are the car colors, along with their prices. Please enter the Color_id to choose your car color.")
            cursor.execute("Select * from Color")
            results = cursor.fetchall()
            for result in results:
                print("Color_id: " + str(result[0]) + " Price: " + str(result[1]) + " Color: " + str(result[2]))
            color_choice = input()
            color_price = 0
            cursor.callproc('color_price', [color_choice])
            for result in cursor.stored_results():
                res = result.fetchall()
                color_price = int(res[0][0])


            price = price + color_price

            car_price = 0
            cursor.callproc('car_choose_price', [choice])
            for result in cursor.stored_results():
                res = result.fetchall()
                car_price = int(res[0][0])

            price = price + car_price
            cartid = 0
            cursor.execute("Select max(Cart_id) from Cart")
            cid = cursor.fetchall()[0][0]
            if (cid == None):
                cartid = 0
            else:
                cartid = int(cid) + 1

            print ("Okay. Here is a summary of your cart. Do you want to purchase? Y/N")
            newCart = Cart(Cart_id=cartid, Make_id=choice, Addon_bt=bt, Addon_leather=leather, Addon_tint=tint, car_color=color_choice, total_price=price)
            session.add(newCart)

            print (repr(newCart))
            session.commit()


            purch = input()
            if (purch == 'N'):
                print ("Okay. Bye.")
                quit()
            if (purch == 'Y'):
                print ("Great. Let's get some information on you so that we can start your purchase. What is your name?")
                name = input()
                print ("What is your address?")
                address = input()
                print ("What is your phone number, without spaces or dashes (e.g. 1234567890)?")
                phone_num = int(input())

                buyerid = 0
                cursor.execute("Select max(Customer_id) from Buyer")
                bid = cursor.fetchall()[0][0]
                if (bid == None):
                    buyerid = 0
                else:
                    buyerid = int(bid) + 1
                newBuyer = Buyer(Customer_id=buyerid, Name=name, Phone_number=phone_num, Address=address, Cart_id=cartid)
                print ("This is the information we have. Is this correct? Y/N")
                print (repr(newBuyer))
                answer = input()
                if (answer == 'N'):
                    print ("Okay. Start over please.")
                    quit()
                if (answer == 'Y'):
                    session.add(newBuyer)
                    session.commit()
                    report = ''
                    print ("Great. Your total is " + str(price) + ".")

                    print ("You'll get a bill in the mail, and after it is paid, you will get a phone call when your car is ready and where to pick it up. Thanks!")


                    cursor.close()
                    cnx.close()

        if (response == 'expensive'):
            print ("Here are our more expensive options for each brand. Choose one model by typing in the make_id to start your cart.")
            cursor.execute("Select Make_id, Model_Shape, Brand_id, max(Price) from Make Where Price > 79000 Group by Brand_id")
            results = cursor.fetchall()
            for result in results:
                print ("Make_id: " + str(result[0]) + " Model: " + str(result[1]) + " Brand: " + str(result[2]) + " Price: " + str(result[3]))
            choice = input()
            bt = False
            tint = False
            leather = False
            price = 0
            print ("This is the price of Bluetooth. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'BLU'")
            arr = cursor.fetchall()
            print (arr[0][0])
            answer = input()
            if (answer == 'Y'):
                bt = True
                price = price + int(arr[0][0])
            print("This is the price of leather. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'LEA'")
            arr = cursor.fetchall()
            print(arr[0][0])
            answer = input()
            if (answer == 'Y'):
                leather = True
                price = price + int(arr[0][0])
            print("This is the price of window tint. Do you want it as an add-on? Y/N")
            cursor.execute("Select Accessories_price From Accessories Where Accessories_id = 'TIN'")
            arr = cursor.fetchall()
            print(arr[0][0])
            answer = input()
            if (answer == 'Y'):
                tint = True
                price = price + int(arr[0][0])
            print ("Here are the car colors, along with their prices. Please enter the Color_id to choose your car color.")
            cursor.execute("Select * from Color")
            results = cursor.fetchall()
            for result in results:
                print("Color_id: " + str(result[0]) + " Price: " + str(result[1]) + " Color: " + str(result[2]))
            color_choice = input()
            color_price = 0
            cursor.callproc('color_price', [color_choice])
            for result in cursor.stored_results():
                res = result.fetchall()
                color_price = int(res[0][0])


            price = price + color_price

            car_price = 0
            cursor.callproc('car_choose_price', [choice])
            for result in cursor.stored_results():
                res = result.fetchall()
                car_price = int(res[0][0])

            price = price + car_price
            cartid = 0
            cursor.execute("Select max(Cart_id) from Cart")
            cid = cursor.fetchall()[0][0]
            if (cid == None):
                cartid = 0
            else:
                cartid = int(cid) + 1

            print ("Okay. Here is a summary of your cart. Do you want to purchase? Y/N")
            newCart = Cart(Cart_id=cartid, Make_id=choice, Addon_bt=bt, Addon_leather=leather, Addon_tint=tint, car_color=color_choice, total_price=price)
            session.add(newCart)

            print (repr(newCart))
            session.commit()


            purch = input()
            if (purch == 'N'):
                print ("Okay. Bye.")
                quit()
            if (purch == 'Y'):
                print ("Great. Let's get some information on you so that we can start your purchase. What is your name?")
                name = input()
                print ("What is your address?")
                address = input()
                print ("What is your phone number, without spaces or dashes (e.g. 1234567890)?")
                phone_num = int(input())

                buyerid = 0
                cursor.execute("Select max(Customer_id) from Buyer")
                bid = cursor.fetchall()[0][0]
                if (bid == None):
                    buyerid = 0
                else:
                    buyerid = int(bid) + 1
                newBuyer = Buyer(Customer_id=buyerid, Name=name, Phone_number=phone_num, Address=address, Cart_id=cartid)
                print ("This is the information we have. Is this correct? Y/N")
                print (repr(newBuyer))
                answer = input()
                if (answer == 'N'):
                    print ("Okay. Start over please.")
                    quit()
                if (answer == 'Y'):
                    session.add(newBuyer)
                    session.commit()
                    report = ''
                    print ("Great. Your total is " + str(price) + ".")

                    print ("You'll get a bill in the mail, and after it is paid, you will get a phone call when your car is ready and where to pick it up. Thanks!")


                    cursor.close()
                    cnx.close()




else:
    print ("Not a valid answer. Goodbye")
    quit()


