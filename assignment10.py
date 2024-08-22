"""
#Task 1: Formatting Flight Itineraries 

def search_flights(flights):
  for flight in flights:
      #print(f"Itinerary: {flight[0]} - From {flight[1]} to {flight[2]}")
      name, origin, depart = flight
      print(f"{name} - From {origin} to {depart}")
      
  
def main():
  flight_itineraires = (
    ("Itinerary 1: Alice", "New York", "London"),
    ("Itinerary 2: Bob", "Tokyo", "San Francisco")
  )

  while True:
    print("\nMake a selection!")
    print("1. View Current flights")
    print("2. Exit")
    choice = input("Make a selection: ")

    if choice == "1":
      search_flights(flight_itineraires)
    elif choice == "2":
      print("Exiting program")
      break
    else:
      print("Invalid choice, please try again!")

if __name__ == "__main__":
  main()

#Task 2: Library System Enhancement

def add_books_verify_books(library):
  book_title = input("Type in book title to add: ")
  author = input("Type Author's full name: ")
  library.append((book_title, author)) #book_title[0], author[1]
  if book_title == library:
    print("Book already exists in the library!")
  elif book_title and author != library:
    print("The book has been added to the library")
  else:
    print("Something went wrong!")

def view_library(library):
  for x in library:
    print(f"{x}") 

def main():
  library_abc = [
    ("1984", "George Orwell"), 
    ("Brave New World", "Aldous Huxley")
  ]

  while True:
    print("\n1. Add a book")
    print("2. View library")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      add_books_verify_books(library_abc)
    elif choice == "2":
      view_library(library_abc)
    elif choice == "3":
      print("Thanks for stopping by!")
      break

if __name__ == "__main__":
  main()
"""
#Task 3: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

def restaurant_orders(ordered_food):
  for x in ordered_food:
    print(f"Order: {x}")

def main():
  orders = [
      ("Alice", "Laptop", 1),
      ("Bob", "Camera", 2),
      # More orders...
  ]

  while True:
    print("1. View library")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      restaurant_orders(orders)
    elif choice == "2":
      print("Thanks for visiting the restaurant!")
      break

if __name__ == "__main__":
  main()