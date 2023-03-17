<script>

	import Postform from "../components/postform.svelte";

	async function getHomeContent(){

		let res = await fetch('/api/home');
		let text = await res.json();

		if (res.ok){
			return text;
		}else{
			throw new Error(text);
		}

	}

	let auth_promise = getHomeContent();

</script>

<main>

	<Postform/>

	{#await auth_promise}
		<p>waiting...</p>
	{:then timeline}
        {#each timeline as status}

            <div>
                <span>Source: {status["source"]}</span><br/>
                <span>{status["author"]["username"]}</span><br/>
                <span>{status["createdTime"]}</span><br/>
                <p>{status["content"]}</p><br/><br/>
            </div>

        {/each}
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}

</main>

<style>

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

</style>