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

_7 in collision code, take away prey when _collision is detected

_8 make text in the top left of screen with score
_9 when collision is detected add 1 to score


________END:__________

Looks like we are almost done.

to add some competition to the game, this is what I have to do next:

1 add a hunter pic(should be biggest looking and largetst range of speed)


2 make a hunter class
3 hunter class randomly runs around(like prey)



4 when hunter touches lion, loose hp
  - lion starts with 10 hp
  - if hunter touches lion, -3 hp
  - if lion eats prey, +1 hp
  - if hp <= 0, game over screen



to decide whether a hunter spawns, pick a random number. if that random number is even, spawn a hunter.

code for that

num = random.randint(0, 3)
if num % 2 == 0:
  hunters.add(Hunter(event.pos))



hunters die after a certain amount of time

TO DO THAT:

when hunter is created, store that time
in loop for hunter, check if current time is still in that 'window'

METHOD FOR THAT

get tics gives current time:
pygame.time.get_ticks()

can use stack overflow