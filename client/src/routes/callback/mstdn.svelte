<script>

    import {onMount} from 'svelte';

    let state = "";
    let code = "";

    onMount(async() => {
        const urlSearchParams = new URLSearchParams(window.location.search);
        const param = Object.fromEntries(urlSearchParams.entries());

        const res = await fetch('/auth/mstdn/callback?' + new URLSearchParams({
            code: param["code"]
        }));
        let data = await res.json();

        if(res.ok){
            code = data["status"];
            window.location.replace("/home")
        }

    })

</script>

<main>

    <p>{code}</p>

	<!-- {#await auth_promise}
		<p>waiting...</p>
	{:then url}
		<p>
			<a href={url}>Log-in Using Twitter</a>
		</p>
	{:catch error}
		<p style="color: red">{error.message}</p>
	{/await} -->

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