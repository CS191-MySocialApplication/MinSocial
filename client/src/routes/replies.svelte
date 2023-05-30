<script>

    import Header from "../components/Header.svelte";
    import ReplyHeader from "../../public/reply_header.png";
    import NavbarDesktop from "../components/NavbarDesktop.svelte"; 
    import NavbarMobile from "../components/NavbarMobile.svelte";
  
    import UnclickedMentions from "../../public/unclicked_mentions.png";
    import HoverUnclickedMentions from "../../public/hover_unclicked_mentions.png";
    import UnclickedDM from "../../public/unclicked_dm.png";
    import HoverUnclickedDM from "../../public/hover_unclicked_dm.png";
    import ClickedReply from "../../public/clicked_reply.png";
    import HoverClickedReply from "../../public/hover_clicked_reply.png";
  
    import Logout from "../../public/logout.png";
    import HoverLogout from "../../public/hover_logout.png";
    let value;
  
    async function getHomeContent() {
      // TODO
    }
  
    let auth_promise = getHomeContent();
  </script>
  
  <div class="desktopFormat">
    <NavbarDesktop
      mentions={UnclickedMentions}
      hoverMentions={HoverUnclickedMentions}
      dm={UnclickedDM}
      hoverDM={HoverUnclickedDM}
      reply={ClickedReply}
      hoverReply={HoverClickedReply}
      logout={Logout}
      hoverLogout={HoverLogout}
    />
  
    <div class="content">
      <Header bind:value={value} title="Replies" icon={ReplyHeader} />
      <main style="display:{value}">
        <!-- TODO -->
      </main>
    </div>
  
    <NavbarMobile
      mentions={UnclickedMentions}
      hoverMentions={HoverUnclickedMentions}
      dm={UnclickedDM}
      hoverDM={HoverUnclickedDM}
      reply={ClickedReply}
      hoverReply={HoverClickedReply}
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
  