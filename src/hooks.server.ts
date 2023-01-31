import type { Handle } from '@sveltejs/kit';
import '$lib/server/db';

export const handle = (({ event, resolve }) => {
	const jwt = event.cookies.get('jwt');
	event.locals.user = jwt ? JSON.parse(jwt) : null;

	return resolve(event);
}) satisfies Handle;
