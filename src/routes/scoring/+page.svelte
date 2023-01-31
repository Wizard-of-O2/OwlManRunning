<script lang="ts">
	import { enhance } from '$app/forms';
  // @ts-ignore
	import FilePond, { registerPlugin } from 'svelte-filepond';
  import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';

	let pond;
	let name = 'filepond';
	const handleInit = () => {};
	const handleAddFile = () => {};

  registerPlugin(FilePondPluginFileValidateType);
</script>

<svelte:head>
	<title>OMR :: Scoring</title>
</svelte:head>
<h3>Scoring</h3>
<form method="POST" use:enhance>
	<input type="text" name="title" placeholder="Title" required />
	<FilePond
		bind:this={pond}
		{name}
		allowMultiple={true}
    storeAsFile={true}
		oninit={handleInit}
		onaddfile={handleAddFile}
    acceptedFileTypes={['image/jpeg']}
	/>
	<button>Submit</button>
</form>
<style>
  
</style>