import { replace } from 'svelte-spa-router';

export async function getMessageContent() {
    let res = await fetch("/api/messages");
    let text = await res.json();

    if (res.status == 200 || res.status == 206) {
      return text;
    } else {
      replace("/");
    }
  }