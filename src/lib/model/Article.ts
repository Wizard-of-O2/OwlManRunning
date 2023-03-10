import mongoose, { Model } from 'mongoose';

// create interface
export interface IArticle {
	author: string;
	title: string;
	content: string;
}

// create schema
const articleSchema = new mongoose.Schema<IArticle>({
	author: { type: String, required: true },
	title: { type: String, required: true },
	content: { type: String, required: true }
});

// create model
export const Article = mongoose.model<IArticle>('Article', articleSchema);
