# Messaging App 

This messaging app is a restful application that allows people sending and receiving messages to one another.
![image](https://user-images.githubusercontent.com/46243822/156650700-1543241a-edb2-477d-8f46-25ac60174d7a.png)


## Installation

clone the reop
```bash
git clone git@github.com:yuvalsultan/messaging_app.git
```

## Usage

The application works through post and get commands.
Post request should include a messae, sender and recipient, and look like the following:
{
    "msg": "wuzup",
    "sender": "Yuval",
    "recipient":"Dana"
}
Get request should include the recipient alone.
{
    "recipient":"Dana"
}
Output of 
