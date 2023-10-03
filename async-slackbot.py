# Import necessary libraries and configurations
from config import target_users, dev_users, config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import datetime

# Retrieve Slack tokens from the configuration
SLACK_APP_TOKEN = config.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = config.get("SLACK_BOT_TOKEN")

# Define questions and replies for each day of the week for regular sprints
questions = {
    "Monday": "What do you plan to do this week?",
    "Wednesday": "What progress have you made on your tasks?",
    "Friday": "What did you achieve this week?"
}

reply_dic = {
    "Monday": "*This week I plan to:*",
    "Wednesday": "*Progress so far on my tasks:*",
    "Friday": "*This week I:*"
}

# Define the Slack channel and user IDs
SLACK_CHANNEL_ID = config.get("dev_CHANNEL_ID") # Test Channel, comment this out when you are done testing
# SLACK_CHANNEL_ID = config.get("target_CHANNEL_ID") # Uncomment when you want to send to your non-test channel

SLACK_USER_IDS = dev_users.values()  # Test Channel, comment this out when you are done testing
# SLACK_USER_IDS = target_users.values() # Uncomment when you want to send to your non-test channel

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)
answers = {}

# Function to get the question for the current day
def todays_question():
    today = datetime.datetime.today().strftime("%A")
    return questions.get(today, "")

# Function to get the reply format for the current day
def todays_reply():
    today = datetime.datetime.today().strftime("%A")
    return reply_dic.get(today, "")

# Function to send messages to users
def send_message_to_users(question):
    for user_id in SLACK_USER_IDS:
        try:
            answers[user_id] = []
            app.client.chat_postMessage(
                channel=user_id,
                text=f"Hola! It's time for our *Asynchronous Standup meeting*. \nWhen you are ready, please answer the following questions: \n\n {question}"
            )
            print("success >> " + user_id)
        except:
            print("fail >> " + user_id)

# Function to listen for replies from users
def listen_for_replies(question):
    @app.event("message")
    def handle_mention(event, say):
        if event["user"] in SLACK_USER_IDS:
            user_id = event["user"]
            response = app.client.conversations_history(channel=event["channel"])["messages"]
            last_msg = response[0]
            before_last_msg = response[1]

            if before_last_msg['text'] == f"Hola! It's time for our *Asynchronous Standup meeting*. \nWhen you are ready, please answer the following questions: \n\n {question}":
                answers[user_id].append(last_msg['text'])
                say(channel=user_id, text="Any blockers you need help with?")

            elif before_last_msg['text'] == "Any blockers you need help with?":
                answers[user_id].append(last_msg['text'])
                answer, attachments = publish_answer(user_id, todays_reply())
                app.client.chat_postMessage(channel=SLACK_CHANNEL_ID, as_user=True, text=f"*<@{user_id}>:* {answer}")

# Function to format and publish the answer
def publish_answer(user_id, reply_msg):
    _user_answers = answers[user_id]
    answer = f"\n{reply_msg}\n {_user_answers[0]}\n"
    answer += f"\n*Blockers:*\n {_user_answers[1]}\n"
    user_info = app.client.users_info(user=user_id)["user"]
    user_image_url = user_info["profile"]["image_48"]
    attachments = [{"fallback": "User profile image", "image_url": user_image_url}]
    return answer, attachments

# Main execution
if __name__ == "__main__":
    handler = SocketModeHandler(app_token=SLACK_APP_TOKEN, app=app)
    question_for_today = todays_question()
    send_message_to_users(question_for_today)
    listen_for_replies(question_for_today)
    handler.start()
