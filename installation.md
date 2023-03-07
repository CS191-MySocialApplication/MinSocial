# Twitter
1. Access the twitter developer portal (https://developer.twitter.com/en/portal/dashboard) You might need to sign up first
2. Create a project then add an app
3. Set up app environment to development
4. Press next.
5. In the User authentication settings, press set up
6. Set App permissions to Read and write and Direct Message
7. Set Type of App to Native App
8. Set callback URL to http://127.0.0.1:5000/logged
9. Set website URL to anything
10. Copy Client ID and paste it into client_id.json

# Setting up Svelte and SASS
1. Install degit via the command <code>npm install -g degit</code>
2. In the <code>minsocial/svelte</code> directory, enter the following commands: 
    A. <code>npm install</code>.
    B. <code>npm install svelte-preprocess node-sass</code>
    C. <code>npm i -D sass</code>

# Application
I recommend that you use a python virtual environment for this.
1. pip install -r requirements.txt
2. flask --app minsocial run