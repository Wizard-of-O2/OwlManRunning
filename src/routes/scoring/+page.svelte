<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<svelte:head>
	<title>OMR :: Scoring</title>
</svelte:head>

<h1>Scoring</h1>
<table>
	<thead>
		<tr>
			<th>Title</th>
			<th>Status</th>
		</tr>
	</thead>
	{#each data.scores as score (score._id)}
		<tr>
			<td><a href="/scoring/{score._id}">{score.title}</a></td>
			<td>{score.status ?? ''}</td>
		</tr>
	{/each}
	<tbody />
</table>
<a href="/scoring/new" role="button">New</a>
