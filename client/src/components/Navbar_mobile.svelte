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
        <div class="iconContainer">
            <div class="mentions">
                <a class="icon" href="/home">
                    <img src={mentions} class="noHover" alt="mentions"/>
                    <img src={hoverMentions} class="hoverImg" alt="hover mentions"/>
                </a>
            </div>
    
            <div class="dm">
                <a class="icon" href="/messages">
                    <img src={dm} class="noHover" alt="dm"/>
                    <img src={hoverDM} class="hoverImg" alt="hover dm"/>
                </a>
            </div>
            
            <div class="settings">
                <a class="icon" href="login.html">
                    <img src={settings} class="noHover" alt="settings"/>
                    <img src={hoverSettings} class="hoverImg" alt="hover settings"/>
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

    @media screen and (max-width:479px) {
        img, .icon {
            width: 40px;
            height: 40px;
        }

        .iconContainer {
            display: flex;
            height: 80px;
            padding: 0 16px;
            justify-content: space-around;
            align-items: center;
        }

        .mentions, .dm, .settings {
            width: 40px;
            display: flex;
            justify-content: center;
        }

        .mentions:hover .noHover, .dm:hover .noHover, .settings:hover .noHover{
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
    }

    @media screen and (min-width:480px) {
        main {
            display: none;
        }
    }
</style>