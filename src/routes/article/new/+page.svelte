<script>
	import { enhance } from '$app/forms';
</script>

<svelte:head>
	<title>OMR :: New article</title>
</svelte:head>
<h3>New Article</h3>
<form method="POST" action="/article?/new" use:enhance>
	<input type="text" name="author" placeholder="author" required maxlength="100"/>
	<input type="text" name="title" placeholder="title" required maxlength="100"/>
	<textarea name="content" placeholder="content" rows="6" required />
	<div class="btn-container">
		<button style="width: auto; margin: 0;">Save</button>
		<a href="/article" role="button" class="secondary">Cancel</a>
	</div>
</form>

<style>
	.btn-container {
		display: flex;
		flex-direction: row;
		justify-content: right;
		gap: 16px;
	}
	textarea {
		resize: none;
	}
</style>
