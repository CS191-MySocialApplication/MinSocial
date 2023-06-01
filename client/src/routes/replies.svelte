<script>

    import Header from "../components/Header.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte"; 
    import NavbarMobile from "../components/NavbarMobile.svelte";
    import Status from '../components/Status.svelte';

    import {link} from 'svelte-spa-router';
  
    let value;
  
    async function getHomeContent() {
      let res = await fetch("/api/replies");
      let text = await res.json();

      if (res.status == 200 || res.status == 206) {
        return text;
      } else {
        throw new Error(text);
      }
    }
  
    let auth_promise = getHomeContent();

  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop title="Replies"/>
  
    <div class="content">
      <Header bind:value={value} title="Replies"/>
      <main style="display:{value}">
        {#await auth_promise}
          <p>waiting...</p>
        {:then response}
          {#each response as status}

            <Status status={status}/>

          {/each}
        {:catch error}
          <p style="color: red">{error.message}</p>
        {/await}
      </main>
    </div>
  
    <NavbarMobile title="Replies"/>
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
  