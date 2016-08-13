import sopel.module
thing = "thing"
@sopel.module.commands('playcard','attack','ability','newturn','joingame')
def servermain(bot, trigger):
    def playcard(trigger):
        bot.say('playing card'+trigger)
    if trigger.group(1) == 'playcard':
        playcard(trigger.group(2))
        thing = "stuff"
    if trigger.group(1) == 'attack':
        #attack(trigger.group(2))
        bot.say(thing)
    if trigger.group(1) == 'ability':
        ability(trigger.group(2))
    if trigger.group(1) == 'newturn':
        bot.say('.newturn'+bot.memory[newturn])
        bot.memory[newturn] = bot.memory[newturn] + 1
        if bot.memory[newturn] >= playerCount:
            bot.memory[newturn] = 0
    if trigger.group(1) == 'joingame':
        bot.say(trigger.nick()+"is now joining the game")
        bot.memory[players[trigger.nick] = 
        


