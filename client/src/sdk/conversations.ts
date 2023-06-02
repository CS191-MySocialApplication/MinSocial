import { replace } from 'svelte-spa-router';

export async function getMessageContent() {
    let res = await fetch("/api/messages");
    let text = await res.json();

    if (res.ok) {
      return text;
    } else {
      replace("/");
    }
  }