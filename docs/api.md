# API

To allow the app to be cached into the client device, we made sure that the web-app is mostly did client-side rendering. This meant that we have to create a REST-API endpoints to serve user data.

## Endpoints

### `mentions_timeline.py`

#### `/api/home` `[GET]`

Provide the user their mentions timeline.

Returns a list of `Status` data model.

### `conversations_list.py`

#### `/api/messages` `[GET]`

Provide the user conversations that they are a participant in.

Shows the latest message.

Returns a list of `Message`.

### `conversation.py`

#### `/api/messages/mstdn/<conversation_id>` `[GET]`

Provide the user the messages in a Mastodon DM.

Returns a list of `Status`.

### `status.py`

#### `/api/toot/<toot_id>` `[GET]`

Provide the user the Mastodon status of the corresponding `toot_id`.

Returns a `Status`.

### `context.py`

#### `/api/toot/<toot_id>/context` `[GET]`

Provide the user the ancestors of the Mastodon status with `toot_id`

Returns a list of `Status`.

### `compose.py`

#### `/api/compose` `[POST]`

Compose a Status to be posted on social medias accounts that are currently logged in.

Expects:
- `text`: `String`

Returns `Status: Success` if post is successful and `Status: Fail` if post is unsuccessful.