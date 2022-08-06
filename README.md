# SpaceInvaders

Space Invaders is a game where the user plays with a ship and shoots down aliens. The game was created with **Python** and the **pygame** module. 

## Gameplay

### Difficulty Modes
Before the user starts to play the game, they are prompted with a menu screen. The menu features three difficulty modes: easy, medium, and difficult. Easy mode allows the user to have 5 lives and the aliens move considerably slow whereas in medium mode, the user has 3 lives and the aliens move nearly as fast as the play. In difficult mode, the aliens move significantly faster than the aliens in medium mode and the user only has 2 lives.  

### Gameplay Mechanics
When done selecting the mode, the user can click the "Play" button on the menu screen or press 'P' on their keyboard to start the game. The user controls a ship by moving left and right with the arrow keys on their keyboard and shoot bullets with the 'W' button. There is a ship counter on the top left of their screen, a high score tracker on the top of the screen, and the current score tracker along with the current level indicator to the right of the screen. If the user is able to clear all of the aliens off of the screen, they move on to the next level. However, if the user is not able to clear all of the aliens or collides with an alien, they lose a live. Once they lose all of their lives, they are unable to keep playing and the game will terminate. Additionally, the user can leave the game at any time by pressing the 'Q' button.

## High Scores
Once the user is done playing the game, a *high_scores.json* file will be created (if it's the users first time playing) and write their high score on a new line in the file

## Screenshots of Game
<img width="1440" alt="startingmenu" src="https://user-images.githubusercontent.com/92037532/183268820-0f8f2372-048f-49e1-8f42-fd9ffca19500.png">
<br>
<br>
<img width="1440" alt="gameplay" src="https://user-images.githubusercontent.com/92037532/183268858-d4bc1f3b-dfe2-4521-b039-a15ddafcaf22.png">
