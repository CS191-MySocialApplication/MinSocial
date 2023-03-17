<script>
	import Header from "../components/Header.svelte";
	import Postform from "../components/postform.svelte";
	import Navbar_desktop from "../components/Navbar_desktop.svelte"

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
<div class="desktop-format">
	<Navbar_desktop />
	<div class="content">
		<Header />
		<main>

			<Postform/>

			{#await auth_promise}
				<p>waiting...</p>
			{:then timeline}
				{#each timeline as status}

					<div class="post">
						<span id="source" class="impt-details">{status["source"]} |</span> 
						<span id="username" class="impt-details">{status["author"]["username"]}</span><br/>
						<span id="datetime">{status["createdTime"]}</span><br/>
						<p>{status["content"]}</p><br/><br/>
					</div>

				{/each}
			{:catch error}
				<p style="color: red">{error.message}</p>
			{/await}

		</main>
	</div>
</div>
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

	@media (max-width: 479px) {
		.desktop-format {  
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }
	}

	@media (min-width: 480px) {
		.desktop-format {
            display: flex;
            flex-direction: row;
        }
	}

</style>