import type { Handle } from '@sveltejs/kit';

export const handle = (({ event, resolve }) => {
	const jwt = event.cookies.get('jwt');
	event.locals.user = jwt ? JSON.parse(jwt) : null;

	return resolve(event);
}) satisfies Handle;
