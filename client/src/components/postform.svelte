<script>

    let statusText;

    const handleOnSubmit = e => {
        const ACTION_URL = e.target.action;

        const formData = new FormData(e.target)

        const data = new URLSearchParams()
		for (let field of formData) {
			const [key, value] = field
			data.append(key, value)
		}

        statusText = "";

        fetch(ACTION_URL, {
            method: 'POST',
            body: data
        });

        
    }
</script>


<div id="postcontainer">
    <form action="/api/compose" on:submit|preventDefault={handleOnSubmit}>
        <div id="containertitle">
            <p>
                Write your thoughts
            </p>
        </div>

        <div id="containerarea">
            <textarea id="text" name="text" rows="5" cols="33" bind:value={statusText}/> <br> 
        </div>

        <div id="containerfooter">
            <div>

            </div>
            <input id="submitbutton" type="submit">
        </div>

    </form>
</div>

<style>
    #postcontainer {
        display: flex;
        border-width: 2px;
        border-style: solid;
        border-color: black;
        border-radius: 25px;
        margin: 0 auto;
    }

    #containertitle{
        border-bottom: 2px;
        border-bottom-style: solid;
        border-color: black;
        padding: 0px 10px; 
    }

    #containerfooter{
        display:flex;
        justify-content: space-between;
        border-top: 2px;
        border-top-style: solid;
        border-color: black;
        padding: 5px 10px; 
    }

</style>