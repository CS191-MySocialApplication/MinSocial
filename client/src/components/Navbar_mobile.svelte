<script>
    export let mentions;
    export let hoverMentions;
    export let dm;
    export let hoverDM;
    export let settings;
    export let hoverSettings;
    
</script>

<main>
    <nav class="nav-bar-mobile">
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

    @media screen and (max-width:479px) {
        img {
            width: 40px;
            height: 40px;
        }
        .mentions {
            margin-top: 20px;
            margin-left: 65px;
            position: absolute;
            display: flex;
        }

        .dm {
            margin-top: 20px;
            margin-left: 165px;
            position: absolute;
            display: flex;
        }
        
        .settings {
            margin-top: 20px;
            margin-left: 265px;
            position: absolute;
            display: flex;   
        }
            
        .hoverImg{
            display: none;
            position: absolute;    
        }

        .mentions:hover .hoverImg, .dm:hover .hoverImg, .settings:hover .hoverImg {
            display: inline;
            opacity:0.5;
            transition: 0.25s ease;
        }
    }

    @media screen and (min-width:480px) {
        main {
            display: none;
        }
    }
</style>