import numpy as np
#Product prices (in Turkish Lira)
products={"apple":5,"banana":8,"milk":12,"bread":4,"cheese":20}
cart=[]
def add_product(product_name):
    product_name = product_name.strip().lower()
    if product_name in products:
        cart.append((product_name, products[product_name]))
        print(f"{product_name}added to cart.")
    else:
        print(f"{product_name} not found.")
        
print("🛒 Welcome to your shopping cart!")   
print("products: "+" ,".join(products.keys())) 
print(" Type 'q' to quit.\n")

while True:
    selection=input("Add product name to cart")
    if selection.lower()=="q":
        break
    product_names = selection.split(",")
    for name in product_names:
        add_product(name) 
    if cart:
        prices = np.array([price for _, price in cart])
        most_expensive = max(cart, key=lambda x: x[1]) 
        print("\n📊 Cart Summary:")
        print(f"Total number of products: {len(prices)}")
        print(f"Total price: {prices.sum()}TL")
        print(f"Average price:{prices.mean():.2f} TL")
        print(f"The most expensive product: {most_expensive[0]} ({most_expensive[1]} TL)")
    else:
        print("your cart is empty!")
        
      

