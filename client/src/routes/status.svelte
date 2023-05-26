<script>
    import Header from "../components/Header.svelte";
    import NavbarDesktop from "../components/NavbarDesktop.svelte";
    import NavbarMobile from "../components/NavbarMobile.svelte";
  
    import ClickedMentions from "../../public/clicked_mentions.png";
    import HoverClickedMentions from "../../public/hover_clicked_mentions.png";
    import UnclickedDM from "../../public/unclicked_dm.png";
    import HoverUnclickedDM from "../../public/hover_unclicked_dm.png";
    import UnclickedReply from "../../public/unclicked_reply.png";
    import HoverUnclickedReply from "../../public/hover_unclicked_reply.png";
  
    import Logout from "../../public/logout.png";
    import HoverLogout from "../../public/hover_logout.png";
  
    import backButton from "../../public/back.png";

    import {link} from 'svelte-spa-router';
  
    export let params = {};

    async function getStatus() {

        if(params && params.id){
            let res = await fetch("/api/toot/"+String(params.id));
            let text = await res.json();
            console.log(text)
            if (res.status == 200 || res.status == 206) {
                return text;
            } else {
                throw new Error(text);
            }
        }
    }
  
    let auth_promise = getStatus();
  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop
      mentions={ClickedMentions}
      hoverMentions={HoverClickedMentions}
      dm={UnclickedDM}
      hoverDM={HoverUnclickedDM}
      reply={UnclickedReply}
      hoverReply={HoverUnclickedReply}
      logout={Logout}
      hoverLogout={HoverLogout}
    />
  
    <div class="content">
      <Header title="Toot" icon={backButton} />
      <main>
        {#await auth_promise}
          <p>waiting...</p>
        {:then status }
            <a class="post" href="/toot/{status["id"]}" use:link>
              <!--Change href to mentions thread-->
              <p id="source" class="imptDetails">{status["source"]} | {status["author"]["username"]}</p>
              <span id="dateTime">{status["createdTime"]}</span><br />
              <p>{@html status["content"]}</p>
            </a>
        {:catch error}
          <p style="color: red">{error.message}</p>
        {/await}
      </main>
    </div>
  
    <NavbarMobile
      mentions={ClickedMentions}
      hoverMentions={HoverClickedMentions}
      dm={UnclickedDM}
      hoverDM={HoverUnclickedDM}
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
    
  </style>
  