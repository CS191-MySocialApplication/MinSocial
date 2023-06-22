<script>
  import Header from "../components/Header.svelte";
  import Messageformv2 from "../components/Messageformv2.svelte";
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
      // console.log("message");
      // console.log(message);
      if(message["participantIDs"].length !== 0){
        if(!(message["participantIDs"][0]["username"] in conversationsDict)) {
          // console.log("new user");
          // console.log(message["participantIDs"][0]["username"]);
          conversationsDict[message["participantIDs"][0]["username"]] = [message];
        }   
        else {
          conversationsDict[message["participantIDs"][0]["username"]].push(message);
        }
      }
    }
    // console.log("convesationsDict");
    // console.log(conversationsDict);
    
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
      <Messageformv2/>
      {#await test}
        <p>waiting...</p>
      {:then conversationsDict}
      
        {#each Object.entries(conversationsDict) as [user, value]}
        
        <!--Displays all messages-->  
        <div id="user">
          <p class="imptDetails">Conversations with {user} </p>
          <div id="conversationContainer">
          {#each Object.entries(value) as [key,message]}
          <!--{console.log("message test")}
              {console.log(message)}-->
            
          <a class="conversation" href="/#/msg/{message["conversationID"]}/{message["messageID"]}">
      
            {#if message["unread"]==true}
            <div class="messageDetails readDetails">
              <p id="username">{message["author"]["username"]} messaged <span class="dateTime">| {message["createdTime"]}</span></p>
            </div>
            
              <div id="unreadContent">
                {#if message["statusDict"]["sensitive"]}
                  <p>{message["statusDict"]["spoiler_text"]}&ensp;&bull;&ensp;<span style="font-size: 12px">Hidden Content</span> </p>
                {:else}
                  {#if message["statusDict"]["media_attachments"].length != 0}
                    <div id="messagePreview">
                    <p id="htmlContent">{@html message["content"]}</p>
                    <p>&ensp;&bull;&ensp;<span style="font-size: 12px">Media</span> </p>
                    </div>
                  {:else if message["statusDict"]["poll"]!= null}
                    <div id="messagePreview">
                      <p id="htmlContent">{@html message["content"]}</p>
                      <p>&ensp;&bull;&ensp;<span style="font-size: 12px">Poll</span> </p>
                    </div>
                  {:else}
                  <p id="htmlContent">{@html message["content"]}
                  {/if}
                {/if}
              </div>

            {:else}
            <div class="messageDetails unreadDetails">
              <p id="username">{message["author"]["username"]} messaged <span class="dateTime">| {message["createdTime"]}</span></p>
            </div>

            <div id="readContent">
              {#if message["statusDict"]["sensitive"]}
                <p>{message["statusDict"]["spoiler_text"]}&ensp;&bull;&ensp;<span style="font-size: 12px">Hidden Content</span></p>
              {:else}
              {#if message["statusDict"]["media_attachments"].length != 0}
                <div id="messagePreview">
                  <p id="htmlContent">{@html message["content"]}</p>
                  <p>&ensp;&bull;&ensp;<span style="font-size: 12px">Media</span> </p>
                  </div>
              {:else if message["statusDict"]["poll"]!= null}
                <div id="messagePreview">
                  <p id="htmlContent">{@html message["content"]}</p>
                  <p>&ensp;&bull;&ensp;<span style="font-size: 12px">Poll</span> </p>
                </div>
              {:else}
              <p id="htmlContent">{@html message["content"]}
              {/if}
              {/if}           
            </div>
            {/if}                        
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
  
  <NavbarMobile lastPageAccessed={$lastPageAccessed}/>
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
  .dateTime {
    font-size: 12px;
  }
  .messageDetails.readDetails {
    color: white;
  }
  .messageDetails.unreadDetails {
    color: #acacac;
    font-weight: normal;
    letter-spacing: normal;
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

  #unreadContent {
    font-size: 14px;
    color: white;
    font-weight: 600;
  }

  #readContent {
    font-size: 14px;
    color: #acacac;
  }

  #htmlContent {
      pointer-events: none;
      margin: 0px;
    }

  #messagePreview {
    display: flex;
  }
</style>