<script>

	async function getAuthLink(){

		let res = await fetch('/auth/twt');
		let text = await res.text();

		if (res.ok){
			let auth_json = JSON.parse(text)
			return auth_json["auth_url"];
		}else{
			throw new Error(text);
		}

	}

	let auth_promise = getAuthLink();

</script>

<main>

	{#await auth_promise}
		<p>waiting...</p>
	{:then url}
		<p>
			<a href={url}>Log-in Using Twitter</a>
		</p>
	{:catch error}
		<p style="color: red">bla bla{error.message}</p>
	{/await}

</main>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

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

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>