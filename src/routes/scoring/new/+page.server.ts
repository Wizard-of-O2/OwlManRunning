import fs from 'node:fs';
import { v4 as uuidv4 } from 'uuid';
import type { Actions } from './$types';
import { Score, type IScore } from '$lib/model/Score';
import mongoose, { type HydratedDocument } from 'mongoose';

export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const title = formData.get('title') as string;
    const file = formData.get('file') as File;

    console.log(title, file);
		
    // upload file to somewhere
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
			user: new mongoose.Types.ObjectId('63d27d96731dee61afd00b77'),
			createAt: new Date(),
		});
		await score.save();

		return {};
	}
} satisfies Actions;
