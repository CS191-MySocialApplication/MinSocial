<script>
  // Used to help svelte distinguish between pages
  export let lastPageAccessed;

  // Icons for the navbar
  import ClickedMentions from "../../public/mentionsClicked.svelte";
  import ClickedReplies from "../../public/replyClicked.svelte";
  import ClickedDM from "../../public/dmClicked.svelte";

  import UnclickedMentions from "../../public/mentionsUnclicked.svelte";
  import UnclickedReplies from "../../public/replyUnclicked.svelte";
  import UnclickedDM from "../../public/dmUnclicked.svelte";

  import Logout from "../../public/Logout.svelte";

  import {onMount} from 'svelte';

  let mstdnLogin = true;
  let mstdnLoginLink = "";

  onMount(async () =>{
        mstdnLogin = document.cookie.split(";").some((item) => item.trim().startsWith("mstdnAccessToken="));

        if(mstdnLogin == false){
            let res = await fetch('/auth/mstdn');
            let text = await res.json();

            if (res.ok){
                mstdnLoginLink = text["auth_url"];
            }
        }
    });

    async function sendMstdnLogout(event){

        let res = await fetch('/auth/mstdn/logout');
		    let text = await res.json();

		    if (res.ok){
          window.location.replace("/");
		    } else{
			    throw new Error(text);
		    } 
    }
</script>


<main>
  <nav class="navBarMobile">
    <div class="iconContainer">
      {#if lastPageAccessed === "/#/home"}
        <div class="mentions">
            <a class="icon" href="/#/home">
                <ClickedMentions/>         
            </a>
        </div>  
        <div class="reply">
            <a class="icon" href="/#/replies">
                <UnclickedReplies/>        
            </a>
        </div>
        <div class="dm">
            <a class="icon" href="/#/messages">
                <UnclickedDM/>         
            </a>
        </div>
      {:else if lastPageAccessed === "/#/replies"}
          <div class="mentions">
              <a class="icon" href="/#/home">
                  <UnclickedMentions/>         
              </a>
          </div>  
          <div class="reply">
              <a class="icon" href="/#/replies">
                  <ClickedReplies/>        
              </a>
          </div>
          <div class="dm">
              <a class="icon" href="/#/messages">
                  <UnclickedDM/>         
              </a>
          </div>
      {:else if lastPageAccessed === "/#/messages"}
          <div class="mentions">
              <a class="icon" href="/#/home">
                  <UnclickedMentions/>         
              </a>
          </div>  
          <div class="reply">
              <a class="icon" href="/#/replies">
                  <UnclickedReplies/>        
              </a>
          </div>
          <div class="dm">
              <a class="icon" href="/#/messages">
                  <ClickedDM/>         
              </a>
          </div>
      {:else}
          <!--Expected behavior for now-->
          <div class="mentions">
              <a class="icon" href="/#/home">
                  <ClickedMentions/>         
              </a>
          </div>  
          <div class="reply">
              <a class="icon" href="/#/replies">
                  <UnclickedReplies/>        
              </a>
          </div>
          <div class="dm">
              <a class="icon" href="/#/messages">
                  <UnclickedDM/>         
              </a>
          </div>
      {/if}
      <div class="logout">
        <a class="icon" on:click={sendMstdnLogout} href="#0">
            <!--Log Out Mastodon-->
            <Logout/>
        </a>
      </div>
    </div>
  </nav>
</main>

<style>
  main {
    position: fixed;
    width: 100%;
    height: 80px;
    left: 0;
    bottom: 0;
    margin: 0;
    background-color: #50c0cb;
    color: white;
  }

  /*Touch screen*/
  @media screen and (hover: none) {
    .navBarMobile {
      display: flex;
      max-width: 100%;
      justify-content: center;
    }

    .iconContainer {
      display: flex;
      flex: 1 1 auto;
      height: 80px;
      max-width: 400px;
      justify-content: space-around;
      align-items: center;
    }

    .mentions,
    .dm,
    .reply,
    .logout {
      width: 45px;
      display: flex;
      justify-content: center;
    }

    .icon {
        width: 45px;
        height: 45px;
        fill: #50C0CB;
    }
    
    .icon:hover {
        fill: #fff;
        opacity:0.5;
        transition: 0.25s ease;
    }
  }
  /*Desktop or Laptop*/
  @media screen and (hover: hover) {
    main {
      display: none;
    }
  }
</style>
