export async function getHomeContent() {
    let res = await fetch("/api/home");
    let text = await res.json();

    if (res.status == 200 || res.status == 206) {
      return text;
    } else {
      throw new Error(text);
    }
}