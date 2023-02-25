import mongoose, { Types, Model } from 'mongoose';

// create interface
export interface IScore {
	title: string;
  path: string;
  user: Types.ObjectId;
  createAt: Date;
  status?: string;
}

// create schema
const scoreSchema = new mongoose.Schema<IScore>({
  title: { type: String, required: true },
  user: { type: mongoose.Schema.Types.ObjectId, required: true },
  path: { type: String, required: true },
  createAt: { type: Date, requiured: true },
  status: { type: String },
});

// create model
export const Score = mongoose.model<IScore>('Score', scoreSchema);
