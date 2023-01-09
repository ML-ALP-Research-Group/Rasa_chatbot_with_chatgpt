# Rasa with chatGPT

## Purpose

The purpose of this repository is to give an example of integrating [Rasa](https://github.com/RasaHQ/rasa) with [chatGPT](https://openai.com/blog/chatgpt/).


### Environment 

- Thw work has been tested with `Ubuntu 20.4` and `python 3.8`

## Installation

- Clone the repository:

```bash
git clone https://github.com/PAIN-BARHAM/Rasa_chatbot_with_chatgpt.git
```

- Open the repository folder or you can use the following:

```bash
cd Rasa_chatbot_with_chatgpt/
```


- Change the permission of `installation_file.sh` by run this command in the repository directory:

```bash
chmod +x installation_file.sh
```

- Run the first bash script by the following command:

```bash
./installation_file.sh
```

Run this on the bash to activate the venv:

```bash
source .env/bin/activate
```

- Change the permission of `installation_file_after.sh` by run this command in the repo directory:

```bash
chmod +x installation_file_after.sh
```

- Run the second bash script by the following command:

```bash
./installation_file_after.sh
```

- Add the config.json file as described on this [guide](https://github.com/acheong08/ChatGPT/wiki/Setup).

* You can add on the current working directory or on the home directory under user name. Example: /home/think3/.config/revChatGPT/config.json

- Move to the chatbot's directory by the following command: 

```bash
cd rasa_chatbot_folder
```

- Train your rasa chatbot by:

```bash
rasa train
```

- Run your chatbot in the command line by:

```bash
rasa shell
```

- Run rasa action server on a new bash on the chatbot directory(Make sure you are still on the venv `source .env/bin/activate`):

```bash
rasa run actions
```

- Wait, a web window will appear and allow you to log in to your chatGPT account. After login successfuly, you will be able to use chatGPT for the chatbot responces.

- Enjoy the conversation...


## Contributors

- [Muhammad Al-Barham](https://github.com/PAIN-BARHAM)
- [Jovana Markovska](https://github.com/JovanaMarkovska)
- [Prof. Ashraf Elnagar](https://github.com/elnagara)