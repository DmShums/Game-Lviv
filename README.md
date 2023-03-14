# Game&Lviv

## Wanderer Game

One of the program modules (main.py) was found on one of the resources for learning the Python programming language. After getting acquainted with this module, it became clear that this is the main module of the wanderer game.

The module consists of two parts. The first part allows you to create a game space, and the second is actually the main cycle of the game. A game space is created by creating rooms with a name and description. The mutual placement of rooms is arranged according to the cardinal directions. In the rooms are placed the characters of the game (friends and enemies), as well as items that you can try to use to fight the enemies. It is also established how the character will respond to an attempt to talk to him and the item that can be used to defeat the enemy.

After the construction of the playing field, the location of the player who has an empty shoulder bag where he can put items to fight enemies is set.

The main loop of the program is executed until the player dies, or until two enemies die. In the main cycle, information about the current room, characters that are there and objects in this room is displayed. The player can choose one of the following actions: move to another room, pick up an item, start a conversation, or start a fight.

If the player takes an item, it disappears from the room and appears in the player's shoulder bag. If the player chooses the direction behind which another room is located, then this room becomes the current room and the game continues. If the player starts a conversation, a message from the character is displayed on the screen. The fight with the enemy begins with entering the name of the item to fight, if such an item is in the shoulder bag and it is exactly such an item that can be defeated, then the player is credited with the first victory (the game lasts up to two victories). If the item is not suitable for fighting this enemy, then the player loses.

## Run file by using this command
```python
python3 main.py
```

## Wanderer Game in Lviv

Wandering through the streets of Lviv, you can meet students, gentlemen, rogues, misfits, batyars and slackers. On the street you can find various items that you can use to treat someone or protect yourself. If you managed to walk from Kozelnytska to Krakivska and back, you win. Otherwise, the game ends with your defeat.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
