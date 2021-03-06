# Type code for classes here
class ItemToPurchase:
    def __init__(self, item_name="none", item_price = 0, item_quantity = 0,
                 item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))


    def print_item_cost(self):
        self.print_cost = (self.item_quantity * self.item_price)
        print(('{} {} @ ${} = ${}') .format(self.item_name, self.item_quantity, self.item_price, self.print_cost))

class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #def add_item(self, items, quantity):
    def add_item(self, name, price, quantity):
        self.cart_items.append(name, price, quantity)
        #self.cart_items += ItemToPurchase

    def remove_item(self, ItemToRemove):
        ItemToRemove = input('Which item would you like to remove? ')
        if ItemToRemove in self.cart_items:
            self.cart_items -= ItemToRemove
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        ItemToPurchase = input('Which item would you like to modify? ')
        self.ItemToPurchase = ItemToPurchase
        if self.ItemToPurchase in self.cart_items:
            if ItemToPurchase.item_description == 'none':
                ItemToPurchase.item_description = input('Enter a new descriptions: ')
            if ItemToPurchase.item_price == 0:
                ItemToPurchase.item_description = input('Enter a new price: ')
            if ItemToPurchase.quantity == 0 == True:
                ItemToPurchase.quantity = input('Enter new quantitiy: ')
            else:
                print('Item not found in cart. Nothing modified.')

    def get_num_items(self):
        num_cart_items = 0
        for i in self.cart_items:
            num_cart_items = num_cart_items + (self.cart_items * self.quantity)
        print('Number of items:', num_cart_items)

    def cost_of_cart(self):
        cart_cost = (self.quantity * self.item_price)
        print('The current cart cost is:,' ,cart_cost)

    def print_total(self):
        if self.cart_items == []:
            print ('SHOPPING CART IS EMPTY')
            print('%s\'s Shopping Cart - %s' % (self.customer_name, self.current_date))
            print(cart_cost)


    def print_descriptions(self):
        print('%s\'s Shopping Cart - %s\n' % (self.customer_name, self.current_date))
        print('Item Descriptions')
        print(self.item)




def main():
    cust_name = ShoppingCart()
    curr_date = ShoppingCart()
    cust_name.customer_name = input('Enter customer\'s name: ')
    curr_date.current_date = input('Enter today\'s date: ')


    print('Item 1')
    name = input('Enter the item name: ')
    desc = input('Enter a description of the item: ')
    price = int(input('Enter the item price: '))
    quantity = int(input('Enter the item quantity: '))
    item1 = ItemToPurchase(name, price, quantity, desc)

    print('Item 2')
    name = input('Enter the item name: ')
    desc = input('Enter a description of the item: ')
    price = int(input('Enter the item price: '))
    quantity = int(input('Enter the item quantity: '))
    item2 = ItemToPurchase(name, price, quantity, desc)

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print('\nTotal: $%s' % (item1.print_cost + item2.print_cost))

    print('Shopping Cart')
    cart = ShoppingCart()
    name = input('Enter the item name: ')
    price = int(input('Enter the item price: '))
    quantity = int(input('Enter the item quantity: '))
    ShoppingCart.add_item(name, price, quantity)


    #cart = ShoppingCart()
    #print('Cart Items:')
    #cart.add_item(item1)


if __name__ == "__main__":

    main()
