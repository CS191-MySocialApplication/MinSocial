<script>

  import {replace} from 'svelte-spa-router';

  import Poll from "./Poll.svelte";
  import MediaInput from "./MediaInput.svelte"

  import { get } from 'svelte/store';
  import my_store from "../sdk/store.ts";
  import ContentWarning from "../../public/contentWarning.svelte";
    import PollIcon from "../../public/poll.svelte";
    import Attachment from "../../public/attachment.svelte";
  const latestID = get(my_store);

  console.log("latestID: ")
  console.log(latestID)

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

  let sendID = latestID;

  const handleOnSubmit = e => {
      const ACTION_URL = e.target.action;
      const formData = new FormData()

      formData.append("attachmentType", attachmentType)
      formData.append("text", statusText);
      formData.append("contentWarning", contentWarningToggle);
      formData.append("sendID", sendID);
      
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
<main>
<div id="postContainer">


  <form action="/api/composeMsg/" on:submit|preventDefault={handleOnSubmit} enctype="multipart/form-data">
    {#if pollToggle}
        <div id="pollContainer">
            <Poll bind:choices={pollChoices} bind:option={pollOption} bind:deadline={pollDeadline} deadlineChoices={deadlineChoices} unused_choices={pollUnusedChoices}/>    
        </div>
    {/if}
    {#if mediaToggle}
        <div id="mediaContainer">
            <MediaInput bind:imageValue={imageValue} bind:image={image} bind:filePreview={filePreview}/>
        </div>
    {/if}
    
    
    {#if contentWarningToggle}
    <div id="containerCW">
        <input type="text" id="cwText" placeholder="Content Warning..." bind:value={contentWarningText} /> 
    </div>
    {/if}
    <div id="flexContainer">
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
        
    </div>
    <div id="containerArea">
        <textarea id="text" name="text" rows=1 bind:value={statusText}/>
    </div>
    <div id="send">
        <input id="submitButton" type="submit" value="">
    </div>
</div>
</form>
</div>
</main>
<style>

    main {
        position: fixed;
        z-index: 1;
        width: 100%;
        font-family: "Open Sans", "sans-serif";
        background-color: #3c4444;/*#252c2c;*/
        border-top: 3px solid #50c0cb;
        color: white;
        margin: 0px;
        bottom: 0;
    }
    #flexContainer {
        display:flex;
        align-items:center;
        padding: 14px;
        width: 85%;
        justify-content: space-between;
        margin-left:8px;
    }
    #mediaContainer, #pollContainer{
        display:flex;
        padding: 14px 14px 0px 14px;
        width: 100%;
        margin-left:8px;
    }
    #containerCW {
        width: 100%;
        display:flex;
        padding: 14px 14px 0px 14px;
        justify-content: center;
        margin-left:8px;
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
    form {
        width: 100%;    
    }

    #containerArea{
        display: flex;
        width: 85%;
 
    }
    .attachments {
        display: flex;
        margin-right: 14px;
    }
    textarea {
        color: white;
        background-color: #252c2c;
        font-family:"Open Sans";  
        font-size: 12px;   
        border-width: 0;
        resize: none;
        outline: none;
        padding: 10px;
        border-radius:5px;
        width:100%
    }
    button {
        background-color: transparent;
        border: none;    
        height:30px;
        width:30px;
        padding: 0px;
        border-radius:5px;
    }

    button:hover{
        background-color: #252c2c;;
        /*opacity: 0.5;*/
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
    #send {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-left: 14px;
    }
    input[type="submit"] {
        background: url('../../public/send.svg');
        border:none; 
        width: 30px;
        height: 30px;
        background-size:95% 95%;
        border-radius: 5px;
        background-repeat: none;
        padding: 0px;
    }

    input[type="submit"]:hover {
        background-color:#252c2c;;
    }
    ::placeholder {
        color: #acacac;
    }
    @media screen and (min-width: 516px) and (max-width: 714px) and (hover: hover) {
        #flexContainer {
            width: 83%;
        }
    }
    @media screen and (max-width: 515px) and (hover: hover) {
        #flexContainer {
            width: 81%;
        }
    }
    @media screen and (hover: none) {  
        main {
            bottom: 80px;
        }
        #flexContainer {
            width: 100%;
            margin-left: 0;
        }
        #send {
            margin-left: 12px;
            margin-right: 24px;
        }
        .attachments {
            margin-right: 12px;
        }
    }    
    
</style>