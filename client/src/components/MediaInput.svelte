<script>
    export let imageValue;
    export let image;

    function inputValidation(){
        if(image.length > 4){
            image = null;
            imageValue.value = "";
        }
    }

</script>

<div id="containerFile">
    <input type="file" multiple bind:this={imageValue} bind:files={image} on:change={inputValidation}>
</div>