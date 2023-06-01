<script>
  import Header from "../components/Header.svelte";
  //import Postform from "../components/Postform.svelte";
  import NavbarDesktop from "../components/NavbarDesktop.svelte";
  import NavbarMobile from "../components/NavbarMobile.svelte";

  import { getMessageContent } from "../sdk/conversations";

  let auth_promise = getMessageContent();
  
  async function isolateConversations() {
    let listOfMessages = await getMessageContent();
    let conversationsDict = {};
    for(let message of listOfMessages) {
      //console.log(message);
      if(!(message["participantIDs"][0]["username"] in conversationsDict)) {
        console.log("new user");
        console.log(message["participantIDs"][0]);
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
  <NavbarDesktop title="Messages"/>
  
  <div class="content">
    <Header title="Messages"/>
    <main>
      <!--
      {#await auth_promise}
        <p>waiting...</p>
      {:then conversations}
        {#each conversations as conversation}
          <a class="conversation" href="/messages">
            <p class="imptDetails">Conversation with {conversation["participantIDs"][0]["username"]} <span id="dateTime">| {conversation["createdTime"]}</span></p>
            <div class="message">
              <p>{conversation["author"]["username"]}:&nbsp</p>
              {@html conversation["content"]}
            </div>
          </a>
        {/each}
      {:catch error}
        <p style="color: red">{error.messages}</p>
      {/await}
      -->
      {#await test}
        <p>waiting...</p>
      {:then conversationsDict}
        {#each Object.entries(conversationsDict) as [key, value]}
        <!--Displays latest message-->
        <!--
        <a class="conversation" href="/messages">
          <p class="imptDetails">{key} <span id="dateTime">| {value[0]["createdTime"]}</span></p>
          
            
          <div class="message">
            <p>{value[0]["author"]["username"]}:&nbsp</p>
            {@html value[0]["content"]}
          </div>

        </a>
        -->
        <!--Displays all messages-->  
        <a class="conversation" href="/#/messages">
          <p class="imptDetails">{key} <span id="dateTime">| {value[0]["createdTime"]}</span></p>
          {#each value as message}
            <div class="message">
              <p>{message["author"]["username"]}:&nbsp</p>
              {@html message["content"]}
            </div>
            
          {/each}
        </a>
        {/each}
      {:catch error}
        <p style="color: red">{error.messages}</p>
      {/await}
    </main>
  </div>

  <NavbarMobile title="Messages"/>
</div>

<style>
    main {
    margin-top: 90px;
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
    border-style: none none solid none;
    border-color: #50c0cb;
    border-width: 1px;
    padding: 0px 14px;
  }
  a:hover {
    background-color: #3c4444;
    fill-opacity: 0.5;
  }
  .imptDetails {
    margin-bottom: 0;
  }
  
  .message {
    color: #acacac;
    display: flex;
  }
  
</style>