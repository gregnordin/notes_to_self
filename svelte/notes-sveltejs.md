# Try out svelte.js

---

# Wednesday, 2021-07-07

## Log

- Look through the rest of the Svelte tutorial just focusing on the main chapter ideas
- Read [What's the deal with SvelteKit?](https://svelte.dev/blog/whats-the-deal-with-sveltekit)


# Tuesday, 2021-07-06

## Next

- Pick up from where I left off at the `Bindings/Group inputs` section of the [Svelte Tutorial](https://svelte.dev/tutorial/making-an-app).
- Look into Flask with svelte
    - [Flask + Svelte](https://svelte.dev/tutorial/group-inputs) - good
    - [Svelte.js + Flask](https://github.com/cabreraalex/svelte-flask-example) - 
A super simple example of using Flask to serve a Svelte app and use it as a backend server.
- Look into D3.js with svelte
    - [svelte-charts](https://medium.com/@mbostock/why-you-should-use-d3-ae63c276e958)
    - [Cannot get D3.js to work inside Svelte component (with Rollup)](https://techinplanet.com/cannot-get-d3-js-to-work-inside-svelte-component-with-rollup/) - good info

## Log

- Start going through [Svelte Tutorial](https://svelte.dev/tutorial/making-an-app) up to the `Introduction - making-an-app` section.
- Install VS code plugin: Svelte for VS Code
- Follow [Svelte for new developers - Creating a project](https://svelte.dev/blog/svelte-for-new-developers#Creating_a_project)

        npx degit sveltejs/template my-svelte-project  
        cd my-svelte-project  
        npm install  
        $ npm run dev
            
            > svelte-app@1.0.0 dev
            > rollup -c -w
            
            rollup v2.52.7
            bundles src/main.js → public/build/bundle.js...
            LiveReload enabled
            created public/build/bundle.js in 228ms
            
            [2021-07-06 13:28:21] waiting for changes...
            
            > svelte-app@1.0.0 start
            > sirv public --no-clear "--dev"
            
            
              Your application is ready~! 🚀
            
              - Local:      http://localhost:5000
              - Network:    Add `--host` to expose
              
    - It works! Use `^C` from the command line to exit.
    - Explore directory, focus on `src` and `public`.
- Edit `src/App.svelte` to add a new component `newpart`.
- Add `src/simplecounter.svelte` and include in App.
    - See [Building a simple Svelte JS app - Example included](https://blog.logrocket.com/how-to-build-a-simple-svelte-js-app/).
        - Center button horizontally: [How can I horizontally center a button element in a div element?](https://stackoverflow.com/questions/15300234/how-can-i-horizontally-center-a-button-element-in-a-div-element)
- Add reactivity with `$: ...`. Nice.
- Go through `props` section of [Svelte Tutorial](https://svelte.dev/tutorial/props).
- Go through `logic` section of [Svelte Tutorial](https://svelte.dev/tutorial/logic).
- Go through `events` section of tutorial.

