<script>
    export let imageValue;
    export let image;
</script>

<div id="containerFile">
    <input type="file" multiple bind:value={imageValue} bind:files={image}>
</div>