<script lang="ts">
	import { enhance } from '$app/forms';
</script>

<svelte:head>
	<title>OMR :: Scoring</title>
</svelte:head>
<h1>New Scoring</h1>
<form method="POST" use:enhance>
	<input type="text" name="title" placeholder="Title" required />
	<input type="file" name="file" required accept="image/jpeg, image/png, application/pdf"/>
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
