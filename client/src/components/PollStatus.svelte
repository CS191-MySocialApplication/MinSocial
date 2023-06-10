<script>
    import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
    import { onMount } from 'svelte';
    import { link } from 'svelte-spa-router';

    export let poll;

    let votedOptions = [];

    async function getPoll(){
        const ACTION_URL = "/api/poll/";
        const formData = new FormData()

        formData.append("id", poll["id"])

        const res = await fetch(ACTION_URL, {
            method: 'POST',
            body: formData
        });
        poll = await res.json();
    }

    onMount(getPoll);

    async function handleOnVote(e){
        const ACTION_URL = e.target.action;
        const formData = new FormData()

        formData.append("choices", JSON.stringify(votedOptions))
        formData.append("id", poll["id"])

        let new_poll = await fetch(ACTION_URL, {
            method: 'POST',
            body: formData
        });        

        
        poll = await new_poll.json()

    }

    // To create the progress bar
	const progress = tweened(0, {
		duration: 400,
		easing: cubicOut
	});

</script>

<div class="parent">

    {#await poll}
        Loading Poll
    {:then poll}
        {#if poll["voted"]}
            <div class="poll">
                {#each poll["options"] as choice}
                    {#if poll["votes_count"] === 0}
                        <div class="pollItem"> 
                            <span class="percentage"> 0% <span> {choice["title"]}
                        </div>
                        <progress value={0}></progress>
                    {:else}
                        <div class="pollItem">
                            <span class="percentage">{Math.trunc(choice["votes_count"]/poll["votes_count"] *100)}% </span>
                            {choice["title"]} 
                        </div>
                        <progress value={(choice["votes_count"]/poll["votes_count"]).toFixed(2)}></progress>
                    {/if}
                {/each}
                {#if poll["votes_count"] === 1}
                    <span class="totalVotes"> {poll["votes_count"]} vote </span>
                {:else}
                    <span class="totalVotes"> {poll["votes_count"]} votes </span>
                {/if}
            </div>

        {:else}
            <div class="pollForm" on:click|stopPropagation on:keypress={()=>{}}>
                <form action="/api/poll/vote" on:submit|preventDefault|once={handleOnVote}>
                    {#each poll["options"] as choice, i}
                        <div class="pollFormItems">
                            {#if poll["multiple"]}
                                <input type="checkbox" class="box" bind:group={votedOptions} name="vote" value={i}/>
                            {:else}
                                <input type="radio" class="box" bind:group={votedOptions} name="vote" value={i}/>
                            {/if}
                            {choice["title"]}
                        </div>
                    {/each}
                    <input id="submitButton" type="submit" value="Vote">
                </form>
            </div>
        {/if}
        
    {:catch error}
        {error}
    {/await}

</div>

<style>
    .parent {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: center;
        margin-bottom: 14px;
    }
    .parent:hover .poll {
        background-color: #252c2c;
    }
    .parent:hover .pollForm {
        background-color: #252c2c;
    }
    .poll {
        display: flex;
        flex-direction: column;
        width: 70%;
        background-color: #3c4444;
        border-radius: 15px;
        padding: 10px 10px;
        margin: 14px;
    }
    progress {
        width: 100%;
        height: 10px;
        border-radius: 5px;
        background-color: #808080;
        border-color: #808080;
    }
    progress::-moz-progress-bar { background: #50c0cb; border-radius: 5px; border-color: #50c0cb}
    progress::-webkit-progress-bar { border-radius: 5px; background: #808080; height: 10px}
    progress::-webkit-progress-value { background: #50c0cb; border-radius: 5px; height: 10px}
    .pollItem {
        display: block;
        font-size: 14px;
        margin: 5px 0px;
        font-weight: 300;
    }
    .percentage {
        font-size: 13px;
        margin-right: 2px;
        font-weight: 600;
    }
    .totalVotes {
        margin-top: 10px;
        font-size: 12px;
    }
    .pollForm {
        width: 70%;
        background-color: #3c4444;
        border-radius: 15px;
        padding: 10px 10px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        font-size: 14px;
        margin: 14px;
    }
    input[type="submit"] {
        background-color: #50c0cb;
        width: 15%;
        height: 24px;
        margin-top: 20px;
        margin-bottom: 5px;
        border: none;
        border-radius: 15px; 
        font-weight: 600;
    }
    input[type="submit"]:hover {
        opacity: 0.5;
    }
    .pollFormItems {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 2px;
    }
    input[type="checkbox"], input[type="radio"] {
        appearance: none;
    }
    input[type="radio"] {
        border-radius: 100px;
    }
    .box {
        width: 15px;
        height: 15px;
        background-color: #3c4444;
        border: 1px solid #ffffff;
    }
    .box:hover {
        border: 1px solid #50c0cb;
    }
    .box:checked {
        background-color: #50c0cb;
	    opacity: 0.8;
        border: 1px solid #50c0cb;
    }
    /* Desktop */
    @media screen and (hover: hover) {
        .poll, .pollForm {
            min-width: 150px;
        }
        #submitButton {
            min-width: 60px;
        }
    }
    /*Touch screen*/
    @media screen and (hover: none) {
        input[type="submit"] {
            min-width: 75px;
        }
        .poll, .pollForm {
            min-width: 100px;
        }
    }
</style>