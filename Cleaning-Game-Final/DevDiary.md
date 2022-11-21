# Cleaning Game Dev Diary
By: Nolan Kelley, Matthew Adner, and Olivia Riley.

## Planned Features:
REMEMBER: These are from the original design document and meeting all of these isn't our goal.
Don't feel bad if we don't make a lot of these.
- [x] States
    - [x] Start state
        - [x] Title screen 
        - [x] Button to start game
    - [x] Running state
- [x] Player
    - [x] Walk w/ WASD
    - [x] Clean messes
    - [x] Complex animations
    - [x] Taking damage (health)
    - [x] Dying
- [ ] Broom 
    - [x] Separate object
    - [x] Player controlled rotation
    - [x] Rotate around end of handle
    - [x] Follow player
    - [x] Damage roombas
    - [ ] Cleaning animation
- [ ] Roombas
    - [ ] Be based on a FSM
    - [x] Clean messes after colliding with them for a bit
    - [x] Damage player
    - [ ] Have HP
    - [ ] Take knockback from the broom
    - [x] Become broken after hit
        - [x] Be picked up after broken
        - [x] Add to score
    - [x] Rotating sprites
    - [x] Various types
        - [x] Normal
        - [x] Homing
            - [x] Player
            - [x] Messes
            - [x] Both
        - [x] Mush
        - [ ] Weak
        - [ ] Boss
- [x] Messes
    - [x] Draw messes
    - [x] Disappear when cleaned
    - [x] Add to score
- [ ] Rooms/Levels
    - [x] Get individual rooms working
    - [ ] Multiple rooms connected to eachother making one level
    - [x] Cleaning all messes sends player to next level
    - [x] Drawing background
- [x] Score
    - [x] Print to screen durring gameplay
- [ ] Endings
    - [x] Lose screen
    - [x] Win Screen
        - [ ] Different win screens based on score (purely time issue)


## Completed Unplanned Features:
* States
    - [x] Pause screen
    * Win screen 
        - [x] Game can be played again
            - [x] Game changes after first completion (Pause screen won't appear.)
* Player
    - [x] Hitbox is separate object only around the player's feet
* Other
    - [x] Interface animations (lose screen dropping from above/health bar falling)
    - [x] Debugg mode (press d on start screen)