import Login from './routes/login.svelte'
import Home from './routes/home.svelte'
import Messages from './routes/messages.svelte'
import Mastodon_Callback from './routes/callback/mstdn.svelte'

const routes = {
    // Exact path
    '/': Login,

    // Using named parameters, with last being optional
    '/home': Home,

    // Wildcard parameter
    '/messages': Messages,

    '/callback/mstdn': Mastodon_Callback,

}

export default routes;