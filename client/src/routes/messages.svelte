<script>
  import Header from "../components/Header.svelte";
  //import Postform from "../components/Postform.svelte";
  import NavbarDesktop from "../components/NavbarDesktop.svelte";
  import NavbarMobile from "../components/NavbarMobile.svelte";

  import UnclickedMentions from "../../public/unclicked_mentions.png";
  import HoverUnclickedMentions from "../../public/hover_unclicked_mentions.png";
  import UnclickedReply from "../../public/unclicked_reply.png";
  import HoverUnclickedReply from "../../public/hover_unclicked_reply.png";
  import ClickedDM from "../../public/clicked_dm.png";
  import HoverClickedDM from "../../public/hover_clicked_dm.png";
  //import UnclickedSettings from "../../public/unclicked_settings.png";
  //import HoverUnclickedSettings from "../../public/hover_unclicked_settings.png";
  import Logout from "../../public/logout.png";
  import HoverLogout from "../../public/hover_logout.png";
  import MessagesHeader from "../../public/dm_header.png";
  import logo from "../../public/logo.png"
  import { push } from "svelte-spa-router";

  async function getMessageContent() {
    let res = await fetch("/api/messages");
    let text = await res.json();
    console.log(text);
    if (res.ok) {
      return text;
    } else {
      throw new Error(text);
    }
  }

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
  <NavbarDesktop
    mentions={UnclickedMentions}
    hoverMentions={HoverUnclickedMentions}
    dm={ClickedDM}
    hoverDM={HoverClickedDM}
    reply={UnclickedReply}
    hoverReply={HoverUnclickedReply}
    logout={Logout}
    hoverLogout={HoverLogout}
    logo={logo}
    class="navbar"
  />
  
  <div class="content">
    <Header title="Messages" icon={MessagesHeader} />
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
              <p>{value[0]["author"]["username"]}:&nbsp</p>
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

  <NavbarMobile
    mentions={UnclickedMentions}
    hoverMentions={HoverUnclickedMentions}
    dm={ClickedDM}
    hoverDM={HoverClickedDM}
    reply={UnclickedReply}
    hoverReply={HoverUnclickedReply}
    logout={Logout}
    hoverLogout={HoverLogout}
  />
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