<script>
  export let mentions;
  export let hoverMentions;
  export let dm;
  export let hoverDM;
  export let reply;
  export let hoverReply;
  export let logout;
  export let hoverLogout;

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
      <div class="mentions">
        <a class="icon" href="/home">
          <img src={mentions} class="noHover" alt="mentions" />
          <img src={hoverMentions} class="hoverImg" alt="hover mentions" />
        </a>
      </div>

      <div class="reply">
        <a class="icon" href="/replies">
          <img src={reply} class="noHover" alt="reply" />
          <img src={hoverReply} class="hoverImg" alt="hover reply" />
        </a>
      </div>

      <div class="dm">
        <a class="icon" href="/messages">
          <img src={dm} class="noHover" alt="dm" />
          <img src={hoverDM} class="hoverImg" alt="hover dm" />
        </a>
      </div>

      <div class="logout">
        <a class="icon" on:click={sendMstdnLogout} href="#0">
          <!--Log Out Mastodon-->
          <img src={logout} class="noHover" alt="logout"/>
          <img src={hoverLogout} class="hoverImg" alt="hover logout"/>
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
    img,
    .icon {
      width: 40px;
      height: 40px;
    }

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
      width: 40px;
      display: flex;
      justify-content: center;
    }

    .mentions:hover .noHover,
    .dm:hover .noHover,
    .reply:hover .noHover
    .logout:hover .noHover {
      opacity: 0.5;
      transition: 0.25s ease;
    }

    .hoverImg {
      position: absolute;
      z-index: 1;
    }

    .noHover {
      position: absolute;
      z-index: 2;
    }
  }

  /*Desktop or Laptop*/
  @media screen and (hover: hover) {
    main {
      display: none;
    }
  }
</style>
