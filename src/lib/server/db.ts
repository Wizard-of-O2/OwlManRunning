import mongoose from 'mongoose';
import { env } from '$env/dynamic/private';

import '$lib/model/Article';

const url = env.MONGODB_URL;
if (url) {
	const conn = await mongoose.connect(url);
	console.log(conn.model);
}
