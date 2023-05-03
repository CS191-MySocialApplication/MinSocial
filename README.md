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

1. Access the Mastodon Developer Portal.

#### Linking the Application with Twitter

1. Access the <a href="https://developer.twitter.com/en/portal/dashboard">Twitter Developer Portal </a>. Note that you might need to sign up first before proceeding to the next step.
2. Create a project then add an app.
3. Set up app environment to development.
4. Press next.
5. In the User authentication settings, press set up.
6. Set App permissions to Read and write and Direct Message.
7. Set Type of App to Native App.
8. Set callback URL to http://127.0.0.1:5000/callback/mstdn.
9. Set website URL to anything.
10. Copy the Client ID and paste it into client_id.json.
  
### Installing application dependencies

#### Install back-end dependencies

We recommend using a python virtual environment for this.

After setting up the virtual environment, enter the command <code>pip install -r requirements.txt</code> on the root directory.

#### Install front-end dependences

After doing this, open up a second terminal (on the same directory) and <code>cd</code> into <code>/client</code>. Then enter the following:

1. <code>npm i</code>
2. <code>npm i @fontsource/open-sans</code> (to install the fonts used)
3. <code>npm run build</code>

### Running the server

Go back to the first terminal (root directory) and enter <code>flask --app minsocial run</code>
