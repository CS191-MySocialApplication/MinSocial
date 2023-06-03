<script>
    import { loop_guard } from "svelte/internal";

    export let imageValue;
    export let image;

    export let filePreview = []

    //Change to svg!
    import attachmentChosen from "../../public/attachmentChosen.png";
    import attachmentNotChosen from "../../public/attachmentNotChosen.png";
    import Postform from "./Postform.svelte";


    function inputValidation(){
        if(image.length > 1){
            for(let i = 0; i < image.length; i++){
                if(image[i].type.split("/")[0] !== "image"){
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

        filePreview = Array.from(image).map(x => {
            return {type: x.type.split("/")[0], url: URL.createObjectURL(x)}
        })
    }

</script>

<label for="fileInput">
    Press
</label>
<input type="file" id="fileInput" multiple bind:this={imageValue} bind:files={image} accept="video/*, image/*" on:change={inputValidation}>

<div>
    {#each filePreview as preview}
        {#if preview.type === "image"}        
            <img src={preview.url} alt="imagePreview">
        {:else if preview.type === "video"}
            <video src={preview.url} controls id="mediaVideo">
                <track kind="captions">
            </video>
        {:else if preview.type === "audio"}
            <source src={preview.url} type="{preview.type}">
        {/if}
    {/each}
</div>

<style>
    img {
        max-width: 100px;
        max-height: 100px;
    }
    /*
    input[type="file"]::file-selector-button {
        display: none;
    }*/
    /* input[type="file"] {
        display: none;
    } */
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