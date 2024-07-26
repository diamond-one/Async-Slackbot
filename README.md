
# Asynchronous Standup Meeting Bot for Slack

This script automates asynchronous standup meetings on Slack by communicating with users based on predefined questions for specific weekdays and collects their responses.

## Current Status
- Functionality: All features are working and was running (manually triggered) in the studio for eight months
- Development: Currently stopped to focus on other projects

## Features
- **Privatly messages users, then posts replies in a public status channel**
- **Day Specific Questions**: Specific to Monday, Wednesday, and Friday.
- **Dynamic Reply Handling**: Understands user replies' context.
- **Error Handling**: Logs unsuccessful message sends.
- **User Profile Integration**: Retrieves user's profile image when publishing their responses.

## Future Direction 
- Create a UI for editing users, schedules and messages
- Create a date/time trigger so the bot does not need to be run manually on scheduled days
- Have bot run headlessly so that no interaction or ide needs to be running for bot to run

## Prerequisites

1. A Slack workspace and permissions to create apps.
2. Python environment.

## Slack API Setup

1. Go to [Slack API](https://api.slack.com/) and create a new app.
2. Add necessary permissions like `chat:write`, `users:read`, and any others that you might need.
3. Install the app to your workspace. This should provide you with both `SLACK_APP_TOKEN` and `SLACK_BOT_TOKEN`.

## Configuration

Your configuration (`config.py`) should include:

- `target_users`: A dictionary containing user IDs for your main team.
- `dev_users`: A dictionary for development/testing.
- `config`: A dictionary with `SLACK_APP_TOKEN`, `SLACK_BOT_TOKEN`, `dev_CHANNEL_ID`, and `target_CHANNEL_ID`.

## Dependencies

```bash
pip install slack_bolt datetime
```

## Usage

### Testing

Ensure you're in testing mode:

```python
SLACK_CHANNEL_ID = config.get("dev_CHANNEL_ID")
SLACK_USER_IDS = dev_users.values()
```

### Production

Switch to production by commenting out testing configurations and uncommenting:

```python
# SLACK_CHANNEL_ID = config.get("target_CHANNEL_ID")
# SLACK_USER_IDS = target_users.values()
```

Run the script:

```bash
python your_script_name.py
```

## Functions Overview

- `todays_question()`: Returns today's question.
- `todays_reply()`: Returns today's reply format.
- `send_message_to_users(question)`: Sends out the day's question.
- `listen_for_replies(question)`: Listens for user replies.
- `publish_answer(user_id, reply_msg)`: Formats and publishes user answers.

## Caution

Always ensure you're using the right channel IDs (`dev_CHANNEL_ID` for testing and `target_CHANNEL_ID` for production) to prevent unintended team-wide messages.
