import mongoose from 'mongoose';
import { env } from '$env/dynamic/private';

import '$lib/model/Answer'
import '$lib/model/Article'
import '$lib/model/Score'

const url = env.MONGODB_URL;
if (url) {
	mongoose.set('strictQuery', false);
	mongoose.set('overwriteModels', true);
	const conn = await mongoose.connect(url);
}
