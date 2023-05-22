
translations = {
    "buy_me_a_pen":{
        "ta":"எனக்கு ஒரு பேனா வாங்க",
        "en":"buy_me_a_pen",
        "fr":"achète moi un stylo",
        "hi":"मुझे एक कलम खरीदो"
    }
}

def translate(func):
    def wrapper(*args,**kwargs):
        msg,lang = func(*args,**kwargs)
        return translations[msg][lang]
    return wrapper

@translate
def say(lang="en"):
    msg = "buy_me_a_pen"
    return msg,lang

print(say("fr"))