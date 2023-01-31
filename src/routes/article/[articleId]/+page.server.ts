import { Article, type IArticle } from '$lib/model/Article';
import { error } from '@sveltejs/kit';
import type { HydratedDocument } from 'mongoose';
import type { PageServerLoad } from './$types';

export const load = (async ({ params }) => {
	const { articleId } = params;

	try {
		const a: HydratedDocument<IArticle> = await Article.findById(articleId).lean();
		const article = JSON.parse(JSON.stringify(a));
		return { article };
	} catch (e) {
		throw error(400, `${e}`);
	}
}) satisfies PageServerLoad;
