import { Score } from '$lib/model/Score';
import { sendToQueue } from '$lib/server/queue';
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const POST = (async ({ params }) => {
	const { id } = params;

	// update
	await Score.updateOne({ '_id': id }, { '$set': { status: 'processing' }, '$unset': { result: 1 } });

	// set to the queue
	await sendToQueue(id);
	return json({});
}) satisfies RequestHandler;

export const DELETE = (async ({ params }) => {
	return json({});
}) satisfies RequestHandler;
