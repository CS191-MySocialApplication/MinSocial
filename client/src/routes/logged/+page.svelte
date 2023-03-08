<script>

    import {onMount} from 'svelte';

    let state = "";
    let code = "";

    onMount(async() => {
        const urlSearchParams = new URLSearchParams(window.location.search);
        const param = Object.fromEntries(urlSearchParams.entries());

        const res = await fetch('/auth/twt/callback?' + new URLSearchParams({
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