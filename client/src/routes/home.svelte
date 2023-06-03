<script>
    import Header from "../components/Header.svelte";
    import Postform from "../components/Postform.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte";
    import NavbarMobile from "../components/NavbarMobile.svelte";
    import Status from '../components/Status.svelte';

    import { getHomeContent } from "../sdk/mentions_timeline";

    import { link } from 'svelte-spa-router';
    import { lastPageAccessed } from "./store.ts";

    let pageTitle = "Mentions"
    let auth_promise = getHomeContent();

</script>
  
  <div class="desktopFormat">
    <NavbarDesktop lastPageAccessed={$lastPageAccessed}/>
  
    <div class="content">
      <Header title={pageTitle}/>
      <main on:load|once={lastPageAccessed.update( n => "/#/home")}>
        <Postform/>
        {#await auth_promise}
          <p>waiting...</p>
        {:then response}
          {#each response as status, index}
            {#if Object.entries(response).length-1 == index}
              <div id="status">
                <Status status={status}/>
              </div>
            {:else}
            <div id="status"
            style="border-style: none none solid none;
            border-color: #50c0cb;
            border-width: 1px;">
              <Status status={status}/>
            </div>
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

  #status {
    display: flex;
  }
  

  
</style>