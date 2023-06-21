<script>
    import { loop_guard } from "svelte/internal";

    export let imageValue;
    export let image;

    export let filePreview = [];

    function inputValidation() {
        if (image.length > 1) {
            for (let i = 0; i < image.length; i++) {
                if (image[i].type.split("/")[0] !== "image") {
                    image = [];
                    imageValue.value = "";
                    alert("Multiple file posting is only available to images.");
                    return;
                }
            }
        }

        if (image.length > 4) {
            image = [];
            imageValue.value = "";
            alert("You can only post 4 images max.");
        }else if (Array.from(image).filter((x) => {
            if (x.type.split("/")[0] !== "image"){
                return x.size > 40000000
            }else{
                return x.size > 8000000
            }
        }).length > 0){
            image = [];
            imageValue.value = "";
            alert("One of files exceeded the maximum file size limit");
            return;
        }

        filePreview = Array.from(image).map((x) => {
            return { type: x.type.split("/")[0], url: URL.createObjectURL(x) };
        });
    }
</script>

<div class="mediaContainer">
    <label for="fileInput">Upload files</label>
    <input
        type="file"
        id="fileInput"
        multiple
        bind:this={imageValue}
        bind:files={image}
        accept="video/*, image/*, audio/*"
        on:change={inputValidation}
    />

    <div class="mediaDisplay">
        {#each filePreview as preview}
            {#if preview.type === "image"}
                <div class="mediaImage">
                    <img src={preview.url} alt="imagePreview" />
                </div>
            {:else if preview.type === "video"}
                <div class="mediaVideo">
                    <video src={preview.url} controls>
                        <track kind="captions" />
                    </video>
                </div>
            {:else if preview.type === "audio"}
                <audio controls src={preview.url} type={preview.type} />
            {/if}
        {/each}
    </div>
</div>
<style>

    .mediaContainer{
        margin-top:10px;
    }

    .mediaDisplay {
        display: flex;
        justify-content: center;
    }

    .mediaImage {
        width: 200px;
        height: 200px;
        overflow: hidden;
        margin: 10px 10px;
    }

    .mediaVideo{
        height: 200px;
        width: auto;
    }

    video{
        height: 100%;
        width: auto;
        border-radius: 5px;
    }

    img {
        object-fit: cover;
        width: 100%;
        height: 200px;
        border-radius: 5px;
    }
    
    input[type="file"]::file-selector-button {
        display: none;
    }
    input[type="file"] {
        display: none;
    }

    label {
        background-color: #50c0cb;
        color: #252c2c;
        font-family:"Open Sans";  
        font-size: 12px;
        font-weight: bold;
        border: none;
        padding: 5px 15px;
        border-radius: 15px; 
        margin-left: 5px;
    }

    label:hover {
        background-color: #50c0cb; /*#a7dfe5;*/
        opacity: 0.5;
    }
</style>
