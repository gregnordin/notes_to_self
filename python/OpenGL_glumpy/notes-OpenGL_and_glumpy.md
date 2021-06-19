
Go through this online book: 
[Python & OpenGL for Scientific Visualization by Nicolas P. Rougier, 2018](https://www.labri.fr/perso/nrougier/python-opengl/)

# Friday, 2020-06-18

Make virtual environment:

    $ conda activate py38
    (py38)
    nordin@nordin@MBP ~/Documents/Projects/2021_Projects/210618_OpenGL
    $ python -m venv .venv --prompt glumpy
    $ source .venv/bin/activate
    (glumpy) (py38)
    $ which python
    /Users/nordin/Documents/Projects/2021_Projects/210618_OpenGL/.venv/bin/python
    (glumpy) (py38)
    $ python --version
    Python 3.8.1
    
Install packages. See [Glumpy Installation](https://glumpy.github.io/installation.html)
    
    (glumpy) (py38)
    $ pip install numpy pyopengl
    
    (glumpy) (py38)
    $ glxinfo
        name of display: /private/tmp/com.apple.launchd.vbxwShdLk7/org.macosforge.xquartz:0
        display: /private/tmp/com.apple.launchd.vbxwShdLk7/org.macosforge.xquartz:0  screen: 0
        direct rendering: Yes
        server glx vendor string: SGI
        server glx version string: 1.4
        server glx extensions:
            GLX_ARB_multisample, GLX_EXT_import_context, GLX_EXT_visual_info,
            GLX_EXT_visual_rating, GLX_OML_swap_method, GLX_SGIS_multisample,
            GLX_SGIX_fbconfig
        client glx vendor string: Mesa Project and SGI
        client glx version string: 1.4
        client glx extensions:
            GLX_ARB_create_context, GLX_ARB_create_context_profile,
            GLX_ARB_create_context_robustness, GLX_ARB_fbconfig_float,
            GLX_ARB_framebuffer_sRGB, GLX_ARB_get_proc_address, GLX_ARB_multisample,
            GLX_EXT_buffer_age, GLX_EXT_create_context_es2_profile,
            GLX_EXT_create_context_es_profile, GLX_EXT_fbconfig_packed_float,
            GLX_EXT_framebuffer_sRGB, GLX_EXT_import_context,
            GLX_EXT_texture_from_pixmap, GLX_EXT_visual_info, GLX_EXT_visual_rating,
            GLX_INTEL_swap_event, GLX_MESA_copy_sub_buffer,
            GLX_MESA_multithread_makecurrent, GLX_MESA_query_renderer,
            GLX_MESA_swap_control, GLX_OML_swap_method, GLX_OML_sync_control,
            GLX_SGIS_multisample, GLX_SGIX_fbconfig, GLX_SGIX_pbuffer,
            GLX_SGIX_visual_select_group, GLX_SGI_make_current_read,
            GLX_SGI_swap_control, GLX_SGI_video_sync
        GLX version: 1.4
        GLX extensions:
            GLX_ARB_get_proc_address, GLX_ARB_multisample, GLX_EXT_import_context,
            GLX_EXT_visual_info, GLX_EXT_visual_rating,
            GLX_MESA_multithread_makecurrent, GLX_OML_swap_method,
            GLX_SGIS_multisample, GLX_SGIX_fbconfig
        OpenGL vendor string: ATI Technologies Inc.
        OpenGL renderer string: AMD Radeon Pro 560X OpenGL Engine
        OpenGL version string: 2.1 ATI-3.10.18
        OpenGL shading language version string: 1.20
        ... <lots more stuff>

    (glumpy) (py38)
    $ pip install glumpy
    (glumpy) (py38)
    $ python
        Python 3.8.1 (default, Jan  8 2020, 16:15:59)
        [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import glumpy  # IT WORKS!
        >>> exit()
        
Run simple program [code/chapter-03/glumpy-quad-solid.py](https://www.labri.fr/perso/nrougier/python-opengl/):

    $ python try_opengl_01.py --debug
        [i] Using GLFW (GL 2.1)
        [i] Running at 60 frames/second
        GPU: Creating program
        GPU: Attaching shaders to program
        GPU: Creating shader
        GPU: Compiling shader
        GPU: Creating shader
        GPU: Compiling shader
        GPU: Linking program
        GPU: Activating program (id=1)
        GPU: Activating buffer (id=5)
        GPU: Creating buffer (id=5)
        GPU: Deactivating buffer (id=5)
        GPU: Activating buffer (id=5)
        GPU: Updating position
        GPU: Deactivating buffer (id=5)
        GPU: Deactivating program (id=1)
        GPU: Activating program (id=1)
        GPU: Activating buffer (id=5)
        GPU: Deactivating buffer (id=5)
        GPU: Deactivating program (id=1)
        GPU: Activating program (id=1)
        ... repeat ad infinitum
        
Try everything else in the rest of Chapter 3 of the book.

