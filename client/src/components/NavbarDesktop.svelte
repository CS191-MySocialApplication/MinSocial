<script>
    // Icons for the navbar
    import ClickedMentions from "../../public/mentionsClicked.svelte";
    
    
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
		} else {
			throw new Error(text);
		} 
    }
    

</script>

<main>
    <nav class="navBarDesktop">
        <div class="iconContainerOutside">
            <div class="iconContainer">

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

            </div>
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
        z-index: 2;
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background-color: #50c0cb;
        color: white;
        width: 12lvw;
        height: 100lvh;
    }

    @media screen and (hover: none) {
        main {
            display: none;
        }
    }
    .iconContainerOutside {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .iconContainer {
        padding-top: 30px;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    .logout {
        position: absolute;
        bottom: 0;
        padding-bottom: 30px;
    }

    .mentions, .dm, .reply, .logout{
        height: 40px;
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
</style>