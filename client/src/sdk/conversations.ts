
export async function getMessageContent() {
    let res = await fetch("/api/messages");
    let text = await res.json();

    if (res.ok) {
      return text;
    } else {
      throw new Error(text);
    }
  }