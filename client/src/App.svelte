<script>
	import "@fontsource/open-sans"

	async function getMstdnAuthLink(){

		let res = await fetch('/auth/mstdn');
		let text = await res.text();

		if (res.ok){
			let auth_json = JSON.parse(text)
			return auth_json["auth_url"];
		} else{
			throw new Error(text);
		}
	}

	let mstdn_auth_promise = getMstdnAuthLink();

</script>

<main>
	{#await mstdn_auth_promise}
		<p>waiting...</p>
	{:then url}
		<p>
			<a href={url}>Log-in Using Mastodon</a>
		</p>
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</main>

<style>
	a {
		font-family: "Open Sans";
	}
</style>