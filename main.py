import threading
import time
import sys

# Global Choices
PRICES = {
    "coffee": {"base": 60, "sizes": {"small": 1.0, "medium": 1.2, "large": 1.5}},
    "tea": {"base": 50, "sizes": {"small": 1.0, "medium": 1.2, "large": 1.5}},
    "juice": {"base": 70, "sizes": {"small": 1.0, "medium": 1.2, "large": 1.5}},
}
ADD_ON_COST = 10
VALID_DRINKS = list(PRICES.keys())
VALID_SIZES = list(PRICES['coffee']['sizes'].keys())

# Subprograms & Modularity

def compute_price(drink: str, size: str, add_ons: dict) -> float:
    """Computes the total price of an order."""
    
    # base Price
    base_price = PRICES[drink.lower()]['base']
    
    # size Multiplier
    size_multiplier = PRICES[drink.lower()]['sizes'][size.lower()]
    
    # add on count 
    add_on_count = sum(add_ons.values()) 
    
    # total
    total_price = (base_price * size_multiplier) + (add_on_count * ADD_ON_COST)
    
    return round(total_price, 2)

def prepare_order(order: dict):
    """Simulates order preparation using threading (Concurrency)."""
    
    print(f"Preparing {order['drink']} for {order['customer']}- ˕ •マ")
    time.sleep(2) # Simulate delay
    print(f"{order['drink']} for {order['customer']} is ready!")

def get_validated_input(prompt: str, valid_options: list) -> str:
    """Helper function to simplify input validation loops."""
    while True:
        user_input = input(f"{prompt} ({', '.join(valid_options)}): ").strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input.(•˕ •マ.ᐟ Please choose from: {', '.join(valid_options)}")

def get_order() -> dict | None:
    """Interactively prompts the user for order details (Control Flow)."""
    
    print("\nฅ New Customer Order ฅ")

    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        print("Order cancelled.")
        return None

    #this part helps the input to be simplified
    drink_choice = get_validated_input("Choose drink", VALID_DRINKS)
    size_choice = get_validated_input("Choose size", VALID_SIZES)
    
    #choices for the add ons
    add_sugar = input("Add sugar? (yes/no): ").strip().lower() == 'yes'
    add_milk = input("Add milk? (yes/no): ").strip().lower() == 'yes'
    
    add_ons = {'sugar': add_sugar, 'milk': add_milk}
    
    price = compute_price(drink_choice, size_choice, add_ons)
    
    # this part displays the summary of the add ons
    add_on_str = ", ".join(k for k, v in add_ons.items() if v)
    add_on_display = f"with {add_on_str}" if add_on_str else "no add-ons"

    print(f"Order summary: {drink_choice.capitalize()} ({size_choice.capitalize()}, {add_on_display}) - ₱{price:.2f}")

    return {
        'customer': customer_name,
        'drink': drink_choice.capitalize(),
        'size': size_choice.capitalize(),
        'price': price,
        'add_ons': add_on_display
    }

def process_orders(order_list: list):
    """Runs all preparation tasks concurrently."""
    
    print("\n" + "="*40)
    print(" ฅ Starting Barista Preparation ฅ")
    print("="*40)

    threads = []
    
    #Threading 
    for order in order_list:
        thread = threading.Thread(target=prepare_order, args=(order,))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join() 

    print("="*40)
    print("All orders completed.")
    print("="*40)


# main execution 

def main_cafe_simulation():
    """Main loop for the café simulation."""
    
    print("Welcome to the Nyan Smart Café Simulation!/ᐠ ˵> ⩊ <˵マ")
    orders = []

    # Control Flow & Expressions - Main Customer Loop
    while True:
        order = get_order()

        if order:
            orders.append(order)

        #
        add_another = input("\nAdd another customer? (yes/no): ").strip().lower()
        if add_another == 'no':
            break
            
    if orders:
        process_orders(orders)
    else:
        print("No orders were placed. Simulation ending.")

if __name__ == "__main__":
    try:
        main_cafe_simulation()
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user. Exiting.")
        sys.exit(0)

