import type { IAnswer } from '$lib/model/Answer';
import { Score, type IResult } from '$lib/model/Score';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async ({ params, locals }) => {
	const { id } = params;

	const score = await Score.findById(id).populate('answer');

	// processing
	if (score == null) throw error(404, 'Not Found');
	if (score.user.toString() !== locals.user?.userId) throw error(403, 'Unauthorize');
	if (score.type === 'type_a') {
		const conv = score?.result?.map((o, idx) => ({
			...o,
			page_no: idx + 1,
			centre_number: `${o.centre_number_1}${o.centre_number_2}`,
			student_number: `${o.student_number_1}${o.student_number_2}${o.student_number_3}${o.student_number_4}`
		}));

		return {
			score: {
				title: score.title,
				type: score.type,
				path: score.path,
				answer_title: (score.answer as IAnswer).title,
				result: conv
			}
		};
	} else if (score.type === 'type_b') {
		const conv = score.result?.map((o, idx) => ({
			...o,
			page_no: idx + 1,
			given_name: makeName(o, 'given_name_'),
			surname: makeName(o, 'surname_')
		}));

		return {
			score: {
				title: score.title,
				type: score.type,
				path: score.path,
				answer_title: (score.answer as IAnswer).title,
				result: conv
			}
		};
	}

	return {
		score: {}
	};
}) satisfies PageServerLoad;

const makeName = (o: IResult, keyHead: string) => {
	const arr = 'abcdefghijklmnopqrstuvwxyz';
	let name = '';
	for (let i = 1; i <= 12; i++) {
		let key = `${keyHead}${i}`;
		if ((o[key] instanceof Array<number>) && (o[key] as number[]).length > 0) {
			name += arr[(o[key] as number[])[0]];
		}
	}
	return name;
};
