import mongoose, { mongo } from 'mongoose';
import { env } from '$env/dynamic/private';

const url = env.MONGODB_URL;
if (url) {
	mongoose.set('strictQuery', false);
	mongoose.set('overwriteModels', true);
	const conn = await mongoose.connect(url);
}
