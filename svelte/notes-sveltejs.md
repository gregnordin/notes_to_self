# Try out svelte.js



# Tuesday, 2021-07-06

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