<script>
  import Header from "../components/Header.svelte";
  //import Postform from "../components/Postform.svelte";
  import NavbarDesktop from "../components/NavbarDesktop.svelte";
  import NavbarMobile from "../components/NavbarMobile.svelte";
  import { each } from "svelte/internal";

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
    reply={UnclickedReply}
    hoverReply={HoverUnclickedReply}
    logout={Logout}
    hoverLogout={HoverLogout}
    class="navbar"
  />
  
  <div class="content">
    <Header title="Messages" icon={MessagesHeader} />
    <main>
      {#await auth_promise}
        <p>waiting...</p>
      {:then conversations}
        {#each conversations as conversation}
          <a class="conversation" href="/messages">
            <!--Change href to conversation thread-->
            <p id="source" class="imptDetails">
              {conversation["source"]} | {conversation["author"]["username"]}</p>
            <span id="dateTime">{conversation["createdTime"]}</span><br />
            <p>{@html conversation["content"]}</p>
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
    margin-top:90px;
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 2rem;
    width: 100%;
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
