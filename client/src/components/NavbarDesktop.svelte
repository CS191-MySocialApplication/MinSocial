<script>
    // Used to help svelte distinguish between pages
    export let lastPageAccessed;

    // Icons for the navbar
    import Logo from "../../public/logo.svelte";

    import ClickedMentions from "../../public/mentionsClicked.svelte";
    import ClickedReplies from "../../public/replyClicked.svelte";
    import ClickedDM from "../../public/dmClicked.svelte";
    
    import UnclickedMentions from "../../public/mentionsUnclicked.svelte";
    import UnclickedReplies from "../../public/replyUnclicked.svelte";
    import UnclickedDM from "../../public/dmUnclicked.svelte";
    
    import Logout from "../../public/Logout.svelte";

    import {onMount} from 'svelte';

    import {link} from 'svelte-spa-router'

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
            <div class="logo">
                <Logo/>
            </div>
            <div class="iconContainer">
                {#if lastPageAccessed === "/#/home"}
                    <div class="mentions">
                        <a class="icon" href="/home" use:link>
                            <ClickedMentions/>         
                        </a>
                    </div>  
                    <div class="reply">
                        <a class="icon" href="/replies" use:link>
                            <UnclickedReplies/>        
                        </a>
                    </div>
                    <div class="dm">
                        <a class="icon" href="/messages" use:link>
                            <UnclickedDM/>         
                        </a>
                    </div>
                {:else if lastPageAccessed === "/#/replies"}
                    <div class="mentions">
                        <a class="icon" href="/home" use:link>
                            <UnclickedMentions/>         
                        </a>
                    </div>  
                    <div class="reply">
                        <a class="icon" href="/replies" use:link>
                            <ClickedReplies/>        
                        </a>
                    </div>
                    <div class="dm">
                        <a class="icon" href="/messages" use:link>
                            <UnclickedDM/>         
                        </a>
                    </div>
                {:else if lastPageAccessed === "/#/messages"}
                    <div class="mentions">
                        <a class="icon" href="/home" use:link>
                            <UnclickedMentions/>         
                        </a>
                    </div>  
                    <div class="reply">
                        <a class="icon" href="/replies" use:link>
                            <UnclickedReplies/>        
                        </a>
                    </div>
                    <div class="dm">
                        <a class="icon" href="/messages" use:link>
                            <ClickedDM/>         
                        </a>
                    </div>
                {:else}
                    <!--Expected behavior for now-->
                    <div class="mentions">
                        <a class="icon" href="/home" use:link>
                            <ClickedMentions/>         
                        </a>
                    </div>  
                    <div class="reply">
                        <a class="icon" href="/replies" use:link>
                            <UnclickedReplies/>        
                        </a>
                    </div>
                    <div class="dm">
                        <a class="icon" href="/messages" use:link>
                            <UnclickedDM/>         
                        </a>
                    </div>
                {/if}
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

    .logo {
        padding-top: 20px;
    }
</style>