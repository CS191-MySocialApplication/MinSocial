import { writable } from 'svelte/store';

export const lastPageAccessed = writable(0);

export default lastPageAccessed;