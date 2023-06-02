<script>

    import {replace} from 'svelte-spa-router';

    import Poll from "./Poll.svelte";
    import MediaInput from "./MediaInput.svelte"

    //Change to svg!
    import cwEnabled from "../../public/contentWarningEnabled.png";
    import cwDisabled from "../../public/contentWarningDisabled.png";
    import pollEnabled from "../../public/pollEnabled.png";
    import pollDisabled from "../../public/pollDisabled.png";


    let attachmentType = "none";

    let statusText;
    let image;
    let imageValue;
    
    let pollChoices;
    let pollOption;
    let pollDeadline;
    let pollToggle = false;

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
        pollDeadline = 300;

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

    function showPoll(){
        pollToggle = ! pollToggle;
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
            <MediaInput bind:imageValue={imageValue} bind:image={image}/>
            <button type="button" id="displayPoll" on:click={showPoll}> 
                {#if !pollToggle}
                <img src={pollDisabled} alt="pollEnable"  />
                {:else}
                    <img src={pollEnabled} alt="pollEnable"  />
                {/if}
                
                
            </button>
            
            <button type="button" id="cwToggle" on:click={changeCW}> 
                {#if !contentWarningToggle}
                <img src={cwDisabled} alt="cwEnable"  />
                {:else}
                <img src={cwEnabled} alt="cwDisable" />
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
                    <Poll bind:choices={pollChoices} bind:option={pollOption} bind:deadline={pollDeadline}/>    
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
    img{
        height: 30px;
        width:30px;
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
</style>