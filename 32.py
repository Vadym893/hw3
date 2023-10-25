interest_in_computer_science = None
like_playing_computer_games = None
has_instagram_account = None

print("Survey Questions:")
interest_in_computer_science = input("Are you interested in computer science? (Y/N): ").upper() == 'Y'
like_playing_computer_games = input("Do you like playing computer games? (Y/N): ").upper() == 'Y'
has_instagram_account = input("Do you have an Instagram account? (Y/N): ").upper() == 'Y'

print("\nSurvey Results:")
print("Interested in computer science:", "Yes" if interest_in_computer_science else "No")
print("Playing computer games:", "Yes" if like_playing_computer_games else "No")
print("Has an Instagram account:", "Yes" if has_instagram_account else "No")
