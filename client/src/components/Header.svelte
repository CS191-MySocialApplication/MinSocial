<script>
    import Toggle from "./Toggle.svelte";
    import "@fontsource/open-sans";
    export let title;
    export let icon;
    export let value = "none";
</script>

<main>
    <div class="headerContainer">
        <div class="headerContent">
            {#if title!="Toot"}
                <img src={icon} class="headerIcon" alt="icon"/>
            {:else}
                <a class="icon" href="/home">
                    <img src={icon} class="backButton" alt="back"/>          
                </a>
            {/if}
            


            <h1 class="Menu">{title}</h1>
        </div>
    
        
        {#if title=="Replies"}
            <Toggle bind:value={value} label="Show Replies"/>
        {/if}
    </div>
</main>

<style>
    main {
        position: fixed;
        z-index: 1;
        width: 100%;
        font-family: "Open Sans", "sans-serif";
        background-color: #252c2c;
        color: white;
        border-bottom: 3px solid #50c0cb;
        margin: -8px 0px 0px 0px;
    }
    .headerContainer {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    img{
        width: 28px;
        height: 28px;
        display:inline-block;
        vertical-align:middle;
        margin-left: 1.5rem;
        margin-right: 10px;
    }
    h1 {
        font-weight: 700;
        letter-spacing: 0.5px;   
        display:inline-block;
        vertical-align:middle;     
    }
    
    @media screen and (hover: none) {
        h1 {
            padding: 24px 0px;
            letter-spacing: 0.6px;
            font-size: 18px;
        }
        .headerContainer {
            margin-right: 24px;
        }
    }
    
    @media screen and (hover: hover) {
        h1 {
            padding: 24px 0px;
            font-size: 20px;
        }
        .headerContainer {
            width: 85lvw;
            margin-right: 24px;
        }
    }
    .backButton:hover {
        background-color: #3c4444;
        fill-opacity: 0.5;
        border-radius: 50%;
    }
</style>