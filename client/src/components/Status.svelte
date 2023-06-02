<script>
    import PollStatus from './PollStatus.svelte';

    import {link} from 'svelte-spa-router';

    export let status;

    let showContent = false;

    function changeattachmentType(){
        if(attachmentType == "none"){
            attachmentType = "media";
        }else if(attachmentType == "media"){
            attachmentType = "poll";
        }else{
            attachmentType = "none"
        }
    }
</script>



    <!--Change href to mentions thread-->
    <div class="post">
      <p id="source" class="imptDetails">{status["account"]["username"]}</p>
      
      <span id="dateTime">{status["created_at"]}</span><br />
      
      
      {#if status["sensitive"]}
        <p id="spoilerText">{status["spoiler_text"]} <button type="button" id="contentToggle" on:click={()=>{showContent = !showContent}}> {#if showContent} Hide {:else} Show {/if} Content</button></p>
      {/if}
      
        
        
      {#if !status["sensitive"] || (status["sensitive"] && showContent)}
      <a href="/toot/{status["id"]}" use:link>
        <p>{@html status["content"]}</p>
      </a>
        {#if status["media_attachments"].length !== 0}
        
        {#each status["media_attachments"] as media}
          {#if media["type"] == "image"}
          <div id="mediaContainer">
            <a href="{media["url"]}" id="mediaAttachment" target="_blank" rel="noreferrer noopener">
              <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
            </a>
          </div>

          {:else if media["type"] == "audio"}
          <div id="mediaContainer">
            
          <audio controls>
            <source src={media["url"]} type="audio/mp3">
          </audio>
          </div>
          {:else if media["type"] == "video"}
          <div id="mediaContainer">
            <a href="{media["url"]}" id="mediaAttachment" target="_blank" rel="noreferrer noopener" >
            <video controls id="mediaVideo">
              <track kind="captions">
              <!--maybe add other video formats?-->
              <source src="{media["url"]}" type="video/mp4">
            </video>
          </a>
        </div>
          {:else}
          <div id="mediaContainer">
            <a href="{media["url"]}" id="mediaAttachment" target="_blank" rel="noreferrer noopener" >
              <video autoplay playsinline loop controls id="mediaGIF">
                <track kind="captions">
                <!--maybe add other gifv formats?-->
                <source src="{media["url"]}" type="video/mp4">
              </video>
            </a>
          </div>
          {/if}
        {/each}

        {:else if status["poll"] !== null}
            <!-- {console.log(status["poll"])} -->

            <PollStatus poll={status["poll"]}/>
            
        {/if}
      {/if}
      
    </div>

  <style>

  .post {
    display: block;
    text-decoration: none;
    color: inherit;
    border-style: none none solid none;
    border-color: #50c0cb;
    border-width: 1px;
    padding: 0px 14px;
  }
  .post:hover {
    background-color: #3c4444;
    fill-opacity: 0.5;
  }

  a:hover {
    text-decoration: underline;
  }
  .imptDetails {
    margin-bottom: 0;
  }

  #mediaImage, #mediaVideo, #mediaGIF {
    cursor: zoom-in;
    object-fit: cover;
    position: relative;
    width: 100%;
    /*height: 100%;*/
  }

  #mediaAttachment{
    box-sizing: border-box;
    object-fit: contain;
    overflow: hidden;
    position: relative;
    display: flex;
    justify-content: center;
    aspect-ratio: 3/2;
    border: 0;
    border-radius: 15px;
    width: 50%;
    object-position: 50% 50%;
    
  }

  #mediaContainer {
    display: flex;
    justify-content: center;
    margin-bottom: 14px;

  }

  #contentToggle {
    margin-left: 14px;
    background-color: #50c0cb;
    color: #252c2c;
    font-family:"Open Sans";  
    font-size: 10px;
    font-weight: bold;
    border: none;
    padding: 2px 8px;
    border-radius: 15px; 
  }

  #contentToggle:hover {
        background-color: #50c0cb; /*#a7dfe5;*/
        opacity: 0.5;
 
    }

  #spoilerText {
    padding: 0;
    display: flex;
  }

  </style>