<script lang="ts">
	import type { PageServerData } from "./$types";

  export let data: PageServerData;
  const { article } = data;
</script>
<article>
  <header>
    <hgroup>
      <h3>{article.title}</h3>
      <h4>{article.author}</h4>
    </hgroup>
  </header>
  {@html article.content};
</article>
<div class="btn-container">
  <div>
    <a href="/article" role="button" class="secondary">List</a>
  </div>
  <div>
    <a href={'#'} role="button" class="secondary">Modify</a>
    <a href={'#'} role="button" class="warning">Delete</a>
  </div>
</div>
<style>
  .btn-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
</style>