<script>

    import ClickedMentions from '../../public/clicked_mentions.png';
    import HoverClickedMentions from '../../public/hover_clicked_mentions.png';
    import UnClickedMentions from '../../public/hover_unclicked_mentions.png';
    import HoverUnclickedMentions from '../../public/hover_unclicked_mentions.png';
    import ClickedDM from '../../public/clicked_dm.png';
    import HoverClickedDM from '../../public/hover_clicked_dm.png';
    import ClickedSettings from '../../public/clicked_settings.png';
    import HoverClickedSettings from '../../public/hover_clicked_settings.png';
    
</script>

<main>
    <nav class="nav-bar-desktop">
        
        <a class="mentions" href="/home">
            <div class="clicked">
                <img src={ClickedMentions} alt="clicked mentions"/>
                <img src={HoverClickedMentions} class="hover_img" alt="hover clicked mentions"/>
            </div>
            <div class="unclicked">
                <img src={UnClickedMentions} alt="unclicked mentions"/>
                <img src={HoverUnclickedMentions} class="hover_img" alt="hover unclicked mentions"/>
            </div>
        </a>
        <a class="dm" href="/messages">
            <img src={ClickedDM} alt="clicked dm"/>
            <img src={HoverClickedDM} class="hover_img" alt="hover clicked dm"/>
        </a>

        <a class="settings" href="login.html">
            <img src={ClickedSettings} alt="clicked settings"/>
            <img src={HoverClickedSettings} class="hover_img" alt="hover clicked settings"/>
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
        margin-left: 50px;
        margin-top: 30px;
        position: absolute;
        display: flex;
    }

    .clicked{
        position: absolute;
        display: flex;
    }
    
    .dm{
        border:none;
        background-color: inherit;
        margin-left: 50px;
        margin-top: 100px;
        position: absolute;
        display: flex;
    }

    .settings{
        border:none;
        background-color: inherit;
        margin-left: 50px;
        margin-top: 170px;
        position: absolute;
        display: flex;
    }
    
    .hover_img{
        display: none;
        position: absolute;    
    }

    .unclicked{
        display: none;
        position: absolute; 
    }

    .mentions:hover .hover_img{
        display: inline;
        opacity:0.5;
        transition: 0.25s ease;
    }
    
    .dm:hover .hover_img{
        display: flex;
        opacity:0.5;
        transition: 0.25s ease;
    }
    
    .settings:hover .hover_img{
        display: flex;
        opacity:0.5;
        transition: 0.25s ease;
    }

    
</style>




