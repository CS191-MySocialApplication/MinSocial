<script>

    import {replace} from 'svelte-spa-router';
    import { createEventDispatcher } from 'svelte';

    import Poll from "./Poll.svelte";
    import MediaInput from "./MediaInput.svelte"

    //Change to svg!
    import ContentWarning from "../../public/contentWarning.svelte";
    import PollIcon from "../../public/poll.svelte";
    import Attachment from "../../public/attachment.svelte";

    let attachmentType = "none";

    let statusText = "";
    let image = [];
    let imageValue;
    let filePreview;
    let mediaToggle = false;
    
    let pollChoices;
    let pollUnusedChoices;
    let pollOption;
    let deadlineChoices = [
        {value: 300, text: "5 minutes"},
        {value: 1800, text: "30 minutes"},
        {value: 3600, text: "1 hour"},
        {value: 21600, text: "6 hours"},
        {value: 43200, text: "12 hours"},
        {value: 86400, text: "1 day"},
        {value: 259200, text: "3 days"},
        {value: 604800, text: "7 days"}
    ]

    let pollDeadline = deadlineChoices[0];
    let pollToggle = false;

    let contentWarningToggle = false;
    let contentWarningText = "";

    const dispatch = createEventDispatcher();

    async function handleOnSubmit(e){
        const ACTION_URL = e.target.action;
        const formData = new FormData()

        if(!mediaToggle && statusText === ""){
            alert("Status must have text");
            return
        }else if(mediaToggle && image.length == 0){
            alert("Status does not contain anything")
            return
        }

        if (pollToggle && pollChoices.filter(x => x === "").length !== 0){
            alert("There should be no empty poll choices");
            return
        } else if(pollToggle && (new Set(pollChoices)).size !== pollChoices.length){
            alert("All poll choices should be unique");
            return
        }

        formData.append("text", statusText);

        formData.append("contentWarning", contentWarningToggle);
        
        if(contentWarningToggle){
            formData.append("contentWarningText", contentWarningText)
        }

        if(pollToggle){
            formData.append("attachmentType", "poll")
            formData.append("choices", JSON.stringify(pollChoices));
            formData.append("option", pollOption);
            formData.append("deadline", pollDeadline.value);
        }else if(mediaToggle){
            formData.append("attachmentType", "media")
            for(let i = 0; i < image.length; i++){
                formData.append("images_"+i, image[i]);
            }
        }else{
            formData.append("attachmentType", "none")
        }

        statusText = "";

        contentWarningToggle = false;
        contentWarningText = "";
        
        if(imageValue){
            imageValue.value = "";
        }
        image = null;
        filePreview = [];
        
        pollChoices = [
            "", ""
        ];

        pollUnusedChoices = [
            "", ""
        ];

        pollOption = true;
        pollDeadline = deadlineChoices[0];

        await fetch(ACTION_URL, {
            method: 'POST',
            body: formData
        });


        dispatch('postSubmit');

    }

    function toggleMedia(){
        if(!mediaToggle){
            pollToggle = false;
            mediaToggle = true;
        }else{
            mediaToggle = false;
        }
    }

    function togglePoll(){
        if(!pollToggle){
            mediaToggle = false;
            pollToggle = true;
        }else{
            pollToggle = false;
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

        <div class="attachments">
            
            <button type="button" id="displayMedia" on:click={toggleMedia}> 
            {#if !mediaToggle}
                <div class="disabled">
                    <Attachment/>
                </div>
            {:else}
                <div class="enabled">
                    <Attachment/>
                </div>
            {/if}
            </button>

            <button type="button" id="displayPoll" on:click={togglePoll}> 
            {#if !pollToggle}
                <div class="disabled">
                    <PollIcon/>
                </div>
            {:else}
                <div class="enabled">
                    <PollIcon/>
                </div>
            {/if}
            </button>
            
            <button type="button" id="cwToggle" on:click={changeCW}> 
                {#if !contentWarningToggle}
                    <div class="disabled">
                        <ContentWarning/>
                    </div>
                {:else}
                    <div class="enabled">
                        <ContentWarning/>
                    </div>
                {/if}
            </button>
            <div id="containerCW">
                {#if contentWarningToggle}
                    <input type="text" id="cwText" placeholder="Content Warning..." bind:value={contentWarningText} /> 
                {/if}
            </div>
        </div>
        
            
        <div>
            {#if pollToggle}
                <Poll bind:choices={pollChoices} bind:option={pollOption} bind:deadline={pollDeadline} deadlineChoices={deadlineChoices} unused_choices={pollUnusedChoices}/>    
            {/if}
            {#if mediaToggle}
                <MediaInput bind:imageValue={imageValue} bind:image={image} bind:filePreview={filePreview}/>
            {/if}
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
    #containerArea{
        display: flex;
        margin-bottom:4px;
    }

    .attachments {
        display: flex;
        margin-bottom: 20px;
    }
    textarea {
        color: white;
        background-color: #252c2c;
        font-family:"Open Sans";  
        font-size: 12px;   
        width: 100%;
        border-width: 0;
        resize: none;
        outline: none;
        padding: 15px;
        border-radius:5px;
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
    button {
        background-color: transparent;
        border: none;    
        margin-right: 4px;
        height:30px;
        width:30px;
        padding: 0px;
        border-radius:5px;
    }
    
    #cwText {
        color: white;
        background-color: #252c2c;
        font-family:"Open Sans";  
        font-size: 12px;   
        width: 100%;
        border-width: 0;
        resize: none;
        outline: none;
        padding: 5px;
        margin-left: 0;
        margin-right: 0;
        border-radius:5px;
    }

    button:hover{
        background-color: #252c2c;
        /*opacity: 0.5;*/
    }

    #containerCW {
        width: 100%;
        display:flex;
    }

    ::placeholder {
        color: #acacac;
    }

    .enabled {
        width: 30px;
        height: 30px;
        fill: #ffffff;
    }
    .disabled {
        width: 30px;
        height: 30px;
        fill:#acacac;
    }
</style>