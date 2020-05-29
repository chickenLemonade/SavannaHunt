the game is a lion chasing its prey around a field

the lion is like pacman
the prey are like the fish

when the lion touches prey, it says something

everytime the lion touches its prey, add 1 to the score

__________STEPS:____________

_1 make background
_2 get pic of prey
_3 make prey code(randomly runs around)
_4 get pic of lion
_5 make lion code(move with keys)
_6 make collision code

__________OPTIONAL:____________

7 in collision code, take away prey when collision is detected

_8 make text in the top left of screen with score
_9 when collision is detected add 1 to score

10 when collision is detected, make lion pic one of an eating lion and time.sleep(2)


__________THE CODE FOR 7 PARTIALLY MADE IS...__________


if event.key == K_d:
  for i in range(len(fishes) // 2):
  fishes.pop(0)