import type { Actions } from './$types';

export const actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const title = formData.get('title') as string;
    const files = formData.getAll('filepond');

    console.log(files);
		
    // upload file to somewhere
		return {};
	}
} satisfies Actions;
