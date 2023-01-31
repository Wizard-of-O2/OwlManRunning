import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions = {
	login: async ({ request, cookies }) => {
		const formData = await request.formData();
		const username = formData.get('username')?.toString() ?? '';
		const password = formData.get('password')?.toString() ?? '';
		if (!username || !password) {
			return fail(400, { username, msg: 'wrong username or password.' });
		}

		// TODO: check username and password
		if (username === 'snow' && password === '11') {
			// Save data to cookie
			const jwt = JSON.stringify({ username: 'snow' });
			cookies.set('jwt', jwt, { path: '/', secure: false });
			throw redirect(307, '/');
		}
		return fail(400, { username, msg: 'wrong username or password.' });
	},
	logout: ({ cookies, locals }) => {
		cookies.delete('jwt', { path: '/', secure: false });
		locals.user = null;
		throw redirect(302, '/');
	}
} satisfies Actions;
