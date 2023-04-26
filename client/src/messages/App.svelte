<script>
  import Header from "../components/Header.svelte";
  import Postform from "../components/Postform.svelte";
  import NavbarDesktop from "../components/NavbarDesktop.svelte";
  import NavbarMobile from "../components/NavbarMobile.svelte";
  import { each } from "svelte/internal";

  import UnclickedMentions from "../../public/unclicked_mentions.png";
  import HoverUnclickedMentions from "../../public/hover_unclicked_mentions.png";
  import ClickedDM from "../../public/clicked_dm.png";
  import HoverClickedDM from "../../public/hover_clicked_dm.png";
  import UnclickedSettings from "../../public/unclicked_settings.png";
  import HoverUnclickedSettings from "../../public/hover_unclicked_settings.png";
  import MessagesHeader from "../../public/dm_header.png";

  async function getMessageContent() {
    let res = await fetch("/api/messages");
    let text = await res.json();

    if (res.ok) {
      return text;
    } else {
      throw new Error(text);
    }
  }

  let auth_promise = getMessageContent();
</script>

<div class="desktopFormat">
  <NavbarDesktop
    mentions={UnclickedMentions}
    hoverMentions={HoverUnclickedMentions}
    dm={ClickedDM}
    hoverDM={HoverClickedDM}
    settings={UnclickedSettings}
    hoverSettings={HoverUnclickedSettings}
    class="navbar"
  />

  <div class="content">
    <Header title="Messages" icon={MessagesHeader} />
    <main>
      {#await auth_promise}
        <p>Waiting...</p>
      {:then conversations}
        {#each conversations as conversation}
          <div class="conversation">
            <span id="source" class="imptDetails"
              >{conversation["source"]} |</span
            >
            <span id="username" class="imptDetails"
              >{conversation["author"]["username"]}</span
            ><br />
            <span id="dateTime">{conversation["createdTime"]}</span><br />
            <p>{conversation["content"]}</p>
            <br /><br />
          </div>
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
    settings={UnclickedSettings}
    hoverSettings={HoverUnclickedSettings}
  />
</div>

<style>
  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 2rem;
    width: 100%;
    margin: 0 auto;
    box-sizing: border-box;
  }

  .content {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  @media screen and (hover: none) {
    .desktopFormat {
      display: flex;
      flex-direction: column;
      align-items: stretch;
    }
  }

  @media screen and (hover: hover) {
    .desktopFormat {
      display: flex;
      flex-direction: row;
    }
    .content {
      display: flex;
      flex-direction: column;
      margin-left: 11.5%;
      width: 100%;
    }
  }
</style>
