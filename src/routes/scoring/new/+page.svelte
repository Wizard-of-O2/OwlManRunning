<script lang="ts">
	import { enhance } from '$app/forms';
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

<svelte:head>
	<title>OMR :: Scoring</title>
</svelte:head>
<h1>New Scoring</h1>
<form method="POST" use:enhance>
	<input type="text" name="title" placeholder="Title" required />
	<select name="type" required>
		<option value="type_a">Type A</option>
		<option value="type_b">Type B</option>
	</select>
	<select name="answer">
		{#each data.answers as answer(answer._id)}
		<option value="{answer._id}">{answer.title}</option>
		{/each}
	</select>
	<input type="file" name="file" required accept="application/pdf"/>
	<div class="btn-container">
		<button type="submit" class="submit-btn">Submit</button>
		<a href="/scoring" class="secondary" role="button">Cancel</a>
	</div>
</form>

<style>
	.submit-btn {
		width: auto;
		margin: 0;
	}
	.btn-container {
		display: flex;
		flex-direction: row;
		justify-content: flex-end;
		gap: 1rem;
	}
</style>
