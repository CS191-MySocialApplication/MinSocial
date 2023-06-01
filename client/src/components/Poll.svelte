<script>
    import { each } from "svelte/internal";

    export let choices = [
        "", 
        ""
    ];
    
    // BAD CODE
    let unused_choices = [
        "", 
        ""
    ];

    export let option = true;
    
    export let deadline;

    function addChoices(){
        choices = choices.concat(unused_choices.slice(0,1));
        unused_choices = unused_choices.slice(1);
    }

    function removeChoices(){
        if(choices.length > 2){
            unused_choices = choices.slice(-1).concat(unused_choices);
            choices = choices.slice(0,-1);
        }
    }

    function selectOption(){
        option = !option;
    }

</script>

<div id="containerPoll">
    <ul>
        {#each choices as choice, i}
            <li><input
                placeholder="Choice {i+1}"
                bind:value={choice}
            ></li>
        {/each}
    </ul>

    <ul>
        <button type="button" on:click={addChoices}>+</button>
        <button type="button" on:click={removeChoices}>-</button>
        </ul>
    <ul>
        <button type="button" on:click={selectOption}>
            Mode:
            {#if option}
                Multiple Choices
            {:else}
                Single Choice
            {/if}
        </button>
    </ul>
    <div>   
        <span> Deadline </span>
        <select bind:value={deadline}>
            <option value="300">5 minutes</option>
            <option value="1800">30 minutes</option>
            <option value="3600">1 hour</option>
            <option value="21600">6 hours</option>
            <option value="43200">12 hours</option>
            <option value="86400">1 day</option>
            <option value="259200">3 days</option>
            <option value="604800">7 days</option>
        </select>
        
    </div>
</div>