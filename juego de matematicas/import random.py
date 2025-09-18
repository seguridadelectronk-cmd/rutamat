import random

print("vamos a jugar Piedra, Papel o tijera")

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
  player_choice = input("\nIngrese Piedra, papel o Tijera: ").lower()
  choices = ["piedra", "papel", "tijera"]
  computer_choice = random.choice(choices)
  print(f"Computer chose: {computer_choice}")

  if (player_choice == "piedra" and computer_choice == "tijera") or (player_choice == "tijera" and computer_choice == "papel") or (player_choice == "papel" and computer_choice == "piedra"):
    winner = "Player"
  elif player_choice == computer_choice:
    winner = "Tie"
  else:
    winner = "Computer"

  if winner == "Player":
    player_wins += 1
    print("Ganaste")
  elif winner == "Computer":
    print("he ganado yo")
    computer_wins += 1
  else:
    print("esto es un empate")

  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

  if player_wins > computer_wins:
   print("Felicitaciones ¡Ganaste!")
else:
  print("GAME OVER")