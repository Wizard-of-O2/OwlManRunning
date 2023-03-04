import { Score, type IScore } from '$lib/model/Score';
import type { HydratedDocument } from 'mongoose';
import type { PageServerLoad } from './$types';

export const load = (async ({ locals }) => {
	const userId = locals.user!.userId;
	const rslt: HydratedDocument<IScore>[] = await Score.find({ user: userId })
    .sort({'createAt': -1})
    .lean();
  
	const scores = rslt.map((o) => ({
		...o,
    answer: '',
		_id: o._id.toString(),
		user: o.user.toString()
	}));

	return { scores };
}) satisfies PageServerLoad;
