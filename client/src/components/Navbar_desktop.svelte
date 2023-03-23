<script>
    export let mentions;
    export let hoverMentions;
    export let dm;
    export let hoverDM;
    export let settings;
    export let hoverSettings;

    import {onMount} from 'svelte';

    let twtLogin = true;
    let mstdnLogin = true;

    let twtLoginLink = "";
    let mstdnLoginLink = "";


    onMount(async ()=>{
        twtLogin = document.cookie.split(";").some((item) => item.trim().startsWith("twtAccessToken="));
        mstdnLogin = document.cookie.split(";").some((item) => item.trim().startsWith("mstdnAccessToken="));

        if(twtLogin == false && mstdnLogin == false){window.location.replace("/")};

        if(twtLogin == false){
            let res = await fetch('/auth/twt');
            let text = await res.json();

            if (res.ok){
                twtLoginLink = text["auth_url"];
            }

        }

        if(mstdnLogin == false){
            let res = await fetch('/auth/mstdn');
            let text = await res.json();

            if (res.ok){
                mstdnLoginLink = text["auth_url"];
            }

        }

    });

    async function sendTwtLogout(){
        
        let res = await fetch('/auth/twt/logout');
		let text = await res.json();

		if (res.ok){
			if(mstdnLogin){
                window.location.reload();
            }else{
                window.location.replace("/");
            }
		}else{
			throw new Error(text);
		} 

    }

    async function sendMstdnLogout(event){
        console.log("sdfsdf")

        let res = await fetch('/auth/mstdn/logout');
		let text = await res.json();

		if (res.ok){
            if(twtLogin){
                window.location.reload();
            }else{
                window.location.replace("/");
            }
		}else{
			throw new Error(text);
		} 
    }
    

</script>

<main>
    <nav class="nav-bar-desktop">
        
        <a class="mentions" href="/home">
            <img src={mentions} alt="mentions"/>
            <img src={hoverMentions} class="hoverImg" alt="hover mentions"/>
        </a>
        <a class="dm" href="/messages">
            <img src={dm} alt="dm"/>
            <img src={hoverDM} class="hoverImg" alt="hover dm"/>
        </a>

        <a class="settings" href="login.html">
            <img src={settings} alt="settings"/>
            <img src={hoverSettings} class="hoverImg" alt="hover settings"/>
        </a>
        
        {#if !twtLogin}
            <br/><br/><br/>
            <a class="settings" href={twtLoginLink}>
                Log in with Twitter
            </a>
        {:else}
            <br/><br/><br/>
            <a class="settings" on:click={sendTwtLogout} href="#0">
                Log Out Twitter
            </a>
        {/if}
        
        {#if !mstdnLogin}
            <br/><br/><br/>
            <a class="settings" href={mstdnLoginLink}>
                Log in with Mastodon
            </a>
        {:else}
            <br/><br/><br/>
            <a class="settings" on:click={sendMstdnLogout} href="#0">
                Log Out Mastodon
            </a>
        {/if}
    </nav>  
</main>

<style>
    main {
        margin: 0;
        background-color: #50c0cb;
        color: white;
        height: 100lvh;
    }
    @media screen and (max-width:479px) {
        main {
            display: none;
        }
    }

    @media screen and (min-width:480px) and (max-width: 899px) {
        main {
            width: 24%;
            margin-right: 20px;
        }
    }

    @media screen and (min-width:900px) {
        main {
            width: 14%;
            margin-right: 20px;
        }
    }
    img{
        width: 40px;
        height: 40px;
    }

    .mentions{
        margin-left: 70px;
        margin-top: 30px;
        position: absolute;
        display: flex;
    }
   
    .dm{
        margin-left: 70px;
        margin-top: 100px;
        position: absolute;
        display: flex;
    }

    .settings{
        margin-left: 70px;
        margin-top: 170px;
        position: absolute;
        display: flex;
    }
    
    .hoverImg{
        display: none;
        position: absolute;    
    }

    .mentions:hover .hoverImg{
        display: inline;
        opacity:0.5;
        transition: 0.25s ease;
    }
    
    .dm:hover .hoverImg{
        display: flex;
        opacity:0.5;
        transition: 0.25s ease;
    }
    
    .settings:hover .hoverImg{
        display: flex;
        opacity:0.5;
        transition: 0.25s ease;
    }

    
</style>




