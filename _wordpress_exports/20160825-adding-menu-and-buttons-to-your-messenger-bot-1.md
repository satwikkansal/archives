title: Adding  Menu and Buttons to your messenger bot
link: https://satwikkansal.wordpress.com/2016/08/25/adding-menu-and-buttons-to-your-messenger-bot/
author: satwikkansal
description: 
post_id: 114
created: 2016/08/25 05:52:03
created_gmt: 2016/08/25 05:52:03
comment_status: open
post_name: adding-menu-and-buttons-to-your-messenger-bot
status: publish
post_type: post

<!--How to add buttons and other visual features to messenger bot and make them work.-->

# Adding  Menu and Buttons to your messenger bot

This blog post demonstrates the process of adding buttons, message templates, and persistent menu to your messenger bot. Messenger provides plenty of handy templates to make your bot visually appealing and "app-like" rather that just a text processing and replying script (well, just my opinion, some people would prefer a truly conversational chat-bot but we're still far from achieving this with high accuracy). Let's see how to add some of the visual features to any messenger bot 

## Adding persistent menu and buttons to Your Messenger Bot

#### What is Persistent Menu?

The Persistent Menu is a menu that is always available to the user (a 3-caret icon in the bottom-left of the message box). This menu should contain important actions that users can select at any point. Having a persistent menu quickly communicates the core capabilities of your bot for first-time and returning users. 

#### How to add Persistent Menu?

The method of adding Persistent Menu is pretty straightforward. You just have to do it once. It took some time for me to figure it out, so I decided to write a blog post to save your time. The code at your webhook endpoint server has nothing to do with the menu. We can make a separate POST request to our bot with the PAGE_ACCESS_TOKEN to make this it work. Sample Request [code language="bash"] curl -X POST -H "Content-Type: application/json" -d '{ "setting_type" : "call_to_actions", "thread_state" : "existing_thread", "call_to_actions":[ { "type":"postback", "title":"Help", "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_HELP" }, { "type":"postback", "title":"Start a New Order", "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_START_ORDER" }, { "type":"web_url", "title":"View Website", "url":"http://petersapparel.parseapp.com/" } ] }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN" [/code] So basically, in the above JSON, call_to_actions contains an array of menu_item objects which are of two types: 1\. web_url 2\. postback For web_url buttons, we need to have an URL value in the JSON. This URL is opened in a mobile browser when the button is tapped. For postback buttons instead of URL, we have payloads. The payload contains data useful to that menu button. For postback buttons, this data will be sent back to you via webhook. You can have a maximum of 5 buttons in the persistent menu. So, How does Facebook determine which bot we are referring to? Its given by the value PAGE_ACCESS_TOKEN parameter in the URL to which we are making this post request. To delete the Persistent Menu send a DELETE request: [code language="bash"] curl -X DELETE -H "Content-Type: application/json" -d '{ "setting_type":"call_to_actions", "thread_state":"existing_thread" }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN" [/code]   And to update or change the Persistent Menu options, simply send another POST request. 

## Adding a "GET STARTED" Button to your messenger bot

#### What is a GET STARTED button in Messenger?

The Welcome Screen can display a Get Started button. When this button is tapped, a postback received callback is triggered along with the person's page-scoped ID (PSID). You can then present a personalized message to greet the user or present buttons to prompt him or her to take action. The process is very much similar, but here you're not allowed any 'title' attribute in the JSON. The button will always be named as 'GET STARTED'. [code language="bash"] curl -X POST -H "Content-Type: application/json" -d '{ "setting_type":"call_to_actions", "thread_state":"new_thread", "call_to_actions":[ { } ] }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"&amp;amp;amp;amp;amp;nbsp; [/code] 

## Adding Greeting Text to your messenger bot

One common way is to combine "GREETING TEXTS" with "GETTING STARTED" button. You can set a greeting for new conversations. This can be used to communicate your bot's functionality. [code language="bash"] curl -X POST -H "Content-Type: application/json" -d '{ "setting_type":"greeting", "greeting":{ "text":"Welcome to My Company!" } }' "https://graph.facebook.com/v2.6/me/thread_settings?access_token=PAGE_ACCESS_TOKEN"&amp;amp;amp;amp;amp;nbsp;&amp;amp;amp;amp;amp;nbsp; &amp;amp;amp;amp;amp;nbsp; [/code] 

## Making your messenger bot perform an action when the button is pressed?

Well, now we have the menu. Let's see how to make the buttons "do something" when invoked by the users. 

### Handling POSTBACK requests from Persistent Menu buttons in messenger

We'll have to look for the POSTBACK event in the request that we're receiving at our webhook endpoint. For example, here's how you'll handle it in python [code language="python"] @app.route('/', methods=['POST']) def webook(): # endpoint for processing incoming messaging events data = request.get_json() log(data)&nbsp; # you may not want to log every incoming message in production, but it's good for testing if data["object"] == "page": for entry in data["entry"]: for messaging_event in entry["messaging"]: if messaging_event.get("postback"): # user clicked/tapped "postback" button in earlier message message_text = messaging_event["postback"]["payload"] # the button's payload log("Inside postback") message_text = message_text.lower() sender_id = messaging_event["sender"]["id"] if (message_text == "SOME_PAYLOAD_WE_DEFINED"): send_message(sender_id, "Yay! This button works!") [/code] So basically, in request JSON, we look for [code language="python"] request["object"]["page"]["entry"]["messaging"]["postback"] [/code] If it exists, then a button has been tapped, and then we can handle it whatever way we want to. All of the above POST requests I covered are one-time requests, i.e., you don't need to send them over and over again. But for interactive buttons in the messages, you'll have to dynamically generate similar POST request depending on the user's input from your webhook endpoint (You'll have to handle this on your server). Similar to buttons there are predefined templates provided by Facebook like 'Generic Template,' 'Receipt Template,' 'Airline Template,' etc. For more details, It'd be easier for you to now check out and follow along Facebook's documentation for [Send API](https://developers.facebook.com/docs/messenger-platform/send-api-reference) in messenger for all the available choices and all the customization that you can do with the templates. PS: I'm currently working on developing a Python-SDK for messenger platform that would simplify the development process of messenger bots to a great extent. If you'd like to collaborate or have any ideas, please ping me.

## Comments

**[Suhel Dhuldhule](#6 "2017-02-20 07:27:02"):** Where Do Hav To I Add This ? I am Using API.AI & I Dont Know How To And Where To Add This

**[satwikkansal](#7 "2017-02-20 08:25:57"):** Assuming you are trying to add a Get Started button, You just need to get your PAGE_ACCESS_TOKEN from the developer settings of your bot and then make CURL request.

**[Suhel Dhuldhule](#8 "2017-02-20 08:27:50"):** How ?

**[satwikkansal](#9 "2017-02-20 08:28:16"):** You can refer to this question on API.ai forums https://discuss.api.ai/t/how-to-trigger-any-intent-when-user-click-on-get-started-button-in-facebook-messenger/1534/2

