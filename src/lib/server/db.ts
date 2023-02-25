import mongoose, { mongo } from 'mongoose';
import { env } from '$env/dynamic/private';

const url = env.MONGODB_URL;
if (url) {
	const conn = await mongoose.connect(url);
	mongoose.set('strictQuery', false);
	mongoose.set('overwriteModels', true);
}
