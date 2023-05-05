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
                    <a class="icon" href="/home">
                        <img src={mentions} class="noHover" alt="mentions"/>
                        <img src={hoverMentions} class="hoverImg" alt="hover mentions"/>            
                    </a>
                </div>

                <div class="reply">
                    <a class="icon" href="login.html">
                        <img src={reply} class="noHover" alt="reply"/>
                        <img src={hoverReply} class="hoverImg" alt="hover reply"/>            
                    </a>
                </div>

                <div class="dm">
                    <a class="icon" href="/messages">
                        <img src={dm} class="noHover" alt="dm"/>
                        <img src={hoverDM} class="hoverImg" alt="hover dm"/>            
                    </a>
                </div>
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

    img, .icon {
        width: 40px;
        height: 40px;
    }
    
    .mentions:hover .noHover, .dm:hover .noHover, .reply:hover .noHover, .logout:hover .noHover{
        opacity:0.5;
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

    /*
    a {
        color: #252c2c;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }*/
</style>