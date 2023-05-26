<script>
    export let label;
    export let value;
    let checked = false; // Replies are not displayed by default

    function handleClick(e){
        const target = e.target;
        const state = target.getAttribute("aria-checked");
        checked = state === 'true' ? false : true;
        value = checked === true ? 'flex' : 'none';
    }
</script>

<main>
    <div class="slider">
        <span id="sliderToggle">{label}</span>
        <button
            role="switch"
            aria-checked={checked}
            aria-labelledby="sliderToggle"
          on:click={handleClick}></button>  
    </div>
</main>

<style>
    .slider {
        display: flex;
        align-items: center;
    }

    @media screen and (hover: none) {
        .slider {
            width: 150px;
            padding-right: 16px;
        }
    }
    .slider button {
        width: 3em;
        height: 1.6em;
        position: relative;
        margin: 0 0 0 0.7em;
        background-color: #3C4444;
        border: none;
        border-radius: 1.5em;
        box-shadow: 0px 0px 0px 2px #36676c;
    }
    .slider button::before {
        content: '';
        position: absolute;
        width: 1.3em;
        height: 1.3em;
        background: #fff;
        top: 0.18em;
        right: 1.5em;
        transition: transform 0.3s;
        border-radius: 100%;
    }
    .slider button[aria-checked='true'] {
      background-color: #50C0CB;
    }
    .slider button[aria-checked='true']::before{
        transform: translateX(1.3em);
        transition: transform 0.3s;
    }
    .slider button:focus {
        border-radius: 1.5em;
    }
</style>