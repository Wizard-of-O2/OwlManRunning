<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import type { PageServerData } from './$types';
	import { page } from '$app/stores';
	import TypeA from './TypeA.svelte';
	import TypeB from './TypeB.svelte';

	export let data: PageServerData;
	$: list = data?.score?.result ?? [];

	const handleDelete = () => {
		goto('/scoring');
	};

	const handleRerun = async () => {
		await fetch(`/scoring/${$page.params.id}`, { method: 'POST' });
		invalidateAll();
	};
</script>

<h2>{data?.score?.title}</h2>
<p>
	Type: {data?.score?.type}<br />
	Answer: {data?.score?.answer_title ?? ''}
</p>

{#if data?.score?.type === 'type_a'}
	<TypeA {list} />
{:else if data?.score?.type === 'type_b'}
	<TypeB {list} />
{/if}
<div class="btn-container">
	<div>
		<a href="/scoring" role="button">List</a>
	</div>
	<div>
		<a href={'#'} on:click|preventDefault={handleRerun} role="button">Rerun</a>
		<a href={'#'} on:click|preventDefault={handleDelete} role="button">Delete</a>
	</div>
</div>

<style>
	.btn-container {
		margin-bottom: 1rem;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
</style>
