import { replace } from 'svelte-spa-router';

export async function getStatus(params: any) {
    if(params.id !== undefined){
        let res = await fetch("/api/context/toot/"+String(params.id));
        let text = await res.json();
        console.log(text)
        if (res.status == 200 || res.status == 206) {
            return text;
        } else {
            replace("/");
        }
    }
}