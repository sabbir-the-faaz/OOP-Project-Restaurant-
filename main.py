from menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from user import chef, customer,Server, Manager
from order import Order
def main():
  menu = Menu()
  pizza_1=Pizza('Alur pizza',500,'large',['alu','onion'])
  menu.add_menu_item('pizza', pizza_1)
  pizza_2 = Pizza('Beef', 800,'large',['beef','onion','oil'])
  menu.add_menu_item('pizza', pizza_2)
  
  
  #adding burger to the menu
  burger_1 =Burger('Naga Burger', 1000, 'chicken', ['bread','chili'])
  menu.add_menu_item('burger', burger_1)
  burger_2 =Burger('Chili Burger', 1000, 'Beef', ['bread','chili'])
  menu.add_menu_item('burger', burger_2)
  
  #adding drinks
  mojo = Drinks('Mojo',50, True)
  menu.add_menu_item('drinks', mojo)
  coffee = Drinks('Mocha',300, False)
  menu.add_menu_item('drinks', coffee)
  
  
  #show menu
  menu.show_menu()
  
  
  restaurant = Restaurant('Royal Fancy Resturant', 2000, menu)
  
  #add employees
  manager= Manager('Md Akash', 5, 'mdsmanaksh19@gmail.com','dhaka',1000, 'jan 01 2024', 'core')
  restaurant.add_employee('manager', manager)
  
  Chef =chef('Rasha', 6, 'j@gmail.com', 'sdfs', 5000, 'Feb 1,2024','chef','everything')
  restaurant.add_employee('chef',Chef)
  
  
  server =Server('asha', 76, 'fj@gmail.com', 'sdfs', 500, 'Feb 1,2024','chef')
  restaurant.add_employee('server',server)
  
  #show employees
  restaurant.show_employees()
  
  #customer 1 placing an order
  customer_1 = customer('saloo',9393, 'ff@nailm','dhaka', 1999 )
  order_1 = Order(customer_1, [pizza_2, coffee])
  customer_1.pay_for_order(order_1)
  restaurant.add_order(order_1)
  
  #customer 1 paying for order
  restaurant.receive_payment(order_1, 2000, customer_1)
  
  print ('revenue and balance', restaurant.revenue, restaurant.balance)
  

#call the main 
if __name__ == '__main__':
  main()
  
  