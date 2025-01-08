# Creating a shopping list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Quit")
    
# Adding a item to the shopping list 
def add_item(shopping_list):
    # Prompt the user to input an item and adds it to the shopping list.
    item = input("Enter an item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list")
    
# Removing an item from the shopping list
def remove_item(shopping_list):
    # Prompt the user to input an item and then remove it from the shopping list.
    item = input("Enter an item name to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"Item '{item}' is not found in your shopping list.")
        
def display_list(shopping_list):    
    # Displaying the shopping list
     if shopping_list:
         print("\n Your Shopping List: ")
         for item in shopping_list:
             print(f"- {item}")
     else: 
         print("Your shopping list is currently empty.")
         
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_item(shopping_list)
            
        elif choice == "2":
            remove_item(shopping_list)
            
        elif choice == "3":
            display_list(shopping_list)
            
        elif choice == "4":
            print("Goodbye! Have a great day!")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
                   
    