<script>
	import Header from "../components/Header.svelte";
	import Postform from "../components/postform.svelte";
	import Navbar_desktop from "../components/Navbar_desktop.svelte"
	import Navbar_mobile from "../components/Navbar_mobile.svelte"
    import { each } from "svelte/internal";

    import UnclickedMentions from '../../public/unclicked_mentions.png';
    import HoverUnclickedMentions from '../../public/hover_unclicked_mentions.png';
    import ClickedDM from '../../public/clicked_dm.png';
    import HoverClickedDM from '../../public/hover_clicked_dm.png';
    import UnclickedSettings from '../../public/unclicked_settings.png';
    import HoverUnclickedSettings from '../../public/hover_unclicked_settings.png';

	async function getMessageContent(){

		let res = await fetch('/api/messages');
		let text = await res.json();

		if (res.ok){
			return text;
		}else{
			throw new Error(text);
		}

	}

	let auth_promise = getMessageContent();

</script>


<div class="desktop-format">
	<Navbar_desktop
	mentions={UnclickedMentions}
	hoverMentions={HoverUnclickedMentions}
	dm={ClickedDM}
	hoverDM={HoverClickedDM}
	settings={UnclickedSettings}
	hoverSettings={HoverUnclickedSettings}
	class = "navbar"/>
	<div class="content">
		<Header title="Messages"/>
		<main>

			{#await auth_promise}
		
				<p>Waiting...</p>

			{:then conversations}
				
				{#each conversations as conversation}
					<div class="conversation">
						<span id="source" class="impt-details">{conversation["source"]} |</span> 
						<span id="username" class="impt-details">{conversation["author"]["username"]}</span><br/>
						<span id="datetime">{conversation["createdTime"]}</span><br/>
						<p>{conversation["content"]}</p><br/><br/>
					</div>
				{/each}
			{:catch error}
				<p style="color: red">{error.messages}</p>
			{/await}


		</main>
	</div>
	<Navbar_mobile />
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