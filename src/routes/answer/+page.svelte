<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<h1>Answer</h1>
<table>
	<thead>
		<tr>
			<th>Title</th>
      <th>Type</th>
		</tr>
	</thead>
	<tbody>
		{#each data.answers as answer(answer._id)}
			<tr>
				<td>{answer.title}</td>
        <td>{answer.type}</td>
			</tr>
		{/each}
	</tbody>
</table>
