import amino
client = amino.Client()
client.login(email='yourlogin', password='yourpassword')
sub_clients = amino.SubClient(comId='156542274', profile=client.profile)

oldMessages = []
while True:
	readChats = sub_clients.get_chat_threads(start=0, size=3).chatId
	for chat in readChats:
		messageList = sub_clients.get_chat_messages(size=2, chatId=chat)
		chatInfo = sub_clients.get_chat_thread(chatId=chat)
		for nickname, content, id in zip(messageList.author.nickname, messageList.content, messageList.messageId):
			if id in oldMessages: pass
			else:
				print(nickname, content)				
				contents = str(content).split(" ")
				if contents[0][0] == "!": 
					if contents[0][1:].lower() == "save":
						nazvan = sub_clients.get_chat_thread(chatId=chat).title
						opisan = sub_clients.get_chat_thread(chatId=chat).content
						fonsss = sub_clients.get_chat_thread(chatId=chat).backgroundImage
						ucon = sub_clients.get_chat_thread(chatId=chat).icon
						sub_clients.send_message(message='Ваши данные сохранены!', chatId=chat)	
					if contents[0][1:].lower() == "res":
						sub_clients.edit_chat(chatId=chat, title=str(nazvan), content=str(opisan))
						try:
							sub_clients.edit_chat(chatId=chat, backgroundImage=str(fonsss))
							sub_clients.edit_chat(chatId=chat, icon=str(ucon))
						except:
							sub_clients.send_message(message='Приват восстановлен!', chatId=chat)
					if contents[0][1:].lower() == "inf":
						sub_clients.send_message(message='1) !save - сохранение чата. 2)!res - восстановление чата 3)!inf - информация.', chatId=chat)	
				oldMessages.append(id)
