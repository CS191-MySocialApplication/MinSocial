# Linking the Application with Twitter
1. Access the <a href="https://developer.twitter.com/en/portal/dashboard">Twitter Developer Portal </a>. Note that you might need to sign up first before proceeding to the next step.
2. Create a project then add an app.
3. Set up app environment to development.
4. Press next.
5. In the User authentication settings, press set up.
6. Set App permissions to Read and write and Direct Message.
7. Set Type of App to Native App.
8. Set callback URL to http://127.0.0.1:5000/logged.
9. Set website URL to anything.
10. Copy the Client ID and paste it into client_id.json.

# Running the Application
We recommend using a python virtual environment for this. 

After setting up the virtual environment, enter the command <code>pip install -r requirements.txt</code> on the root directory.

After doing this, open up a second terminal (on the same directory) and <code>cd</code> into <code>/client</code>. Then enter the following:
1. <code>npm i</code>
2. <code>npm i @fontsource/open-sans</code> (to install the fonts used)
3. <code>npm run build</code>

Go back to the first terminal (root directory) and enter <code>flask --app minsocial run</code>
