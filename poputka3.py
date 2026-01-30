import re


MEMORY_FILE = "memory.json"

responses = {
    "привет": "Привет Как я могу тебе помочь",
    "как дела": "У меня все отлично спасибо! А у тебя",
    "пока": "До свидание! Обрашайся еще",
    "ты кто": "Я маленький ИИ"
}


error = "я не понял повторите еще раз "

intentions = {
    "greeting": {
        "keys": ["привет", "здравствуйте", "хай"],
        "answer": "Привет! Рад тебя видеть 😊"
    },
    "bye": {
        "keys": ["пока", "до свидания", "bb"],
        "answer": "Пока! Хорошего дня 👋"
    },
    "ask_name": {
        "keys": ["как меня зовут", "скажи моё имя",],
        "answer": "Я пока не знаю твоё имя, но могу запомнить!"
    },
    "save_name": {
        "keys": ["запомни моё имя", "мое имя"],
        "answer": "Хорошо, скажи — как тебя зовут?"
    },
    "ask_age": {
        "keys": ["скажи мой возраст", "какой у меня возраст"],
        "answer": "Возраст я пока не знаю, но могу запомнить!"
    },
    "save_age": {
        "keys": ["запомни мой возраст", "сколько мне лет"],
        "answer": "Хорошо, скажи — сколько тебе лет?"
    },
    "ask_mood": {
        "keys": ["какое у меня настроение", "как моё настроение"],
        "answer": "Не уверен, но могу попытаться угадать 🙂"
    },
    "save_mood": {
        "keys": ["запомни моё настроение"],
        "answer": "Хорошо, расскажи — какое у тебя настроение?"
    },
    "unknown": {
        "keys": [],
        "answer": "Я тебя понял, но пока не знаю, как ответить 🙂"
    }
}



memory = {
    "name":"",
    "age":"",
    "mood":""
}


memorys = {}


while True:
    msg = input("You:")
    if msg in responses:
        print("Ai:", responses[msg] )
    if msg.startswith("запомни"):
        word = msg.replace("запомни","")
        memorys[word] = True
        print("Ai: запомнено")



    def normalize(text: str) -> str:
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
        text = re.sub(r'\s+', '', text)
        return text


    def get_category(text: str) -> str:
        words = text.split()

        for cat,data in intentions.items():
            for key in data['keys']:
                k = normalize(key)

                if "" not in k:
                    if k in words:
                        return cat
                else:
                    if k in words:
                        return cat
        return "unknown"




    msg = input("you:").strip()
    if msg.lower() == "exit":
        print("Ai off")
        break

    norm = normalize(msg)
    cat = get_category(norm)

    if cat in ["greeting", "bye"]:
        print("Ai:", intentions[cat]["answer"])
        continue

    if cat == "save_name":
        print("Ai:", intentions[cat]["answer"])
        name = input("name:").strip()
        memory["name"] = name
        print("Ai: Отлично, запомнил!")
        continue

    if cat == "save_age":
        print("Ai:", intentions[cat]["answer"])
        age = input("name:").strip()
        memory["age"] = age
        print("Ai: Отлично, запомнил!")
        continue

    if cat == "save_mood":
        print("Ai:", intentions[cat]["answer"])
        mood = input("name:").strip()
        memory["mood"] = mood
        print("Ai: Отлично, запомнил!")
        continue

    if cat == "ask_name":
        if memory["name"]:
            print("Ai: Тебя зовут", memory["name"])
        else:
            print("AI: Я пока не знаю твоё имя")
        continue

    if cat == "ask_age":
        if memory["age"]:
            print("Ai: Тебя ", memory["age"], "лет")
        else:
            print("AI: Я пока не знаю твой возраст")
        continue

    if cat == "ask_mood":
        if memory["mood"]:
            print("Ai:У тебя настроение-", memory["mood"])
        else:
            print("AI: Я пока не знаю твоё настроение ")
        continue

    if msg in responses:
        print(responses[msg])
        continue
    if msg == "выход":
        break



    print("Ai:", intentions["unknown"]["answer"])



