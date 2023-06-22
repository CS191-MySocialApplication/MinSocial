<script>
    import Header from "../components/Header.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte";
    import NavbarMobile from "../components/NavbarMobile.svelte";
    import Message from '../components/Message.svelte';

    import Messageform from "../components/MsgForm.svelte";

    import {link, replace} from 'svelte-spa-router';
    import { lastPageAccessed } from "./store.ts";

    export let params = {};
    
    
    import { getMsg } from "../sdk/message"

    import my_store from "../sdk/store.ts";
    my_store.update(n => params.tid)

    // console.log(params.tid)

    let auth_promise = getMsg(params);

    function onFormSubmit(e){
        replace("/messages")
    }

  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop lastPageAccessed={$lastPageAccessed}/>
  
    <div class="content">
      <Header title="Conversation"/>
      <main>
        {#await auth_promise}
          <p>waiting...</p>
        {:then response }
          {@const usernames = response[Object.entries(response).length-1]}
          <div id="messageThread">
          {#each response as status, index}
            {#if Object.entries(response).length-1 != index}
              {#if usernames.includes(status["account"]["username"]) }
                <!--Message from other user-->
                <div id="leftAlignment">
                  <div id="otherMessageArea">
                    <div id="otherMessage">
                      <Message status={status}/>
                    </div>
                  </div>
                  <span id="dateTime">{status["created_at"]}</span>
                </div>
              {:else}
                <!--Message from user-->
                <div id="rightAlignment">
                <div id="ownMessageArea">
                  <div id="ownMessage">
                    <Message status={status}/>
                  </div>
                </div>
                <span id="dateTime">{status["created_at"]}</span>
              </div>
              {/if}
            {/if}
          {/each}
        </div>
        {:catch error}
          <p style="color: red">{error.message}</p>
        {/await}
        <!--to turn into a Messageform-->
      </main>
      <Messageform on:postSubmit={onFormSubmit}/>
    </div>
  
    <NavbarMobile lastPageAccessed={$lastPageAccessed}/>
  </div>
  
  <style>
    main {
      margin-top: 70px;
      margin-bottom: 70px;
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
    
    #otherMessageArea {
      display: flex;
      justify-content: left;
      width: 100%;
    }
    #ownMessageArea {
      display: flex;
      justify-content: right;
      width: 100%;
    }
    

    #leftAlignment {
      text-align: left;
      margin-bottom:14px;
    }

    #rightAlignment {
      text-align: right;
      margin-bottom:14px;
    }
    
    #otherMessage {
      background-color: #3c4444;
      border-radius: 15px;
      max-width: 50%;
    }

    #ownMessage {
      background-color: #36676c;
      border-radius: 15px;
      max-width: 50%;
    }
  </style>
  
