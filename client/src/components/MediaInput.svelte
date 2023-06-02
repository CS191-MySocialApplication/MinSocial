<script>
    export let imageValue;
    export let image;

    let fileChosen = false;

    //Change to svg!
    import attachmentChosen from "../../public/attachmentChosen.png";
    import attachmentNotChosen from "../../public/attachmentNotChosen.png";
  import Postform from "./Postform.svelte";

</script>

<label for="fileInput">
    <!--Better if img change happens when a file is confirmed to be uploaded-->
    {#if !fileChosen}
        <img src={attachmentNotChosen} alt="mediaIcon"/>
    {:else}
        
        <img src={attachmentChosen} alt="mediaIcon"/>
    {/if}
    
</label>
<input type="file" id="fileInput" multiple bind:value={imageValue} bind:files={image} on:click={()=>{fileChosen = !fileChosen;}}>

<style>
    img {
        height: 30px;
        width: 30px;
    }
    /*
    input[type="file"]::file-selector-button {
        display: none;
    }*/
    input[type="file"] {
        display: none;
    }
    label {
        height: 30px;
        width: 30px;
        margin-left: 5px;
        margin-right:4px;
        display:inline-flex;
        border-radius: 5px;
    }

    label:hover {
        background-color: #252c2c;
    }

</style>