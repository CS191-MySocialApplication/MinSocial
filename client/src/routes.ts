import Login from './routes/login.svelte'
import Home from './routes/home.svelte'
import Message from './routes/message.svelte'
import Messages from './routes/messages.svelte'
import Replies from './routes/replies.svelte'
import Status from './routes/status.svelte'
import Mastodon_Callback from './routes/callback/mstdn.svelte'

const routes = {
    '/': Login,
    '/home': Home,
    '/msg/:cid/:tid': Message,
    '/messages': Messages,
    '/replies': Replies,
    '/callback/mstdn': Mastodon_Callback,
    '/toot/:id': Status
}

export default routes;