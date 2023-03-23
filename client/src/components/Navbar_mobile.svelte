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
    <nav class="nav-bar-mobile">
        <!--No icons yet. li placed in the meantime-->
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
            
        .clicked{
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

        .mentions:hover .hover_img, .dm:hover .hover_img, .settings:hover .hover_img {
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