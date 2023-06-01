<script>

    import {replace} from 'svelte-spa-router';

    import Poll from "./Poll.svelte";
    import MediaInput from "./MediaInput.svelte"

    let attachmentType = "none";

    let statusText;
    let image;
    let imageValue;
    
    let pollChoices;
    let pollOption;
    let pollDeadline;

    let contentWarningToggle = false;
    let contentWarningText = "";

    const handleOnSubmit = e => {
        const ACTION_URL = e.target.action;
        const formData = new FormData()

        formData.append("attachmentType", attachmentType)
        formData.append("text", statusText);
        formData.append("contentWarning", contentWarningToggle);
        
        if(contentWarningToggle){
            formData.append("contentWarningText", contentWarningText)
        }

        if(attachmentType == "poll"){
            formData.append("choices", JSON.stringify(pollChoices));
            formData.append("option", pollOption);
            formData.append("deadline", pollDeadline);
        }else if(attachmentType == "media"){
            for(let i = 0; i < image.length; i++){
                formData.append("images_"+i, image[i]);
            }
        }

        statusText = "";

        contentWarningToggle = false;
        contentWarningText = "";
        
        imageValue = "";
        image = "";
        
        pollChoices = [
            "", ""
        ];

        pollOption = true;
        deadline = 300;

        fetch(ACTION_URL, {
            method: 'POST',
            body: formData
        });        

    }

    function changeattachmentType(){
        if(attachmentType == "none"){
            attachmentType = "media";
        }else if(attachmentType == "media"){
            attachmentType = "poll";
        }else{
            attachmentType = "none"
        }
    }

    function changeCW(){
        contentWarningToggle = ! contentWarningToggle;
    }
</script>


<div id="postContainer">
    <form action="/api/compose/" on:submit|preventDefault={handleOnSubmit} enctype="multipart/form-data">
        <div id="containerTitle">
            <span>
                Write your thoughts
            </span>
        </div>

        <div id="containerArea">
            <textarea id="text" name="text" rows="3" bind:value={statusText}/>
        </div>

        <br>
        <button type="button" on:click={changeCW}> {#if !contentWarningToggle} Enable {:else} Disable {/if} Content Warning </button>
        {#if contentWarningToggle}
            <input type="text" bind:value={contentWarningText} /> 
        {/if}
        <br>

        <button type="button" on:click={changeattachmentType}>Attachment: {attachmentType}</button>

        {#if attachmentType=="media"}

            <MediaInput bind:imageValue={imageValue} bind:image={image}/>

        {:else if attachmentType=="poll"}

            <Poll bind:choices={pollChoices} bind:option={pollOption} bind:deadline={pollDeadline}/>

        {/if}

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
    #containerArea{
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