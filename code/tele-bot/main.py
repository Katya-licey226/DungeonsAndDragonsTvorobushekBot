import telebot

API_TOKEN = '7346294707:AAF3CdvR_R7pv2TcLuABsywQrbronwQWqoQ'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'count': 0, 'names': []}
    bot.send_message(message.chat.id, '''В далёком королевстве, где магия и чудеса являются обыденностью, а драконы и подземелья – частью повседневной жизни, начинается новая глава в истории героев. В этом мире, полном опасностей и приключений, вы – группа отважных искателей приключений, готовых бросить вызов тьме и защитить невинных от зла.
Ваша миссия – исследовать древние подземелья, полные ловушек, монстров и сокровищ, и раскрыть тайны, скрытые за их стенами. Вы столкнётесь с могущественными драконами, охраняющими свои сокровища, и другими опасностями, которые подстерегают вас на каждом шагу.
Но не только опасности ждут вас в этом путешествии. Вы найдёте верных союзников, которые помогут вам в борьбе с злом, и узнаете о себе много нового. Ваши решения и действия будут определять исход этой эпической битвы между добром и злом.
Пора начинать! Сколько человек будет играть? (введите число от 2 до 4)''')

@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id]['count'] == 0)
def ask_count(message):
    try:
        count = int(message.text)
        if 2 <= count <= 4:
            user_data[message.chat.id]['count'] = count
            bot.send_message(message.chat.id, f"Введите имена {count} человек, через пробел:")
        else:
            bot.send_message(message.chat.id, "Пожалуйста, введите число от 2 до 4.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число.")

@bot.message_handler(func=lambda message: message.chat.id in user_data and 0 < user_data[message.chat.id]['count'] <= 4)
def ask_names(message):
    names = message.text.split()
    if len(names) == user_data[message.chat.id]['count']:
        user_data[message.chat.id]['names'] = names
        bot.send_message(message.chat.id, f"Количество человек: {user_data[message.chat.id]['count']}")
        bot.send_message(message.chat.id, "Имена: " + ", ".join(names))
bot.send_message(message.chat.id, f"Поехали?")        
        del user_data[message.chat.id]
    else:
        bot.send_message(message.chat.id, f"Пожалуйста, введите ровно {user_data[message.chat.id]['count']} имен. Через пробел.")



bot.polling()