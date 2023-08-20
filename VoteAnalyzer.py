
# Date of completion:Aug 01,2023
# Brief explanation of the program: This program takes voting data as input, including the number of candidates,
# their last names, and the number of votes received by each candidate. It then processes this data and displays
# various statistics, including the total number of votes, the average number of votes, and a list of candidates
# who received more votes than the average.

# Define a function to get a valid number input from the user within a given range.
def get_valid_number(prompt, lower_bound, upper_bound):
    """
    Function to get a valid number input from the user within a given range.

    Parameters:
    prompt (str): The message to display when asking for input.
    lower_bound (int): The lower bound of the valid range.
    upper_bound (int): The upper bound of the valid range.

    Returns:
    int: The valid number entered by the user.
    """
    while True:
        try:
            # Ask the user to input a number and convert it to an integer.
            number = int(input(prompt))
            # Check if the number is within the specified range.
            if lower_bound <= number <= upper_bound:
                # Return the valid number.
                return number
            # If the number is not within the range, display an error message.
            print(f"Invalid entry. Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            # If the user enters a non-numeric value, display an error message.
            print("Invalid input. Please enter a valid number.")

# Define the main function to run the program.
def main():
    # Step a) Ask for the number of candidates in an election.
    num_candidates = get_valid_number("Enter the number of candidates (1 to 100): ", 1, 100)

    # Step b) Ask for the last names and votes received for each candidate.
    candidate_last_names = []
    votes_received = []
    for i in range(num_candidates):
        # Ask the user to enter the last name of the candidate.
        last_name = input(f"Enter the last name of candidate: ")
        # Append the last name to the list of candidate_last_names.
        candidate_last_names.append(last_name)

        # Step b) contd.: Ensure the number of votes is 0 or more.
        votes = get_valid_number(f"Enter the number of votes received by {last_name}: ", 0, float('inf'))
        # Append the number of votes to the list of votes_received.
        votes_received.append(votes)

    # Step c) and d) Display the header and candidate votes received.
    print("\nVOTE DATA – 08/01/2023")
    print("Candidate Votes Received")
    for i in range(num_candidates):
        # Display the name and votes received for each candidate.
        print(f"{candidate_last_names[i]:<15} {votes_received[i]:>5}")

    # Step f) Find and display the total number of votes casted.
    total_votes = sum(votes_received)
    print("\nTotal votes casted = ", total_votes)

    # Step g) Find and display the average number of votes casted.
    average_votes = total_votes / num_candidates
    print("Average votes = ", format(average_votes, ".2f"))

    # Step h) Display the header for candidates with votes more than average.
    print("\nList of candidates who received votes more than the average")

    # Step i) Display the name and number of votes for candidates with votes more than average.
    for i in range(num_candidates):
        if votes_received[i] > average_votes:
            # Display the name and votes of candidates who received more votes than the average.
            print(f"{candidate_last_names[i]:<15} {votes_received[i]:>5}")

# Run the main function if the script is executed as the main program.
if __name__ == "__main__":
    main()
