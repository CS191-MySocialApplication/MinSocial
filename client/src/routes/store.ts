import { writable } from 'svelte/store';

export const lastPageAccessed = writable("/#/home");

export default lastPageAccessed;