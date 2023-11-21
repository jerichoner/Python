
# Let's start with the Calendar class.

from datetime import datetime, timedelta

class Calendar:
    def __init__(self):
        self.events = {}
    
    def add_event(self, name, date):
        self.events[date] = self.events.get(date, []) + [name]
    
    def display_events(self, date):
        return self.events.get(date, [])
    
    def delete_event(self, name, date):
        if date in self.events:
            self.events[date] = [event for event in self.events[date] if event != name]
            if not self.events[date]:
                del self.events[date]
    
    def display_upcoming_events(self, days_ahead):
        upcoming_events = {}
        current_date = datetime.now().date()
        end_date = current_date + timedelta(days=days_ahead)
        
        for date, events in self.events.items():
            if current_date <= date <= end_date:
                upcoming_events[date] = events
                
        return upcoming_events

# Next, let's implement the InventoryItem class.

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def increase_quantity(self, amount):
        self.quantity += amount
    
    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("Cannot decrease quantity below zero.")
    
    def total_value(self):
        return self.quantity * self.price

# Finally, let's implement the Student class.

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
    
    def add_grade(self, subject, grade):
        self.subjects[subject] = self.subjects.get(subject, []) + [grade]
    
    def average_grade(self):
        total_grades = 0
        count_grades = 0
        for grades in self.subjects.values():
            total_grades += sum(grades)
            count_grades += len(grades)
        return total_grades / count_grades if count_grades else 0

# Let's instantiate these classes to check if they work correctly.
calendar = Calendar()
inventory_item = InventoryItem('Widget', 100, 2.5)
student = Student('John Doe')

# Add some events, inventory adjustments and grades to test.
calendar.add_event('Meeting with team', datetime(2023, 11, 23).date())
inventory_item.increase_quantity(50)
student.add_grade('Math', 90)

# Print the results to verify the implementations.
print(calendar.display_events(datetime(2023, 11, 23).date()), 
 inventory_item.total_value(), 
 student.average_grade())

# The task is to develop a class for the game "Tic-Tac-Toe". The class should represent the game board and have methods for player moves (X and O), checking for a winner, and determining a draw.

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_turn = "X"
    
    def print_board(self):
        for row in self.board:
            print("|" + "|".join(row) + "|")
    
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_turn
            self.current_turn = "O" if self.current_turn == "X" else "X"
        else:
            raise ValueError("The cell is already occupied")
    
    def check_winner(self):
        # Check rows, columns and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[2][0]
        
        return None
    
    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True if self.check_winner() is None else False

# Let's instantiate this class and play a game to check if the methods work correctly.
game = TicTacToe()

# Make some moves
game.make_move(0, 0)  # X
game.make_move(1, 1)  # O
game.make_move(0, 1)  # X
game.make_move(1, 2)  # O
game.make_move(0, 2)  # X

# Print the board and check the game status.
game.print_board()
winner = game.check_winner()
is_draw = game.check_draw()

(winner, is_draw)
