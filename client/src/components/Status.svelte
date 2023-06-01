<script>
    import {link} from 'svelte-spa-router';

    export let status;

    let showContent = false;

</script>



    <!--Change href to mentions thread-->
    <p id="source" class="imptDetails">{status["account"]["username"]}</p>
    <span id="dateTime">{status["created_at"]}</span><br />
    {#if status["sensitive"]}
        <span id="spoilerText">{status["spoiler_text"]} <button type="button" on:click={()=>{showContent = !showContent}}> {#if showContent} Hide {:else} Show {/if} Content</button></span>
    {/if}
    <a class="post" href="/toot/{status["id"]}" use:link>
    {#if !status["sensitive"] || (status["sensitive"] && showContent)}
        <p>{@html status["content"]}</p>
        {#if status["media_attachments"].length !== 0}
        {#each status["media_attachments"] as image}
            <img src="{image["url"]}" alt="something"/>
        {/each}
        {:else if status["poll"] !== null}
        <!-- {console.log(status["poll"])} -->
        <ul>
        {#each status["poll"]["options"] as choice}
            <li>{choice["title"]} - Votes: {choice["votes_count"]}</li>
        {/each}
        </ul>

        Total Votes - {status["poll"]["votes_count"]}
        {/if}
    {/if}
  </a>

  <style>
    a {
    display: block;
    text-decoration: none;
    color: inherit;
    border-style: none none solid none;
    border-color: #50c0cb;
    border-width: 1px;
    padding: 0px 14px;
  }
  a:hover {
    background-color: #3c4444;
    fill-opacity: 0.5;
  }
  .imptDetails {
    margin-bottom: 0;
  }
  </style>