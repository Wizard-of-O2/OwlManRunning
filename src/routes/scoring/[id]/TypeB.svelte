<script lang="ts">
	import type { IResult } from '$lib/model/Score';

	export let list: IResult[];
	let range1 = [...Array(30).keys()];
</script>

<figure>
	<table>
		<thead>
			<tr>
				<th rowspan="2">No</th>
				<th colspan="2" rowspan="2">Name</th>
				<th colspan="30">Subject #1</th>
				<th colspan="30">Subject #2</th>
				<th colspan="30">Subject #3</th>
			</tr>
			<tr>
				{#each range1 as idx}
					<th>{idx + 1}</th>
				{/each}
				{#each range1 as idx}
					<th>{idx + 1}</th>
				{/each}
				{#each range1 as idx}
					<th>{idx + 1}</th>
				{/each}
			</tr>
		</thead>
		{#each list as r (r.page_no)}
			<tr>
				<td>{r.page_no}</td>
				<td>{r.given_name}</td>
				<td>{r.surname}</td>
				{#each range1 as idx}
					<td>{r[`answer_0_${idx + 1}`]}</td>
				{/each}
				{#each range1 as idx}
					<td>{r[`answer_1_${idx + 1}`]}</td>
				{/each}
				{#each range1 as idx}
					<td>{r[`answer_2_${idx + 1}`]}</td>
				{/each}
			</tr>
		{/each}
	</table>
</figure>
