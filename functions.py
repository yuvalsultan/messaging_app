
stock = {

}


def add_msg_to_stock(stock, sender, recipient, msg):
    if recipient in stock.keys():
        if sender in stock[recipient].keys():
            stock[recipient][sender].append(msg)
        else:
            stock[recipient][sender] = [msg]
    else:
        new_chat = {sender: [msg]}
        stock[recipient] = new_chat
    print(stock)


def get_msg(stock, recipient):
    messages = []
    if recipient in stock.keys():
        recipient_chat = stock[recipient]
        for sender in recipient_chat.keys():
            for msg in recipient_chat[sender]:
                messages.append("{0}: {1}".format(sender, msg))
        return messages
    else:
        return ["There aren't any messages for {0}".format(recipient)]


if __name__ == "__main__":
    stock = {
        "Dana": {
            "Yuval": ["Hey Dana", "How are you?", "Are you coming today?"],
            "Shlomi": ["Hey this is Shlomi"]
        },
        "Yuval": {
            "Dana": ["Yuval I love you", "Please talk to me soon"],

        }
    }
    print(get_msg(stock,"Dana"))
