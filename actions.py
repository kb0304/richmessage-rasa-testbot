# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

attachmentDict = {
  "text button with url": [{
      "title": "text button with url",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        }
      ]
    }],
  "text button with msg in chat window":[{
      "title": "text button with msg in chat window",
      "actions": [
        {
          "type": "button",
          "text": "Say hello in chat window?",
          "msg": "hello in chat window",
          "msg_in_chat_window": True
        }
      ]
    }],
  "image button with url":[{
      "title": "image button with url",
      "actions": [
        {
          "type": "button",
          "url": "http://www.kayak.com",
          "image_url": "http://www.emoji.co.uk/files/phantom-open-emojis/travel-places-phantom/12698-airplane.png",
          "is_webview": False
        }
      ]
    }],
  "image button with msg in chat window":[{
      "title": "image button with msg in chat window",
      "actions": [
        {
          "type": "button",
          "image_url": "http://www.emoji.co.uk/files/phantom-open-emojis/travel-places-phantom/12698-airplane.png",
          "msg": "I clicked the airplane",
          "msg_in_chat_window": True
        }
      ]
    }],
  "multiple text buttons":[{
      "title": "multiple text buttons with url",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://requests.example.com/cancel/r123456",
          "is_webview": False
        }
      ]
    }],
  "horizontal text buttons":[{
      "title": "horizontal text buttons with url",
      "button_alignment": "horizontal",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "http://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://requests.example.com/cancel/r123456",
          "is_webview": False
        }
      ]
    }],
  "attachment with buttons":[{
      "title": "Lauri M(title field)",
      "title_link": "https://www.basketball-reference.com/players/m/markkla01.html",
      "text": "Should have been rookie of the year (text field)",
      "description": "What a great player! (description field)",
      "image_url": "http://www.trbimg.com/img-5b04c449/turbine/ct-spt-bulls-lauri-markkanen-all-rookie-team-20180522",
      "actions": [
        {
          "type": "button",
          "text": "Book flights",
          "url": "https://www.kayak.com",
          "is_webview": False
        },
        {
          "type": "button",
          "text": "Cancel travel request",
          "url": "https://www.kayak.com",
          "is_webview": False
        }
      ]
    }]
};

replyDict = {
  "hello in chat window": "received your ‘hello in chat window’",
  "I clicked the airplane": "received your response about clicking the airplane"
}

class ActionRichmessage(Action):
    def name(self):
        return "action_richmessage"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message['text']
        if (text in attachmentDict):
            dispatcher.utter_custom_message(*attachmentDict[text])
        elif (text in replyDict):
            dispatcher.utter_message(replyDict[text])
        return []
