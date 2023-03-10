import mongoose, { Types, Model } from 'mongoose';
import type { IAnswer } from './Answer';

// create interface
export interface IScore {
	title: string;
	path: string;
	filename: string;
	type: string;
	answer?: Types.ObjectId | IAnswer;
	user: Types.ObjectId;
	createAt: Date;
	status?: string;
	result?: any[];
}

export interface IResult {
	page_no: number;
	[key: string]: number[] | string | number;
}

// create schema
const scoreSchema = new mongoose.Schema<IScore>({
	title: { type: String, required: true },
	path: { type: String, required: true },
	filename: { type: String, required: true },
	type: { type: String, required: true },
	answer: { type: mongoose.Schema.Types.ObjectId, ref: 'Answer' },
	user: { type: mongoose.Schema.Types.ObjectId, required: true },
	createAt: { type: Date, requiured: true },
	status: { type: String },
	result: Array<IResult>
});

// create model
export const Score = mongoose.model<IScore>('Score', scoreSchema);
