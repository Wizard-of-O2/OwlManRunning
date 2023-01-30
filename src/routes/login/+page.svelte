<script lang="ts">
	import { enhance } from '$app/forms';
	import type { ActionData } from './$types';
	export let form: ActionData;
</script>

<svelte:head>
	<title>OMR :: Sign in</title>
</svelte:head>
<div>
	<div style="width: 50%; margin: auto; text-align: center;">
		<h3>Sign in</h3>
		{#if form?.msg}
			<article class="warning">{form.msg}</article>
		{/if}
		<form method="POST" action="?/login" use:enhance>
			<input
				type="text"
				placeholder="Username"
				name="username"
				required
				maxlength="100"
				value={''}
			/>
			<input
				type="password"
				placeholder="Password"
				name="password"
				required
				maxlength="100"
				value={''}
			/>
			<input type="submit" value="Sign in" />
		</form>
	</div>
</div>

<style>
	article.warning {
		padding: 8px;
		background-color: tomato;
		margin: 0 0 8px 0;
	}
</style>
