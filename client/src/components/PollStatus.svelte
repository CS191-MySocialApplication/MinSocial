<script>
    import { tweened } from 'svelte/motion';
	import { cubicOut } from 'svelte/easing';
    import { onMount } from 'svelte';

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

<a class="parent" href="#/home">
    
    {#await poll}
        Loading Poll
    {:then poll}
        {#if poll["voted"]}
            <!--<ul>
                {#each poll["options"] as choice}
                    <li>{choice["title"]} - Votes: {choice["votes_count"]}</li>
                {/each}
            </ul>
            Total Votes - {poll["votes_count"]}-->

            <!---UI for polls-->
            <a class="poll" href="#/home">
                {#each poll["options"] as choice}
                    {#if poll["votes_count"] === 0}
                        <div class="pollItem"> 
                            <span class="percentage"> 0% <span> {choice["title"]}
                        </div>
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
            </a>

        {:else}
            <form action="/api/poll/vote" on:submit|preventDefault={handleOnVote}>
                {#each poll["options"] as choice, i}
                    <div>
                        {#if poll["multiple"]}
                            <input type="checkbox" bind:group={votedOptions} name="vote" value={i}/>
                        {:else}
                            <input type="radio" bind:group={votedOptions} name="vote" value={i}/>
                        {/if}
                        {choice["title"]}
                    </div>
                {/each}
                <input id="submitButton" type="submit" value="Vote">
            </form>
        {/if}
    {:catch error}
        {error}
    {/await}

</a>

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
    .poll {
        display: flex;
        flex-direction: column;
        width: 50%;
        background-color: #3c4444;
        border-radius: 15px;
        padding: 10px 10px;
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
</style>