<script>
    import {link} from 'svelte-spa-router';

    export let status;
    import PollStatus from "./PollStatus.svelte"

    let showContent = false;

</script>

    <!--<p id="source" class="imptDetails">{status["account"]["username"]}</p>-->
    
    {#if status["sensitive"]}
        <span id="spoilerText">{status["spoiler_text"]} <button type="button" id="contentToggle" on:click={()=>{showContent = !showContent}}> {#if showContent} Hide {:else} Show {/if} Content</button></span>
    {/if}
    <div class="message">
    {#if !status["sensitive"] || (status["sensitive"] && showContent)}
        <p id="htmlContent">{@html status["content"]}</p>

        {#if status["media_attachments"].length == 4}
        <div id="centering">
          <div id="mediaGallery"> 
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
          <div id="mediaGallery"> 
            {#each status["media_attachments"] as media , index}
              {#if index == 0}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener">
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

              {/if}
            {/each}
          </div>
        </div>
        {:else if status["media_attachments"].length == 2}
        <div id="centering">
          <div id="mediaGallery"> 
            {#each status["media_attachments"] as media}
              {#if media["type"] == "image"}
                <div id="multipleMediaContainer" style="grid-row:span 2;">
                  <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener">
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
            <div id="singleMediaContainer">
              <a href="{media["url"]}" id="imageLink" target="_blank" rel="noreferrer noopener">
                <img src="{media["url"]}" id="mediaImage" alt="mediaImage"/>
              </a>
            </div>
        
          {:else if media["type"] == "audio"}

                <audio controls id="mediaAudio">
                  <source src={media["url"]} type="audio/mp3">
                </audio>

          {:else if media["type"] == "video"}
            <div id="singleMediaContainer">
              <div id="videoContainer">
                <video controls id="mediaVideo">
                  <track kind="captions">
                  <!--maybe add other video formats?-->
                  <source src="{media["url"]}" type="video/mp4">
                </video>
              </div>
            </div>

          {:else}
            <div id="singleMediaContainer">
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

    #spoilerText {
      margin: 14px;
      display:block;
      font-size:14px;
      font-weight: bold;
    }

    #contentToggle {
      margin-left: 5px;
      background-color: #50c0cb;
      color: #252c2c;
      font-family:"Open Sans";  
      font-size: 10px;
      font-weight: bold;
      border: none;
      padding: 2px 8px;
      border-radius: 15px; 
    }
    #htmlContent {
      font-size:14px;
      pointer-events: none;
      margin:0px 14px;
    }

    #mediaImage, #mediaGIF, #mediaVideo{
  object-position: 50% 50%;
  object-fit: cover;
  height: 100%;
  width: 100%;
  border-radius:5px;
}



#mediaAudio {
  width: 100%;
  padding: 0px 14px 14px 14px;
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
  border-radius:5px;
}

#multipleMediaContainer {
  border:0;
  border-radius:5px;
  display:block;
  overflow:hidden;
  position: relative;
  
}

#singleMediaContainer {
  /*border:0;
  border-radius:5px;*/
  display:block;
  overflow:hidden;
  position: relative;
  box-sizing: border-box;
  aspect-ratio: 3/2;
  padding: 0px 14px 14px 14px;
  width: 100%;
}

#mediaGallery {
  box-sizing: border-box;
  overflow: hidden;
  position: relative;
  aspect-ratio: 3/2;
  padding: 0px 14px 14px 14px;
  display: grid;
  gap: 4px;
  grid-template-columns: 49.3% 49.3%;
  grid-template-rows: 49.3% 49.3%;
  width:100%;
}

#centering {
  display:flex;
  justify-content: center;
}
    
  </style>