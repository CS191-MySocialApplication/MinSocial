<script>
    import { each } from "svelte/internal";

    export let choices = [
        "", 
        ""
    ];
    
    // BAD CODE
    export let unused_choices = [
        "", 
        ""
    ];

    export let deadlineChoices;

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
<div id="centering">

    
<div id="containerPoll">
    <div id="containerTitle">
        <span>
            Create your own poll
        </span>
    </div>
    <ul>
        {#each choices as choice, i}
            <div id="liSeparator">
            <li><input
                placeholder="Choice {i+1}" 
                bind:value={choice}
            ></li>
            </div>
        {/each}
    </ul>
    

    <div id="separator">
        <div id="alterContainer">
        <button type="button" id="alterButton" on:click={addChoices}>Add</button>
        
        <button type="button" id="alterButton" on:click={removeChoices}>Remove</button>
        
        </div>
    </div>
    <div id="separator">
        <div id="modeContainer">
    <button type="button" id="modeButton" on:click={selectOption}>
        
        Mode:&ensp;
        {#if option}
            Multiple Choices
        {:else}
            Single Choice
        {/if}
    
    </button>
</div>
    </div>
   
   
    <div id="selectContainer">   
        <select bind:value={deadline}>
            {#each deadlineChoices as deadlineChoice}
                <option value={deadlineChoice}>{deadlineChoice.text}</option>
            {/each}
        </select>
        
    </div>
</div>
</div>
<style>

    ul {
        list-style-type: none;
        padding-inline-start: 0px;
        margin-block-start: 0px;
        margin-block-end: 10px;
    }

    input {
        /*color: #252c2c;*/
        background-color: #acacac;
        font-family:"Open Sans";  
        font-size: 12px;   
        border-width: 0;
        resize: none;
        outline: none;
        padding: 5px;
        width:100%;
        border-radius:5px;
        
    }
    
    li {
        display:flex;
        width:100%;
    }
    #liSeparator {
        display:flex;
        justify-content:center;
        width:100%;
        align-items:center;
        margin-top:4px;    
    }

    #alterContainer {
        display: flex;
        justify-content:space-between;
        width: 100%;
    }

    #modeContainer{
        display: flex;
        justify-content:center;
        width: 100%;
    }
    #separator {
        display:flex;
        justify-content:center;
        width:100%;
        margin-bottom:10px;
    }

    #selectContainer {
        display:flex;
        justify-content:center;
        width:100%;
    }

    #centering {
        display:flex;
        justify-content:center;
        width:100%;
    }
    button {
        padding: 5px 15px;
        border-radius: 15px; 
        border: none;
        color: white;
        background-color: #3c4444;
        font-family:"Open Sans";  
        font-size: 12px;
        padding: 3px 10px;   
    }

    #modeButton {
        width: 100%;
    }

    #alterButton {
        width: 49%;
    }

    select {
        background-color: #3c4444;
        color:white;
        font-family: "Open Sans";
        font-size: 12px;
        border-width: 0;
        resize: none;
        outline: none;
        padding: 3px;
        width: 100%;
        border-radius:5px;
    }

    #containerPoll {
        border-radius: 15px;
        background-color: #252c2c;
        padding: 4px 10px 10px 10px;
        width: 50%;
        margin: 0px 0px  0px 0px;
    }

    #containerTitle{
        font-size: 14px;
        padding: 10px 15px;
        font-weight: bold;
        color: white;
        display: flex;
        justify-content: center;

    }

    ::-webkit-input-placeholder {
        color: #3c4444 !important; 
    }
</style>