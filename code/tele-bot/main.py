import telebot
import nero_modle as ai
import random
from telebot import types

API_TOKEN = '7346294707:AAF3CdvR_R7pv2TcLuABsywQrbronwQWqoQ'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

def create_player_roles(num_players, player_names):
    roles = ['Воин', 'Маг', 'Клерик', 'Разбойник', 'Бард', 'Паладин', 'Друид', 'Варвар', 'Плут', 'Монах']
    player_roles = {}
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

@bot.message_handler(func=lambda message: message.chat.id in user_data and 0 < user_data[message.chat.id]['count'] <= 4)
def ask_names(message):
    names = message.text.split()
    if len(names) == user_data[message.chat.id]['count']:
        user_data[message.chat.id]['names'] = names
        bot.send_message(message.chat.id, f"Количество человек: {user_data[message.chat.id]['count']}")
        bot.send_message(message.chat.id, "Имена: " + ", ".join(names))
        keyboard = types.InlineKeyboardMarkup()
        key_go = types.InlineKeyboardButton(text='Поехали 🔮', callback_data='go')
        keyboard.add(key_go)
        bot.send_message(message.chat.id, f"Поехали? Если закралась ошибка придётся нажать /start", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, f"Пожалуйста, введите ровно {user_data[message.chat.id]['count']} имен. Через пробел.")

@bot.callback_query_handler(func=lambda call: call.data == 'go')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Мне надо пару мнгновений для настройки игры, пожалуйста, подождите. Настройки автомотически применются ничего делать не недо.')
    bot.send_message(message.chat.id, f"⌛️")
    # Example usage of the ai module

    
    count_get = user_data[message.chat.id]['count']
    name_get = user_data[message.chat.id]['names']
    bot.send_message(message.chat.id, count_get)
    bot.send_message(message.chat.id, name_get[0])
    bot.send_message(message.chat.id, name_get[1])
    player = [0] * count_get
    rolei = [0] * count_get
    super_mana = 0
    gold = 0
    veriants1 = [0] * 3 
    veriants2 = [0] * 3 
    veriants3 = [0] * 3 
    veriants4 = [0] * 3 
    round = count_get * 2
    roles = ['Воин', 'Маг', 'Разбойник', 'Бард', 'Друид', 'Варвар', 'Монах']
    for i in range (count_get):
        nober = random.uniform(0, 9)
        player[i] = f"{name_get[i]} это {roles[nober]}"
        rolei [i] = roles[nober]
        bot.send_message(message.chat.id, player[i])
        if rolei[i] == 'Маг' or rolei[i] == 'Монах':
            live [i] = 3
            mana [i] = 5
            gold += 3
            super_mana += 1
            if d != 0:
                join = i
                kat = 1
                d == 0
                veriants1 = ['Призвать пипенюга', 'Призвать тучку', 'Превратить верёвку в ковёр самолёт']
        elif rolei[i] == 'Воин' or rolei[i] == 'Разбойник' :
            live [i] = 5
            mana [i] = 10
            gold += 4
            if d != 0 :
                join = i
                kat = 2
                d == 0
                veriants1 = ['Достать верёвку', 'Отрезать верёвку', 'Повесить вёрёвку на колышек и помочь']
        else :
            live [i] = 6
            mana [i] = 3
            gold += 7
            if d != 0 :
                join = i
                kat = 3
                d == 0
                veriants1 = ['Оплатить доставку за 2 монеты', 'Подкупить гоблина', 'Обратиться к колдуньи за 2 монеты']
                veriants3 = ['Дать верёвку', 'Подать факел', 'Спуститься вниз']
    get_q1 = veriants1[random.uniform(0,2)]
    get_q2 = veriants2[random.uniform(0,2)]
    get_q3 = veriants3[random.uniform(0,2)]
    get_q4 = veriants4[random.uniform(0,2)]
        
        
    message_text = ai.giga_get(f'''
Сочини историю для игры Подземелье и драконы без своих комментариев где будет {count_get}  игроков, где {player}  и где {player[random.uniform(0,count_get - 1)]} идёт исследовать яму и случайно попадается в ловушку а остальные должны помочь, вариантов есть несколько: 1){get_q1} 2){get_q2} 3){get_q3} 4){get_q3}
''')
    keyboard_1 = types.InlineKeyboardMarkup()
    q1 = types.InlineKeyboardButton(text=get_q1, callback_data='yes')
    q2 = types.InlineKeyboardButton(text=get_q1, callback_data='no')
    q3 = types.InlineKeyboardButton(text=get_q1, callback_data='yes')
    q4 = types.InlineKeyboardButton(text=get_q1, callback_data='no')
    get_pin = random.uniform(0, 3) 
    if get_pin == 1:
        keyboard_1.add(q4)
        keyboard_1.add(q2)
        keyboard_1.add(q3)
        keyboard_1.add(q1)
    elif get_pin == 2:
        keyboard_1.add(q1)
        keyboard_1.add(q2)
        keyboard_1.add(q3)
        keyboard_1.add(q4) 
    elif get_pin == 3:
        keyboard_1.add(q1)
        keyboard_1.add(q4)
        keyboard_1.add(q3)
        keyboard_1.add(q2) 
    else:
        keyboard_1.add(q1)
        keyboard_1.add(q2)
        keyboard_1.add(q3)
        keyboard_1.add(q4)
    if super_mana > 0 :
        key_mana = types.InlineKeyboardButton(text=f"Супер-Мана ✨ (осталось {super_mana} использований)", callback_data='yes')
        keyboard_1.add(Key_mana)
    bot.send_message(message.chat.id, message_text,  reply_markup=keyboard_1)
bot.polling()