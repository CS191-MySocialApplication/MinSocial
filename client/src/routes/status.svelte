<script>
    import Header from "../components/Header.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte";
    import NavbarMobile from "../components/NavbarMobile.svelte";
    import Status from '../components/Status.svelte';

    import Postform from "../components/Postform.svelte";

    import {link} from 'svelte-spa-router';

    export let params = {};
    
    import { getStatus } from "../sdk/status"
  
    let auth_promise = getStatus(params);
  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop title="Toot"/>
  
    <div class="content">
      <Header title="Toot"/>
      <main>
        {#await auth_promise}
          <p>waiting...</p>
        {:then response }
          {#each response as status}
            <!--<a class="post" href="/context/toot/{status["id"]}" use:link>
              Change href to mentions thread
              <p id="source" class="imptDetails">{status["source"]} | {status["author"]["username"]}</p>
              <span id="dateTime">{status["createdTime"]}</span><br />
              <p>{@html status["content"]}</p>
            </a>-->
            <Status status={status}/>
          {/each}
        {:catch error}
          <p style="color: red">{error.message}</p>
        {/await}
      </main>
    </div>
  
    <NavbarMobile title="Toot"/>
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
    
  </style>
  