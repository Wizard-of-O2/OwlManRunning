<script lang="ts">
	interface Record {
		page_no: number;
		[key: string]: number | number[];
	};

	export let path: string;
	export let list: Record[];
	let range1 = [...Array(60).keys()];
</script>

<figure>
	<table>
		<thead>
			<tr />
			<tr>
				<th rowspan="2">No</th>
				<th rowspan="2">Centre No</th>
				<th rowspan="2">Student No</th>
				<th colspan="60">Subject #1</th>
				<th colspan="60">Subject #2</th>
			</tr>
			<tr>
				{#each range1 as r}
					<th>{r + 1}</th>
				{/each}
				{#each range1 as r}
					<th>{r + 1}</th>
				{/each}
			</tr>
		</thead>
		<tbody>
			{#each list as r (r.page_no)}
				<tr>
					<td><a href="https://objectstorage.ap-seoul-1.oraclecloud.com/n/cnqwgzok7slt/b/bucket-1/o/{path}/result_{r.page_no}.png"
								target="_blank" rel="noreferrer">{r.page_no}</a></td>
					<td>{r.centre_number}</td>
					<td>{r.student_number}</td>
					{#each range1 as rr}
						<td>{r[`answer_0_${rr + 1}`]}</td>
					{/each}
					{#each range1 as rr}
						<td>{r[`answer_1_${rr + 1}`]}</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>
</figure>
