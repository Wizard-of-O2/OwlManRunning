<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<svelte:head>
	<title>OMR :: Article</title>
</svelte:head>
<h3>Articles</h3>
<table>
	<thead>
		<tr>
			<th>title</th>
			<th style="width: 10%;">username</th>
		</tr>
	</thead>
	<tbody>
		{#each data.articles as article (article._id)}
			<tr>
				<td><a href="/article/{article._id}">{article.title}</a></td>
				<td>{article.author}</td>
			</tr>
		{/each}
	</tbody>
</table>
<div class="btn-container">
  <a href="/article/new" role="button">Write</a>
</div>
<style>
  .btn-container {
    display: flex;
    flex-direction: row;
    justify-content: right;
  }
</style>