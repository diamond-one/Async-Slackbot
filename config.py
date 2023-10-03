
# Use this dev_users group to target a test channel in slack, use your user ID and a failing ID (already entered) to check 
# if failed sends are displayed in your terminal when you run the code
# a successful test should message your user in private and show in the terminal:

# success >> "YOUR USER ID HERE"
# fail >> XXX999XXX999
# Bolt app is running!



dev_users = {
                "User_ID": "YOUR USER ID HERE", 
                "Failing_ID": "XXX999XXX999"
}


# Here enter you SLACK_BOT_TOKEN and SLACK_APP_TOKEN as well as the channel IDs you want to send messages to
config= {
            "SLACK_BOT_TOKEN": "ENTER YOUR SLACK BOT TOKEN HERE : IT STARTS WITH xoxb",
            "SLACK_APP_TOKEN": "ENTER YOUR SLACK APP TOKEN HERE : IT STARTS WITH xapp",
            "dev_CHANNEL_ID": "ENTER YOU TEST CHANNEL ID HERE",
            "target_CHANNEL_ID": "ENTER YOUR TARGET CHANNEL TO SEND ASYNC MSGS HERE",

}

target_users = {
            # "Username": "User ID",      ## Format Example, user ID is found by clicking on each users profile in slack
            "Username": "00000000000",
            "Username": "00000000000",
            "Username": "00000000000",
            "Username": "00000000000",
            "Username": "00000000000",



}