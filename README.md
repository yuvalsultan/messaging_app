# Messaging App 

This messaging app is a restful application that allows people sending and receiving messages to one another.
![image](https://user-images.githubusercontent.com/46243822/156650802-33238219-d3a4-4f51-b822-6efcc7001963.png)

## Installation

1. Clone the reop
```bash
git clone git@github.com:yuvalsultan/messaging_app.git
```
2. Install requirements.txt
```bash
pip install -r requirements.txt
```


## Usage

The application works through post and get commands.
Post request should include a messae, sender and recipient, like the following:
{
    "msg": "wuzup",
    "sender": "Yuval",
    "recipient":"Dana"
}
Get request should include the recipient alone.
{
    "recipient":"Dana"
}
the output is a list of messages sent to this certain recipient. 
The mesages are displayed on the localhost webpage.

