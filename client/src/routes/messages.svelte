<script>
  import Header from "../components/Header.svelte";
  import Messageform from "../components/Messageform.svelte";
  import NavbarDesktop from "../components/NavbarDesktop.svelte";
  import NavbarMobile from "../components/NavbarMobile.svelte";

  import { getMessageContent } from "../sdk/conversations";
  import { lastPageAccessed } from "./store.ts";

  let pageTitle = "Messages"
  let auth_promise = getMessageContent();
  
  async function isolateConversations() {
    let listOfMessages = await auth_promise;
    let conversationsDict = {};
    for(let message of listOfMessages) {
      console.log("message");
      console.log(message);
      if(!(message["participantIDs"][0]["username"] in conversationsDict)) {
        console.log("new user");
        console.log(message["participantIDs"][0]["username"]);
        conversationsDict[message["participantIDs"][0]["username"]] = [message];
      }   
      else {
        conversationsDict[message["participantIDs"][0]["username"]].push(message);
      }
    }
    console.log("convesationsDict");
    console.log(conversationsDict);
    
    return conversationsDict;
    
  
  }

  let test = isolateConversations();
  
  /*isolateConversations().then(function(){
    console.log(listOfMessages);
    
  });

  console.log(conversationsDict);*/
</script>

<div class="desktopFormat">
  <NavbarDesktop lastPageAccessed={$lastPageAccessed}/>

  <div class="content">
    <Header title={pageTitle}/>
    <main on:load|once={lastPageAccessed.update( n => "/#/messages")}>
  
      {#await test}
        <p>waiting...</p>
      {:then conversationsDict}
      
        {#each Object.entries(conversationsDict) as [user, value]}
        
        <!--Displays all messages-->  
        <div id="user">
          <p class="imptDetails">Conversations with {user} </p>
          <div id="conversationContainer">
          {#each Object.entries(value) as [key,message]}
            
          <a class="conversation" href="/#/msg/{message["messageID"]}">
            <div class="messageDetails">
                <p id="username">{message["author"]["username"]} messaged <span id="dateTime">| {message["createdTime"]}</span></p>
                <!--<p id="timeSent"><span id="dateTime">{message["createdTime"]}</span></p>-->    
            </div>
            <p id="content">{@html message["content"]}</p>
          </a>
          
          {/each}
        </div>
        </div>
      {/each}
      
      {:catch error}
        <p style="color: red">{error.messages}</p>
      {/await}
    </main>
  </div>
  
  <NavbarMobile title={pageTitle}/>
</div>

<style>
    main {
    margin-top: 70px;
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 2rem;
    width: 100%;
    box-sizing: border-box;
  }

  @media screen and (hover: none) {
    .desktopFormat {
      display: flex;
      flex-direction: column;
      align-items: stretch;
      margin: 0;
    }
  }

  @media screen and (hover: hover) {
    .desktopFormat {
      display: flex;
      flex-direction: row;
      margin: 0;
    }
    .content {
      display: flex;
      flex-direction: column;
      margin-left: 11.5%;
      width: 100%;
    }
  }

  a {
    display: block;
    text-decoration: none;
    color: inherit;
    padding: 0px 14px 1px 14px;
    
    border-radius: 5px;
    background-color: #3c4444; /*#252c2c;*/
    
  }

  #user {
    display: block;
    text-decoration: none;
    color: inherit;
    /*
    border-style: none none solid none;
    border-color: #50c0cb;
    border-width: 1px;
    */
    padding: 0px 14px;
  }
  a:hover {
    background-color: #252c2c;
  }
  
  .messageDetails {
    font-weight: bold;
    letter-spacing: 0.5px;
    font-size: 14px;
    display: flex;
    justify-content: space-between;

  }

  #conversationContainer {
    border-radius: 15px;
    background-color:#3c4444;
    margin: 14px 0px;
    padding: 14px;

  }
  
  #username {
    margin-bottom: 0px;
  }

  #content {
    font-size: 14px;
    color: #acacac;
  }
</style>