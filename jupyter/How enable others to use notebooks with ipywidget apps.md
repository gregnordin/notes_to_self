# How enable others to use notebooks with ipywidget apps?

## 2 use cases:

- Access control for my group and collaborators only &rarr; Jupyterhub on server behind BYU firewall
    - CS Dashboard to serve built-out dashboards
    - Shared storage to get to and run notebooks
- No access control that anyone can get to (share with colleagues located anywhere) &rarr; Public server running voila
    - For each dashboard, run `voila xxx.ipynb` on a unique port, leaving ports 80 and 443 open for the usual default browser traffic

## Main possibilities

- [Voila](https://voila.readthedocs.io/en/stable/index.html)

        (base)
        $ conda activate jupyter_py37
        (jupyter_py37) (base)
        $ pip install voila

- JupyterHub
    - [JupyterHub Tutorial: Set up your Lab, Classroom, or Business](https://www.youtube.com/watch?v=Mk6ZHVIw0Xs)
    - The Littlest JupyterHub (TLJH)
        - [Installing on your own server](https://tljh.jupyter.org/en/latest/install/custom-server.html)
        - Can use LDAP as the authenticator. See:
            - [Configuring JupyterHub authenticators](https://tljh.jupyter.org/en/latest/topic/authenticator-configuration.html) - LDAPAuthenticator is already installed, there's an example for how to configure at least one part of it
            - [LDAPAuthenticator](https://github.com/jupyterhub/ldapauthenticator) README says the minimum info needed to configure it
- Flask and ipywidgets
    - [maartenbreddels/flask-ipywidgets](https://github.com/maartenbreddels/flask-ipywidgets)
        - Hasn't been updated in 2 years, looks dead

## Other possibilities 

Without necessarily being interactive....

- [Static website from Jupyter Notebooks](https://mikkelhartmann.dk/2019/05/14/static-website-from-jupyter-notebooks.html)
- [Switching to Nikloa for Jupyter Notebooks and a static site](https://mglerner.github.io/posts/switching-to-nikloa-for-jupyter-notebooks-and-a-static-site.html)
- Put a static website on an RPi in my office
    - But IP address will keep changing so how create a stable link to it?
- Put a static website on an RPi at home
- Put a static website on a BYU VM
- Put a static website on Digital Ocean or Linode?
- [Raspberry Pi on Internet via reverse SSH tunnel](https://gist.github.com/nileshtrivedi/4c615e8d3c1bf053b0d31176b9e69e42) 