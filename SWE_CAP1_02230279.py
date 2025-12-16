#SWE_CAP1_02123456.py
################################
# Your Name
#print ("Name: Chimi GYeltshen")
# Your Section
#print("Section: A") 
# Your Student ID Number
#print("Student ID : 02230279")
################################
# REFERENCES
#https://www.youtube.com/watch?v=LpZmZs2_BC4
#https://www.youtube.com/watch?v=bEGHcXUivls
#https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
################################
# SOLUTION
# Your Solution Score: Total Score is : 39920
# Put your number here
################################



def read_input():
    with open('RA CAP1/input_9_cap1.txt') as file:
        return file.readlines()

def calculate_choice(outcome, opponent_choice):
    if outcome == 'X':  # (X = lose ) so desired outcome is to lose
        if opponent_choice == 'A':
            return 'scissors'
        elif opponent_choice == 'B':
            return 'rock'
        elif opponent_choice == 'C':
            return 'paper'
    elif outcome == 'Y':  # (Y = draw )so desired outcome is to draw
        if opponent_choice == 'A':
            return 'paper'
        elif opponent_choice == 'B':
            return 'scissors'
        elif opponent_choice == 'C':
            return 'rock'
    elif outcome == 'Z':  # (A = win ) s0 desired outcome is to win
        if opponent_choice == 'A':
            return 'rock'
        elif opponent_choice == 'B':
            return 'paper'
        elif opponent_choice == 'C':
            return 'scissors'

def calculate_score(player_choice, opponent_choice):
    # values for each shape
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}

    # Determine the outcome of the round
    if player_choice == opponent_choice:
        result = 'draw'
    elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
         (player_choice == 'paper' and opponent_choice == 'rock') or \
         (player_choice == 'scissors' and opponent_choice == 'paper'):
        result = 'win'
    else:
        result = 'lose'

    # Calculate the score for the round based on the outcome and choice
    player_score = choices[player_choice]
    if result == 'win':
        player_score += 6
    elif result == 'draw':
        player_score += 3

    return player_score


def main():
    rounds = read_input()

    if rounds is None:
        print("Error: No input data found.")
        return

    total_score = 0
    rounds_played = 0  
    
    # choices dictionary
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}

    for round_info in rounds:
        # Check if three rounds have been played or not
        if rounds_played >= 10001:
            break  # If three rounds have been played, exit the loop

        opponent_choice, outcome = round_info.split()
        
        # Calculate your choice for the round
        player_choice = calculate_choice(outcome, opponent_choice)

        # Calculating the score for the round
        round_score = choices[player_choice] + calculate_score(player_choice, opponent_choice)
        
        # Increment the rounds played count by one to keep track of the number of rounds 
        rounds_played += 1

        # Updating the total score with each round's score 
        total_score += round_score

       

    # Total score (sum of scores for all three rounds)
    print("Total Score is :", total_score)

if __name__ == "__main__":
    main()
