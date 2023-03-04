<script lang="ts">
	import '@picocss/pico/css/pico.min.css';
	import '../app.css';

	import { enhance } from '$app/forms';
	import type { LayoutServerData } from './$types';
	export let data: LayoutServerData;

	const handleSubmit = () => {
		const f = document.querySelector('#form') as HTMLFormElement;
		return f.submit();
	};
</script>

<div class="container">
	<nav>
		<ul>
			<li><a href="/">OMR</a></li>
			{#if data.user}
				<li><a href="/scoring">Scoring</a></li>
				<li><a href="/answer">Answer</a></li>
			{/if}
		</ul>
		<ul>
			{#if !data.user}
				<li><a href="/login">Sign in</a></li>
			{:else}
				<li>
					<form method="POST" action="/login?/logout" use:enhance id="form">
						<a href={'#'} on:click={handleSubmit}>Sign out</a>
					</form>
				</li>
			{/if}
		</ul>
	</nav>
</div>
<main class="container">
	<slot />
</main>
