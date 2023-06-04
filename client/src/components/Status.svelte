<script>
  import PollStatus from './PollStatus.svelte';

  import {link} from 'svelte-spa-router';
  import {push, pop, replace} from 'svelte-spa-router'
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
  <div class="post" on:click={()=>{push("/toot/"+status["id"]); window.location.reload(true) }} on:keypress={()=>{}}>
    <div class="statusDetails">
      <p id="username">{status["account"]["username"]} <span id="dateTime">| {status["created_at"]}</span></p>
    </div>
    
    {#if status["sensitive"]}
      <p id="spoilerText">{status["spoiler_text"]} <button type="button" id="contentToggle" 
        onclick="event.stopPropagation(); event.preventDefault; return false"
        on:click={()=>{showContent = !showContent}}> {#if showContent} Hide {:else} Show {/if} Content</button></p>
    {/if}
    
    {#if !status["sensitive"] || (status["sensitive"] && showContent)}
      <a href="/toot/{status["id"]}" use:link>
        <p id="htmlContent">{@html status["content"]}</p>
      </a>

      {#if status["media_attachments"].length == 4}
        <div id="centering">
          <div id="mediaGallery" on:click|stopPropagation on:keypress={()=>{}}> 
            {#each status["media_attachments"] as media}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener">
                    <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
                  </a>
                </div>
              {:else}
                <div id="multipleMediaContainer">
                  <div id="gifContainer">
                    <video autoplay playsinline loop muted id="mediaGIF">
                      <track kind="captions">
                      <!--maybe add other gifv formats?-->
                      <source src="{media["url"]}" type="video/mp4">
                    </video>
                  </div>
                </div>
        
              {/if}
            {/each}
          </div>
        </div>
      {:else if status["media_attachments"].length == 3}
        <div id="centering">
          <div id="mediaGallery" on:click|stopPropagation on:keypress={()=>{}}> 
            {#each status["media_attachments"] as media , index}
              {#if index == 0}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener" onclick="event.stopPropagation();">
                    <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
                  </a>
                </div>
              {:else}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <div id="gifContainer">
                    <video autoplay playsinline loop muted id="mediaGIF">
                      <track kind="captions">
                      <!--maybe add other gifv formats?-->
                      <source src="{media["url"]}" type="video/mp4">
                    </video>
                  </div>
                </div>
        
              {/if}
              {:else}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener" onclick="event.stopPropagation();">
                    <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
                  </a>
                </div>
              {:else}
                <div id="multipleMediaContainer">
                  <div id="gifContainer">
                    <video autoplay playsinline loop muted id="mediaGIF">
                      <track kind="captions">
                      <!--maybe add other gifv formats?-->
                      <source src="{media["url"]}" type="video/mp4">
                    </video>
                  </div>
                </div>
        
              {/if}

              {/if}
            {/each}
          </div>
        </div>
      {:else if status["media_attachments"].length == 2}
        <div id="centering">
          <div id="mediaGallery" on:click|stopPropagation on:keypress={()=>{}}> 
            {#each status["media_attachments"] as media}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener" onclick="event.stopPropagation();">
                    <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
                  </a>
                </div>
              {:else}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <div id="gifContainer">
                    <video autoplay playsinline loop muted id="mediaGIF">
                      <track kind="captions">
                      <!--maybe add other gifv formats?-->
                      <source src="{media["url"]}" type="video/mp4">
                    </video>
                  </div>
                </div>
        
              {/if}
            {/each}
          </div>
        </div>  
      {:else if status["media_attachments"].length == 1}
        {@const media = status["media_attachments"][0]}
        <div id="centering">
          {#if media["type"] == "image"}
            <div id="singleMediaContainer" on:click|stopPropagation on:keypress={()=>{}}>
              <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener">
                <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
              </a>
            </div>
        
          {:else if media["type"] == "audio"}

                <audio controls id="mediaAudio" on:click|stopPropagation on:keypress={()=>{}}>
                  <source src={media["url"]} type="audio/mp3">
                </audio>

          {:else if media["type"] == "video"}
            <div id="singleMediaContainer" on:click|stopPropagation on:keypress={()=>{}}>
              <div id="videoContainer">
                <video controls id="mediaVideo">
                  <track kind="captions">
                  <!--maybe add other video formats?-->
                  <source src="{media["url"]}" type="video/mp4">
                </video>
              </div>
            </div>

          {:else}
            <div id="singleMediaContainer" on:click|stopPropagation on:keypress={()=>{}}>
              <div id="gifContainer">
              <video autoplay playsinline loop muted id="mediaGIF">
                <track kind="captions">
                <!--maybe add other gifv formats?-->
                <source src="{media["url"]}" type="video/mp4">
              </video>
            </div>
            </div>
        
          {/if}
          
        </div>
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
  width:100%;
  /*
  border-style: none none solid none;
  border-color: #50c0cb;
  border-width: 1px;
  
  
  */
  padding: 0px 14px;
}
.post:hover {
  background-color: #3c4444;
  

}

.statusDetails {
    color: white;
    font-weight: bold;
    font-size: 14px;
    display: flex;
    justify-content: space-between;

  }

  #username{
    margin-bottom: 0px;
  }

  #htmlContent {
    font-size: 14px;
    pointer-events: none;
  }


#mediaImage, #mediaGIF, #mediaVideo{
  object-position: 50% 50%;
  object-fit: cover;
  height: 100%;
  width: 100%;
}

#mediaAudio {
  margin-bottom:14px;
}
#imageLink {
  height: 100%;
  width: 100%;
  cursor: zoom-in;
  display:block;
  position:relative;
}

#gifContainer, #videoContainer{
  height: 100%;
  width: 100%;
  cursor: zoom-in;
  position:relative;
  overflow:hidden;
}

#multipleMediaContainer {
  border:0;
  border-radius:5px;
  display:block;
  overflow:hidden;
  position: relative;
}

#singleMediaContainer {
  border:0;
  border-radius:5px;
  display:block;
  overflow:hidden;
  position: relative;
  box-sizing: border-box;
  aspect-ratio: 3/2;
  margin-bottom: 14px;
  width: 50%;
}

#mediaGallery {
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  aspect-ratio: 3/2;
  margin-bottom: 14px;
  display: grid;
  gap: 4px;
  grid-template-columns: 49.3% 49.3%;
  grid-template-rows: 49.3% 49.3%;
  width: 50%;
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
  font-size:14px;
}

#centering {
  display:flex;
  justify-content: center;
}

</style>