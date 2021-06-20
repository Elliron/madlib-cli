import re  # imports regex

# Global Variables
short_template_dark_and_stormy = "../assets/dark_and_stormy_night_template.txt" # test template
long_template_video_game = "../assets/video_game.txt" # main game template

# Functions

# Welcome and Game Intro
def welcome():
  """
  The function will print a welcome message.
  The function will print instructions on how to play the game.
  """
  print("""
                           Hi, Welcome to Madlibs!!!
                           -------------------------
                  Follow the instructions below to play the game.
                  -----------------------------------------------
    You will be able to chose between a long and a short version of the game.
  
                         To quit at any time enter quit.
  
               The game will ask you for an adjective, noun, name, etc.
  
          The game will then take your answers and use them to finish a story.
  
                             Good luck and have fun!
  """)

# Starts game and selects long or short version
def game_start():
  """
  The function will start the game.
  The function will ask the user if they want to play a long or short game.
  The function will play the long or short version based on the user's input.
  If the user types in "quit" the game will exit.
  """

  print("""
  Choose a version:
  >>> Long
  >>> Short
  """)
  individual_user_input = input(">>> ")
  if individual_user_input != "QUIT":
    
    if individual_user_input.lower() == "short":
      print("Starting Short Game")
      play_the_game(short_template_dark_and_stormy)

    if individual_user_input.lower() == "long":
      print("Starting Long Game")
      play_the_game(long_template_video_game)

  else:
    print("Otay Bye!")

# Actual Madlibs game code for playing the game
def play_the_game(asset_template_file_chosen_by_user: str): # expects a string as value
  """
  The function will take in the template chosen by the user as a string.
  The function will create a list of the users input.
  The function will open the template chosen by the user using the read_template function.
  The function will parse and print the placeholder words in the chosen template to the user, asking for an Adjective, Noun, etc.
  The function will turn the list of users input into a Tuple.
  The function will merge the Tupled list of user input into the chosen template replacing the place holder words in order.
  The function will print the finished template with the users input to the user.
  The function will invoke the save_story function to save finished story to the assets folder as "user_input_storage".
  """
  
  # function setup, reads and parses information
  list_of_user_inputs = []
  opened_template_file_chosen_by_user = read_template(asset_template_file_chosen_by_user)
  returns_everything_between_curly_brackets_in_templates = parse_template(opened_template_file_chosen_by_user)

  # list_of_nouns_adjectives_verbs_from_template
  list_of_nouns_adjectives_verbs_from_template = returns_everything_between_curly_brackets_in_templates[1]
  template_with_curly_bracket_strings_removed = returns_everything_between_curly_brackets_in_templates[0]

  # for loop, looping through template user chose and printing a request for the value in the template.  The value being an Adjective, Noun, Name, etc.  If the user types in quit it exits the game.
  for each_adjective_verb_etc_being_asked_for in list_of_nouns_adjectives_verbs_from_template:
    print("Give me a(n):", each_adjective_verb_etc_being_asked_for)
    individual_user_input = input("Enter Here:>>> ")
    if individual_user_input !='QUIT':
      list_of_user_inputs.append(individual_user_input)
    else:
      print("GAME OVER!")
      quit()

  tupled_list_of_user_inputs = tuple(list_of_user_inputs)
  completed_story_output = merge(template_with_curly_bracket_strings_removed, tupled_list_of_user_inputs)

  print(completed_story_output)

  save_story(completed_story_output)

# Function saves completed story to assets folder
def save_story(completed_story_saved_to_assets_folder):
  with open("../assets/user_input_storage.txt", "w") as asset_template_file_chosen_by_users:
    asset_template_file_chosen_by_users.write(completed_story_saved_to_assets_folder)

# Main Function Invocations
def main_function_invocations():
  """
  The function will invoke the game.
  """
  welcome()
  game_start()

# Function that opens and reads a file string/text
def read_template(str):
  """
  The function will take in a string.
  The function will open a file for reading only.
  The function will return FileNotFound if it cannot find the file.
  """

  with open(str, "r") as template_file:
    try:
      contents = template_file.read()
      return contents
    except FileNotFoundError as error:
      print(error, "File does not exit")

# Parses string/text inside curly brackets from template and returns the string without the curly brackets
def parse_template(str):
  """
  The function will parse a string.
  The function will look for information between curly brackets.
  The function will make the information a tuple.
  """

  stripped = str

  # Regex grabs everything between curly brackets without brackets
  # Kassies Regex from Code Review
  # Tuple makes it so they can't be changed
  parts = tuple(re.findall(r"\{(.*?)\}", stripped))

  str = re.sub(r"\{(.*?)\}", "{}", stripped)

  return (str, parts)

# Merges string and tuple togethor
def merge(str, tuple):
  """
  The function will merge a string and a tuple
  """

  return str.format(*tuple)

if __name__ == "__main__":
  main_function_invocations()