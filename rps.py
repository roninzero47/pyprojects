import random

class RockPaperScissor:

	def __init__(self,player):

		self.player = player

	def player_choice(self):

		user_choice = input('Rock, Paper or Scissors? ')

		return user_choice.lower()

	def computer_choice(self):

		comp_choice = random.choice(lst)

		return comp_choice.lower()

	def start_game(self,user_choice, comp_choice):

		if user_choice[0] == 'r':

			if comp_choice[0] == 's':

				print(f'{self.player} wins!')

			elif comp_choice[0] == 'p':

				print(f'{self.player} losses!')

			else:

				print('Draw')

		elif user_choice[0] == 'p':

			if comp_choice[0] == 'r':

				print(f'{self.player} wins!')

			elif comp_choice[0] == 's':

				print(f'{self.player} losses!')

			else:

				print('Draw')

		elif user_choice[0] == 's':

			if comp_choice[0] == 'p':

				print(f'{self.player} wins!')

			elif comp_choice[0] == 'r':

				print(f'{self.player} losses!')

			else:

				print('Draw')

		else:

			print('Wrong input')

if __name__ == '__main__':
	
	lst = ['rock','paper','scissor']

	print("Welcome to Rock Paper Scissors!")

	user = RockPaperScissor(input('Enter player name: '))

	game = True

	while game:

		user_play = user.player_choice()

		comp_play = user.computer_choice()

		print(comp_play)

		user.start_game(user_play, comp_play)

		choice = input("play again? ").lower()

		if choice[0] == 'n':
			
			print("Goodbye")
			
			game = False

			break

		elif choice[0] == 'y':

			pass

		else:

			print('wrong input')