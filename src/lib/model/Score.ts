import mongoose, { Types } from 'mongoose';

// create interface
export interface IScore {
	title: string;
  path: string;
  user: Types.ObjectId;
  createAt: Date;
}

// create schema
const scoreSchema = new mongoose.Schema<IScore>({
  title: { type: String, required: true },
  user: { type: mongoose.Schema.Types.ObjectId, required: true },
  path: { type: String, required: true },
  createAt: { type: Date, requiured: true },
});

// create model
if (!mongoose.models.Score) {
  mongoose.model<IScore>('Score', scoreSchema);
}

export const Score = mongoose.models.Score;
