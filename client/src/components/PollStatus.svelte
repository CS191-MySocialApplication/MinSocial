<script>

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

</script>

<div>
    
    {#await poll}
        Loading Poll
    {:then poll}
        {#if poll["voted"]}
            <ul>
                {#each poll["options"] as choice}
                    <li>{choice["title"]} - Votes: {choice["votes_count"]}</li>
                {/each}
            </ul>
            Total Votes - {poll["votes_count"]}
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

    
</div>