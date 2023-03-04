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

	let answer_title = '';
	if (score.answer && 'title' in score.answer) {
		answer_title = score.answer.title;
	}

	if (score.type === 'type_a') {
		const result = score.result?.map((o, idx) => ({
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
				answer_title,
				result
			}
		};
	} else if (score.type === 'type_b') {
		const result = score.result?.map((o, idx) => ({
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
				answer_title,
				result
			}
		};
	}

	return {
		score: {}
	};
}) satisfies PageServerLoad;

const makeName = (o: IResult, keyHead: string) => {
	const str = 'abcdefghijklmnopqrstuvwxyz';
	let name = '';
	for (let i = 1; i <= 12; i++) {
		let key = `${keyHead}${i}`;
		const arr = o[key] as number[];
		if (arr.length > 0) {
			name += str[arr[0]];
		}
	}
	return name;
};
