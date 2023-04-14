# Data Models

Data models aid in the standardization of the different types of data used in the web-app, making their utilization neater and coherent. 


## Data Model Types

### Status

#### `status.py`

An *abstract data type* that represents the "posts" made on the specified platforms. In particular, there are 2 child classes:


##### `Tweet`

A class representing a post sourced from *Twitter*. Has the attributes `id`, `author_id`, `created_at`, and `text`.

Is displayed in the form of a `dictionary`

##### `Toot`

A class representing a post sourced from *Mastodon*. Has the attributes `id`, `account`, `created_at`, and `content`.

Is displayed in the form of a `dictionary`



### Message

#### `message.py`

An *abstract data type* that represents the messages sent on the specified platforms. In particular, there are 2 child classes:


##### `TwtMsg`

A class representing a message sourced from *Twitter*. Has the attributes `id`, `text`, `user`, `dm_conversation_id`, and `created_at`.

Is displayed in the form of a `dictionary`

##### `MstdnMsg`

A class representing a message sourced from *Mastodon*. Has the attributes `id`, `content`, `account`, `conversationID`, and `created_at`.

Is displayed in the form of a `dictionary`



### Author

#### Endpoint: `author.py`

***(Unfinished)***