<script>
    // Component needed for header
    import Toggle from "./Toggle.svelte";

    // Font family to be used
    import "@fontsource/open-sans";

    // Variables needed for the Header and Toggle components
    export let title;  
    export let value = "none";

    // Icons that would be used for the Header
    import MentionsHeader from "../../public/mentionsHeader.svelte";
    import MessagesHeader from "../../public/dmHeader.svelte";
    import RepliesHeader from "../../public/replyHeader.svelte";
    import BackButton from "../../public/back.svelte"

    import {push, pop, replace} from 'svelte-spa-router'

    import { lastPageAccessed } from "../routes/store.ts";
</script>

<main>
    <div class="headerContainer">
        <div class="headerContent">
            {#if title == "Mentions"}
                <div class="headerIcon">
                    <MentionsHeader/>
                </div>
            {:else if title == "Replies"}
                <div class="headerIcon">
                    <RepliesHeader/>
                </div>
            {:else if title == "Messages"}
                <div class="headerIcon">
                    <MessagesHeader/>
                </div>
            {:else}
                <div class="backButtonIcon" on:click={()=>pop()} on:keypress>
                    <BackButton/>        
                </div>
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
        margin: 0px;
    }
    .headerContainer {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .headerIcon, .backButtonIcon {
        width: 28px;
        height: 28px;
        display: inline-block;
        vertical-align: middle;
        margin-left: 1.5rem;
        margin-right: 4px;
    }
    .backButtonIcon:hover {
        background-color: #3c4444;
        fill-opacity: 0.5;
        border-radius: 50%;
    }
    h1 {
        font-weight: 700;
        letter-spacing: 0.5px;   
        display:inline-block;
        vertical-align: middle;     
    }
    
    @media screen and (hover: none) {
        h1 {
            padding: 10px 0px;
            letter-spacing: 0.6px;
            font-size: 16px;
        }
        .headerContainer {
            margin-right: 24px;
        }
    }
    
    @media screen and (hover: hover) {
        h1 {
            padding: 10px 0px;
            font-size: 16px;
        }
        .headerContainer {
            width: 85lvw;
            margin-right: 24px;
        }
    }
</style>