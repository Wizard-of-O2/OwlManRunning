import fs from 'node:fs';
import { v4 as uuidv4 } from 'uuid';
import type { Actions } from './$types';
import { Score, type IScore } from '$lib/model/Score';
import mongoose, { type HydratedDocument } from 'mongoose';
import { redirect } from '@sveltejs/kit';
import { sendToQueue } from '$lib/server/queue';

export const actions = {
	default: async ({ request, locals }) => {
		const formData = await request.formData();
		const title = formData.get('title') as string;
		const file = formData.get('file') as File;

		const uid = uuidv4();
		// create folder
		fs.mkdirSync(`uploads/${uid}`);

		// save files
		const buf = Buffer.from(await file.arrayBuffer());
		const path = `uploads/${uid}/${file.name}`;
		fs.writeFileSync(path, buf);

		// create
		const score: HydratedDocument<IScore> = new Score({
			title,
			path,
			user: new mongoose.Types.ObjectId(locals.user!.userId),
			createAt: new Date(),
			status: 'processing'
		});
		const savedScore = await score.save();

		// send to queue
		await sendToQueue(savedScore._id.toString());

		throw redirect(303, '/scoring');
	}
} satisfies Actions;
