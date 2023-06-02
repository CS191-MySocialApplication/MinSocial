<script>
    export let imageValue;
    export let image;

    let fileChosen = false;

    //Change to svg!
    import attachmentChosen from "../../public/attachmentChosen.png";
    import attachmentNotChosen from "../../public/attachmentNotChosen.png";
    import Postform from "./Postform.svelte";


    function inputValidation(){
        if(image.length > 1){
            for(let i = 0; i < image.length; i++){
                if(image[i].type.split("/")[0] != "image"){
                    image = [];
                    imageValue.value = "";
                    alert("Multiple file posting is only available to images.");
                    return;
                }
            }
        }

        if(image.length > 4){
            image = [];
            imageValue.value = "";
            alert("You can only post 4 images max.")
        }
    }

</script>

<label for="fileInput">
    <!--Better if img change happens when a file is confirmed to be uploaded-->
    {#if !fileChosen}
        <img src={attachmentNotChosen} alt="mediaIcon"/>
    {:else}
        
        <img src={attachmentChosen} alt="mediaIcon"/>
    {/if}
    
</label>
<input type="file" id="fileInput" multiple bind:this={imageValue} bind:files={image} accept="video/*, image/*" on:change={inputValidation} on:click={()=>{fileChosen = !fileChosen;}}>

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