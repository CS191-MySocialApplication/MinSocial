<script>
    import Header from "../components/Header.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte";
    import NavbarMobile from "../components/NavbarMobile.svelte";
    import Status from '../components/Status.svelte';

    import Postform from "../components/Postform.svelte";

    import {link} from 'svelte-spa-router';
    import { lastPageAccessed } from "./store.ts";

    export let params = {};
    
    import { getStatus } from "../sdk/status"
  
    let auth_promise = getStatus(params);
  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop title="Toot" lastPageAccessed={$lastPageAccessed}/>
  
    <div class="content">
      <Header title="Toot"/>
      <main>
        {#await auth_promise}
          <p>waiting...</p>
        {:then response }
          {#each response as status , index}
            {#if Object.entries(response).length-1 != index}
            {#if Object.entries(response).length-2 == index}

              {#if index == 0}
                <div id="parent">
                  <Status status={status}/>
                </div>
              {:else}
                <div id="status">
                  <div id="line"></div>   
                  <Status status={status} id="reply"/>    
                </div>
              {/if}
            {:else}
              {#if index == 0}
                <div id="parent" 
                style="border-style: none none solid none;
                border-color: #50c0cb;
                border-width: 1px;">
                  <Status status={status}/>
                </div>
              {:else}
                <div id="status"
                style="border-style: none none solid none;
                border-color: #acacac;
                border-width: 1px;">
                  <div id="line"></div>   
                  <Status status={status} id="reply"/>    
                </div>
              {/if}
            {/if}
            {/if}
          {/each}
        {:catch error}
          <p style="color: red">{error.message}</p>
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

    #line{
      margin: 14px 0px 14px 14px;
      border-width: 0px 0px 0px 2px;
      border-style: solid;
    }

    #status, #parent{
      display: flex;
      
    }

    #status:hover {
      background-color:#3c4444;
    }

  </style>
  