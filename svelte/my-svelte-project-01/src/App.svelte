<script>
  export let name;

  let count = 0;

  function handleClick() {
    count += 1;
  }
</script>

<main>
  <h1>Hello {name}!</h1>
  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps.
  </p>
</main>

<newpart>
  <p>Test text</p>
  <p>name variable: {name}</p>
</newpart>

<button on:click={handleClick}>
  Clicked {count}
  {count === 1 ? "time" : "times"}
</button>

<style>
  newpart {
    text-align: center;
  }
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
