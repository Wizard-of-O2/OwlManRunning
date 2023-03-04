import mongoose, { Model } from 'mongoose';

// create interface
export interface IAnswer {
	title: string;
	content?: string;
	type: string;
	path: string;
	[key: string]: string | [number] | undefined;
}

// create schema
const answerSchema = new mongoose.Schema<IAnswer>({
	title: { type: String, required: true },
	content: { type: String },
	type: { type: String, required: true },
	path: { type: String },
});

// create model
export const Answer = mongoose.model<IAnswer>('Answer', answerSchema);
