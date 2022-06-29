import telebot

CHAVE_API = "" #Chave API gerada pelo BotFather do telegram deve ser inserida aqui

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "Você escolheu a opção 1")
    bot.send_message(mensagem.chat.id, menu)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Você escolheu a opção 2")
    bot.send_message(mensagem.chat.id, menu)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Você escolheu a opção 3")
    bot.send_message(mensagem.chat.id, menu)

def verificar(mensagem):
    if mensagem.text == "1":
        return opcao1(mensagem)
    if mensagem.text == "2":
        return opcao2(mensagem)
    if mensagem.text == "3":
        return opcao3(mensagem)
    else:
        return menu

menu = """Escolha uma das opções abaixo para continuar:
1 - /opcao1 - fazer x
2 - /opcao2 - fazer y
3 - /opcao3 - fazer z
        
obs: clique em uma opção ou digite o número equivalente"""

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, menu)

bot.polling() #função usada para o bot ficar em loop