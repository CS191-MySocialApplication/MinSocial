<script>

    let statusText;
    let cwText;

    const handleOnSubmit = e => {
        const ACTION_URL = e.target.action;

        const formData = new FormData(e.target)

        const data = new URLSearchParams()
		for (let field of formData) {
			const [key, value] = field
			data.append(key, value)
		}

        statusText = "";
        cwText = "";

        fetch(ACTION_URL, {
            method: 'POST',
            body: data
        });        
    }
</script>


<div id="postContainer">
    <form action="/api/compose" on:submit|preventDefault={handleOnSubmit}>
        <div id="containerTitle">
            <span>
                Write your thoughts
            </span>
        </div>

        <div id="containerArea">
            <textarea id="text" name="text" rows="3" bind:value={statusText}/>
        </div>
        <div id="containerArea">
            <textarea placeholder="Content Warning..." id="cw" name="cw" rows="1" bind:value={cwText}/>
        </div>
        <div id="containerFooter">
            <input id="submitButton" type="submit" value="Post">
        </div>

    </form>
</div>

<style>
    #postContainer {
        box-sizing: border-box;
        display: flex;
        border-radius: 15px;   
        border: solid;
        border-color:#3c4444;
        border-width:4px;
        background-color: #3c4444 ; /*#50c0cb #3c4444 #36676c;  */
        margin: 0 0 32px 0;
        width: 100%;
    }
    
    form {
        width: 100%;    
    }
    

    #containerTitle{
        /*
        border-bottom: 2px;
        border-bottom-style: solid;
        border-color: black;
        */
        font-size: 14px;
        padding: 10px 15px;
        font-weight: bold;
        color: white;
    }
    #containerArea {
        display: flex;
    }


    textarea {
        color: #acacac;
        background-color: #252c2c;
        font-family:"Open Sans";  
        font-size: 12px;   
        width: 100%;
        border-width: 0;
        resize: none;
        outline: none;
        padding: 15px;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 4px;
    }

    
    #containerFooter{
        /*
        border-top: 2px;
        border-top-style: solid;
        border-color: black;
        */
        padding: 5px 15px; 
        text-align: right;
    }

    input[type="submit"] {
        background-color: #50c0cb;
        color: #252c2c;
        font-family:"Open Sans";  
        font-size: 14px;
        font-weight: bold;
        border: none;
        padding: 5px 15px;
        border-radius: 15px; 
    }

    input[type="submit"]:hover {
        background-color: #50c0cb; /*#a7dfe5;*/
        opacity: 0.5;
 
    }
</style>