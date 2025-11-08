# Nyan Smart Café Simulation 🐱

This is a simple, multi-threaded Python script that simulates the ordering and preparation process at a bustling cat café.

It allows a user to input multiple customer orders one by one. After all orders are taken, it simulates the "barista" preparation process by handling all orders concurrently using Python's `threading` module.

---

## ✨ Features

* **Interactive Order Taking:** Prompts for customer name, drink (coffee, tea, juice), size (small, medium, large), and add-ons (sugar, milk).
* **Dynamic Price Calculation:** Computes the final price based on the base drink cost, a size multiplier, and a fixed cost for each add-on.
* **Input Validation:** A reusable helper function ensures that users select only valid drinks and sizes.
* **Concurrent Order Preparation:** Uses `threading` to simulate multiple orders (e.g., one for Alice, one for Bob) being prepared at the same time, rather than one after the other.
* **Clean Order Summary:** Displays a clear summary and total price for each order before processing.

---

## 🚀 How to Run

This script runs on Python 3 and uses only standard libraries (`threading`, `time`, `sys`).

1.  Save the code as a Python file (`cafe.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script:

    ```bash
    python cafe.py
    ```

---

## 🧠 Key Concepts Demonstrated


This script serves as a practical example of several key programming concepts:

Modularity: The code is broken down into small, single-responsibility functions (compute_price, get_order, prepare_order).

Concurrency: The threading module (prepare_order and process_orders) is used to run multiple tasks simultaneously, simulating a real-world scenario where multiple orders are prepared at once.

Control Flow: The program uses while loops for the main application logic (main_cafe_simulation) and for input validation (get_validated_input).

Data Structures: It uses dictionaries (PRICES) for structured data lookup and lists (orders, threads) to manage collections of items.

---
## Reflection 🐾

1. How did you implement concurrency in your code?
Using Python's built-in threading module to run tasks at the same time.
I loop through the list of all customer orders. (process_orders )
Then for I create a new thread and assign it the prepare_order function as its job. and to pass theespecific order's details.
for thread.start() on each thread. this show them all, letting them run concurrently. This is why you see all the "Preparing..." messages print at once, followed by the time.sleep. and for this last use thread.join() in the final loop. This tells the main program to "wait here until all the threads you just started have finished their work." Once they are all done, the script moves on and prints "All orders completed."

2. What challenges did you encounter while modularizing your program?
My main challenge was that my validation code was not flexible.
I tried to add new sizes just for coffee (like 'venti'), while keeping 'small, medium, large' for tea and juuice so it broke the program.
When the user tried to order a 'small' tea, the code would fail. It was checking the word 'small' against the coffee size list ('venti') and didn't find it.
The problem was that I had one single list of VALID_SIZES that was hard-coded to only use the coffee sizes. My "reusable" validation function was stuck using that one list for all drinks, which wasn't very modular at all.
 
3. If you could enhance your simulation, what new feature would you add?
Honestly, I don't know but maybe I wish it will not take orders from every name and process everything in one go. So I hope Ic could come up with it takes order and then process it and it will loop back to start by taking another order from different name.


---
## 💻 Example Usage

Here is what a typical session looks like in the terminal:

```text
Welcome to the Nyan Smart Café Simulation!/ᐠ ˵> ⩊ <˵マ

ฅ New Customer Order ฅ
Enter customer name: Mickz
Choose drink (coffee, tea, juice): coffee
Choose size (small, medium, large): large
Add sugar? (yes/no): yes
Add milk? (yes/no): no
Order summary: Coffee (Large, with sugar) - ₱100.00

Add another customer? (yes/no): yes

ฅ New Customer Order ฅ
Enter customer name: Armored Titan
Choose drink (coffee, tea, juice): tea
Choose size (small, medium, large): small
Add sugar? (yes/no): no
Add milk? (yes/no): yes
Order summary: Tea (Small, with milk) - ₱60.00

Add another customer? (yes/no): no

========================================
 ฅ Starting Barista Preparation ฅ
========================================
Preparing Coffee for Mickz- ˕ •マ
Preparing Tea for Armored Titan- ˕ •マ
Coffee for Mickz is ready!
Tea for Armored Titan is ready!
========================================
All orders completed. ദ്ദി/ᐠ - ⩊ -マ.ᐟ
========================================
