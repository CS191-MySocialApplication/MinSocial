# MinSocial

> Minsocial is a minimal social media interface for Mastodon (social.up.edu) and Twitter that is aims to protect the mental health of users.

This is a capstone project for CS 191/192 (Software Engineering I & II) in the University of the Philippines - Diliman.

## Dependencies

- OS: Preferably Ubuntu
- Front-end:
	- NVM (Preferably to install latest Node.js and NPM versions)
	- Node.js 19.9.0
	- NPM 9.6.0
- Back-end:
	- Python 3

## Installation

1. Register the application
	1. Register using Mastodon
	2. Register using Twitter
2. Installing application dependencies
	1. Install back-end dependencies
	2. Install front-end dependencies
3. Running the server

### Registering the application

#### Linking the Application with Mastodon

When linking the application with Mastodon, you would have to chose a Mastodon instance with your account. Let its URL be `INSTANCE_URL`.

Place the URL of the instance in the `.env` file in the project folder in the field `mastodon_api_base_url`.

Then we proceed to set up your Mastodon Application:

1. Access the <b>Mastodon Developer Dashboard</b> at `[INSTANCE_URL]/settings/applications`. Note that you might need to sign up first before proceeding to the next step.
2. Press *`New application`*.
3. Set the name of the application
4. Add the following in the `Redirect URI` text area:
	- http://127.0.0.1:5000
	- http://YOUR_IP_ADDRESS_IN_THE_NETWORK:PORT (optional. Add this if you want to run your server in a local network. See section on this below)
5. Press `Submit`
6. Select the newly created application in the dashboard
7. Copy the `Client Key` and `Client Secret`
8. Paste the Mastodon `Client Key` and `Client Secret` to `PROJECT_FOLDER/.env`.
  
### Installing application dependencies

#### Install back-end dependencies

We recommend using a python virtual environment for this.

After setting up the virtual environment, enter the command <code>pip install -r requirements.txt</code> on the root directory.

#### Install front-end dependences

After doing this, open up a second terminal (on the same directory) then enter the following:

```
nvm install 19.9.0
cd client
npm i
npm run build
```

### Running the server

Go back to the first terminal (root directory) and enter <code>flask --app minsocial run</code>

### Running as server in a local network

To run as a server in a local network, do the following steps.

1. Find your local network IP address (seen in `ifconfig`). Let this be `YOUR_IP_ADDRESS_IN_THE_NETWORK`.
2. Add the following to the redirect URI form in the Mastodon App Dashboard: `http://YOUR_IP_ADDRESS_IN_THE_NETWORK:5000` (Also see Mastodon Installation Guide).
3. Go to the project folder and enter `flask --app minsocial run --host=0.0.0.0`