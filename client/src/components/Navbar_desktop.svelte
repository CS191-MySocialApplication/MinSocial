<script>
    export let mentions;
    export let hoverMentions;
    export let dm;
    export let hoverDM;
    export let settings;
    export let hoverSettings;

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
            
    </nav>
</main>

<style>
    main {
        
        margin: 0;
        background-color: #50c0cb;
        color: white;

        
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




