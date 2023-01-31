import { error, redirect } from '@sveltejs/kit';
import type { HydratedDocument } from 'mongoose';

import type { Actions, PageServerLoad } from './$types';
import { Article, type IArticle } from '$lib/model/Article';

export const load = (async ({ locals }) => {
	if (!locals.user) throw error(401, 'Unauthorize');
	const result = await Article.find({}).lean();
	return { articles: JSON.parse(JSON.stringify(result)) };
}) satisfies PageServerLoad;

export const actions = {
	new: async ({ request }) => {
		const formData = await request.formData();
		const author = formData.get('author')?.toString();
		const title = formData.get('title')?.toString();
		const content = formData.get('content')?.toString();
		const article: HydratedDocument<IArticle> = new Article({
			author,
			title,
			content
		});
		await article.save();

		throw redirect(307, '/article');
	}
} satisfies Actions;
