import telebot
import nero_modle as ai
import time
from telebot import types
API_TOKEN = '7346294707:AAF3CdvR_R7pv2TcLuABsywQrbronwQWqoQ'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}
 def create_player_roles(num_players, player_names):
    roles = ['Воин', 'Маг', 'Клерик', 'Разбойник', 'Бард', 'Паладин', 'Друид', 'Варвар', 'Плут', 'Монах']
    # Создаем словарь для хранения информации о ролях игроков
    player_roles = {}
        
    # Заполняем словарь информацией о ролях
    for i in range(num_players):
        player_roles[player_names[i]] = f"{player_names[i]} это {random.choice(roles)}"
        
    return player_roles
        
@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'count': 0, 'names': []}
    video_file = open('1723633841534.mp4', 'rb')
    bot.send_video(message.chat.id, video=video_file)
    bot.send_message(message.chat.id, '''В далёком королевстве, где магия и чудеса являются обыденностью, а драконы и подземелья – частью повседневной жизни, начинается новая глава в истории героев. В этом мире, полном опасностей и приключений, вы – группа отважных искателей приключений, готовых бросить вызов тьме и защитить невинных от зла.
Ваша миссия – исследовать древние подземелья, полные ловушек, монстров и сокровищ, и раскрыть тайны, скрытые за их стенами. Вы столкнётесь с могущественными драконами, охраняющими свои сокровища, и другими опасностями, которые подстерегают вас на каждом шагу.
Но не только опасности ждут вас в этом путешествии. Вы найдёте верных союзников, которые помогут вам в борьбе с злом, и узнаете о себе много нового. Ваши решения и действия будут определять исход этой эпической битвы между добром и злом.
Пора начинать! Сколько человек будет играть? (введите число от 2 до 4)''', reply_markup=types.ReplyKeyboardRemove())

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

@bot.message_handler(commands=['fix'])
def ask_count(message):
    user_data[message.chat.id]['count'] = count
    bot.send_message(message.chat.id, f"Введите имена {count} человек, через пробел:")


@bot.message_handler(func=lambda message: message.chat.id in user_data and 0 < user_data[message.chat.id]['count'] <= 4)
def ask_names(message):
    names = message.text.split()
    if len(names) == user_data[message.chat.id]['count']:
        user_data[message.chat.id]['names'] = names
        bot.send_message(message.chat.id, f"Количество человек: {user_data[message.chat.id]['count']}")
        bot.send_message(message.chat.id, "Имена: " + ", ".join(names))
        keyboard = types.InlineKeyboardMarkup()
        key_go = types.                InlineKeyboardButton(text='Поехали 🔮', callback_data='go')
# И добавляем кнопку на экран
        keyboard.add(key_go)
        bot.send_message(message.chat.id, f"Поехали? Если закралась ошибка придётся нажать /start", reply_markup=keyboard)        
        del user_data[message.chat.id]
    else:
        bot.send_message(message.chat.id, f"Пожалуйста, введите ровно {user_data[message.chat.id]['count']} имен. Через пробел.")

@bot.callback_query_handler(func=lambda call: call.data == 'go')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id  
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Мне надо несколько минут для генерации истории, пожалуйста, подождите. История загрузится автомотически ничего делать не недо. Магия скоро произайдёт')  
    bot.send_message(message.chat.id, f"⌛️")
 

    # Пример использования функции

    player_roles = create_player_roles(user_data[message.chat.id]['count'], user_data[message.chat.id]['names'])
    user_data[message.chat.id]['roles'] = player_roles
    message_text = ai.giga_get("Что такое промт?")
    context_text = message_text
    bot.send_message(message.chat.id, message_text)
    bot.send_message(message.chat.id, player_roles)

bot.polling()
