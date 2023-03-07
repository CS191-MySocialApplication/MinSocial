<script>
	import Index from "./index.svelte"

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

<!--
	The component for the main page. Uncomment this portion to see the front-end
	This part is tentative
	<Index />
-->
<main>

	{#await auth_promise}
		<p>waiting...</p>
	{:then url}
		<p>
			<a href={url}>Log-in Using Twitter</a>
		</p>
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}

</main>

<style>
</style>