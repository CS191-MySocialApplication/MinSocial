<script>
	import "@fontsource/open-sans"

	import {replace} from 'svelte-spa-router';
	import {onMount} from 'svelte';
	import Logo from "../../public/logoLogin.svelte";

	let state = "";
	let code = "";
	
	onMount(async() => {
		
		const urlSearchParams = new URLSearchParams(window.location.search);

		let data = null;

		if(urlSearchParams.get("code")){
			const res = await fetch('/auth/mstdn/callback?' + new URLSearchParams({
				code: urlSearchParams.get("code")
			}));

			let data = await res.json();
			if(res.ok){
				code = data["status"];
				window.location.replace("/#/home")
			} else {
				window.location.replace("/")
			}
		}
	});

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
		<div class="logo">
			<Logo/>
		</div>
		<p>
			<a href={url}>Log-in Using Mastodon</a>
		</p>
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await}
</main>

<style>
	main {
  height: 100lvh;
  width: 100lvw;
  margin: 0;
  background-color: #50c0cb;
  display: flex;
	flex-direction: column;
  align-items: center;
  justify-content: center;
}
.logo {
	width: 100px;
	height: 100px;
	margin-bottom: 2%;
}
a {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  width: 265px;
  height: 60px;
  background-color: #252c2c;
  color: white;
  text-decoration: none;
  margin: 24px;
  font-family: "Open Sans";
  font-size: medium;
}/*# sourceMappingURL=styles.css.map */
</style>