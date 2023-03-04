import { Answer, type IAnswer } from '$lib/model/Answer';
import type { HydratedDocument } from 'mongoose';
import type { PageServerLoad } from './$types';

export const load = (async () => {
	const rslt: HydratedDocument<IAnswer>[] = await Answer.find().lean();
	const answers = rslt.map((o) => ({
		...o,
		_id: o._id.toString()
	}));

  console.log(rslt);

	return { answers };
}) satisfies PageServerLoad;
