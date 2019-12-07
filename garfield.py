from time import sleep
from termcolor import colored
from random  import choice
from simpleeval import simple_eval

class Bot:
    
    wait = 1
    
    # self.runtype: run type of the bot, can be 'once' or 'looped', default to 'once'

    def __init__(self, runtype = 'once'):
        self.runtype = runtype
        self.q = ''
        self.a = ''
        
    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'green')
    
    def _run_once(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _run_looped(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['x', 'q', 'exit', 'quit']:
                break
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))
        
    def run(self):
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'looped':
            self._run_looped()

class HelloBot(Bot):
    def __init__(self, runtype = 'once'):
        super().__init__(runtype)
        self.q = "Hi, what is your name?"
        
    def _think(self, s):
        return f"Hello {s}!"

class GreetingBot(Bot):
    def __init__(self, runtype = 'once'):
        super().__init__(runtype)
        self.q = "How are you today?"
    
    def _think(self, s):
        if 'good' in s.lower() or 'great'in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that" 

class FavoriteColorBot(Bot):
    def __init__(self, runtype = 'once'):
        super().__init__(runtype)
        self.q = "What's your favorite color?"
        
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {choice(colors)}"

class CalcBot(Bot):
    def __init__(self, runtype = 'once'):
        super().__init__(runtype)
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try,input 'q' 'x' 'quit' or 'exit' to quit:"
        
    def _think(self, s):
        result = simple_eval(s)
        return f"Done.Result = {result}"

class Garfield:
    
    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []
        
    def add(self, bot):
        self.bots.append(bot)
        
    def _prompt(self, s):
        print(s)
        print()
    
    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

garfield = Garfield(1)
garfield.add(HelloBot())
garfield.add(GreetingBot())
garfield.add(FavoriteColorBot())
garfield.add(CalcBot('looped'))
garfield.run()