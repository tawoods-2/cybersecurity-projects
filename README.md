# Cybersecurity Python Practice

This repository contains Python scripts I am building while learning cybersecurity and penetration testing. 

## Current Scripts
- first_script.py: Basic port scanning practice
- port_scanner.py: Additional port scanning practice
- rock_paper_scissors.py: Basic rock, paper, scissors game 
- loan.py: Basic mortgage loan calculator

## Goals
- Improve scripting skills
- Build tools for penetration testing
- Document my progress 

## Port Scanner (Version 1)

This is a basic Python port scanner that checks ports 1-10 on a target IP address.

### Features
- Takes user input for target
- Scan multiple ports
- Identifies open vs closed ports

### What I Learned
- Python loops
- User input handling
- Basic networking with sockets
- How port scanning works

### Note
This project is for learning purposes only. 

## Rock Paper Scissors Game

This is a simple Python game where the user plays Rock, Paper, Scissors against the computer. 

### Features
- Random computer choice using Python's 'random' module
- User input handling
- Game logic for win, lose, or tie 

### How it works 
1. The user selects rock, paper, or scissors 
2. The computer randomly selects an option 
3. The program compares both choices and determines the result

### Example Output

Do you want rock, paper, or scissors? Rock WIN! Computer choice: scissors

### File
- rock_paper_scissors.py

## Loan Calculator 

This project simulates a loan payment over time, including interest calculations and monthly payments. 

### Features
- Takes user input for: 
    - Loan amount 
    - Annual percentage
    - Monthly payment 
    - Number of months 
- Calculates monthly interest 
- Applies payments over time using a loop 
- Stops early if fhe loan is fully paid off 
- Displays remaining balance after each payment 

### Example Output 
Paid 1000.00 of which 125.00 was interest Now I owe 49125.00
Paid 1000.00 of which 122.81 was interest Now I owe 48247.81 ...
The last payment is 850.23 You paid off the loan in 24 months

### Skills Demonstrated 
- User input handling
- Type conversion ('float', 'int')
- Loops ('for')
- Conditional logic ('if')
- Basic financial calculations 
- Output formatting (rounding to 2 decimal places)

### Notes
- Values are formatted to 2 decimal places for readability 
- Full precision is used during calculations for accuracy 
- Script is designed for learning purposes