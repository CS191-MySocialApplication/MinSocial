
export async function getMsg(params: any) {
    if(params.tid !== undefined){
        let res = await fetch("/api/context/toot/"+String(params.cid)+"/"+String(params.tid));
        let text = await res.json();
        console.log(text)
        if (res.status == 200 || res.status == 206) {
            return text;
        } else {
            throw new Error(text);
        }
    }
}