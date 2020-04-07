# Zoom API

Python wrapper around the [Zoom.us](http://zoom.us) REST API v2. Source code available at https://github.com/Git-Good-Team/zoomapi.

This work is based on [Zoomus](https://github.com/actmd/zoomus) and [zoomapi](https://github.com/crista/zoomapi).

## Bot Commands

Execute botm1.py to get started. Available commands are:

### stop

Exits program

### create channel

Creates a channel. User needs to provide a channel name and what type of channel is to be created.

### lists channels

Lists all channels the user is part of.

### get channel

Retrives channel information. User must provide channel id.

### list channel members

List all members that belong to a specific channel. User must provide channel id.

### delete channel

Deletes a specific channel. User must provide channel id.

### update channel

Updates a specific channel. User must provide channel id.

### join channel

Joins a specific channel. User must provide channel id.

### invite channel members

Invites Zoom users to a specific channel. User must provide channel id and a list of user emails.

### remove channel member

Removes users to a specific channel. User must provide channel id and a member id.

### leave channel

Active user leaves a channel that he belongs to. User must provide channel id.

### list messages

User lists all messages from a specific user that were sent in private messages or in a channel. User must provide user id, channel id or contact email.

### send message

Sends a message to a contact or channel. User must provide the message to be sent and channel id or contact email.

### update message

Updates an existing message. User must provide message id and contact email or channel id.

### delete message

Deletes an existing message. User must provide message id and contact email or channel id.

### Other commands

Any other command will be treated as an invalid command.

