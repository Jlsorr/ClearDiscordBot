
# Discord ClearAll Bot

This bot allows administrators to clear all messages in a specific Discord channel using the `!clearall` command. It also sends a confirmation message, which automatically deletes after 5 seconds.

## Features
- Command: `!clearall` – Deletes all messages in the current channel.
- Only users with administrator permissions can execute the command.

## Requirements
- Python 3.8+
- `discord.py` library

## Installation
1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install discord.py
   ```
3. Replace `'TOKEN'` in the source code with your bot's token.

## Usage
1. Run the bot using the following command:
   ```bash
   python bot.py
   ```
2. In any channel where the bot has permissions, use `!clearall` to delete all messages.

## Permissions
Ensure the bot has the following permissions in the server:
- Manage Messages
- Send Messages

## License
This project is open-source. Feel free to modify and distribute it as needed.

### Example

```bash
!clearall
```
