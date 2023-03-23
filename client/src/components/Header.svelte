<script>
    import "@fontsource/open-sans"
    export let title;
    export let icon;
</script>

<main>
    <img src={icon} class="headerIcon" alt="icon"/>
    <h1 class="Menu">{title}</h1>
</main>

<style>
    main {
        font-family: "Open Sans", "sans-serif";
        margin: 0;
        background-color: #252c2c;
        color: white;
        border-bottom: 3px solid #50c0cb;
    }
    
    img{
        width: 27px;
        height: 27px;
        display:inline-block;
        vertical-align:middle;
        margin-right: 5px;
    }
    h1 {
        margin: 0;
        font-weight: 700;
        letter-spacing: 0.5px;   
        display:inline-block;
        vertical-align:middle;     
    }
    


    @media screen and (max-width:479px) {
        h1 {
            padding: 24px 0px;
            letter-spacing: 0.6px;
            font-size: 18px;
        }
    }
    
    @media screen and (min-width:480px) {
        h1 {
            padding: 24px 0px;
            font-size: 20px;
        }
    }
</style>