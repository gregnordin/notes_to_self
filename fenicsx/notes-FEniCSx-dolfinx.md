# Tutorial/example resources

[DOLFINx documentation](https://docs.fenicsproject.org/dolfinx/main/python/)

[The FEniCSx tutorial](https://jsdokken.com/dolfinx-tutorial/) by jsdokken.

[FEniCS23-tutorial](https://jsdokken.com/FEniCS23-tutorial/README.html) by jsdokken.  

[DOLFINx: The next generation FEniCS problem solving environment](https://zenodo.org/records/10447666) - 12/31/23, extensive journal paper.

[Nguyen Lab Wiki - fenicsx how-to](https://me.jhu.edu/nguyenlab/doku.php?id=fenicsx) - lots of good info.

## Discourse threads

[Can I run FEniCSx in Apple silicon M3 max?](https://fenicsproject.discourse.group/t/can-i-run-fenicsx-in-apple-silicon-m3-max/13211) - similar problem as mine where he migrated from 2015 Intel macbook pro to M3 Max Apple Silicon macbook pro. Solution: *erase everything in the new MacBook and set it up by hand, not use migration*.

> dokken writes: *Several core developers use Mac in their development.*

[The usage of the functions of dolfinx](https://fenicsproject.discourse.group/t/the-usage-of-the-functions-of-dolfinx/13214).

>The API of DOLFINx has been quite stable since v0.5.x/v0.6.x.
>There will always be some API changes, as we keep on improving the software.

# Install latest version of `fenicsx`



```
micromamba create -n fenicsx-env fenics-dolfinx mpich pyvista imageio
micromamba activate fenicsx-env

which python
	/Users/nordin/micromamba/envs/fenicsx-env/bin/python
python --version
	Python 3.12.1
python -c "import platform; print(platform.processor())"
	arm

python -c 'import dolfinx; print(f"DOLFINx version: {dolfinx.__version__} based on GIT commit: {dolfinx.git_commit_hash} of https://github.com/FEniCS/dolfinx/")'
	DOLFINx version: 0.7.2 based on GIT commit:  of https://github.com/FEniCS/dolfinx/
	
cd <correct directory>
python diffusion_2D.py
```

**The above works great--should have re-done my python installation and management long ago.**

## Make available as Jupyter kernel

```
micromamba install ipykernel
python -m ipykernel install --user --name fenicsx-env --display-name="fenicsx-env"
```



# OLD - Install latest version of `fenicsx`

Problem: my conda installation on my Apple Silicon macbook pro is for Intel x86 architecture and I need `fenicsx` to run natively on Apple Silicon. 

## What architecture python is running?

How to tell which architecture python is running on ([How to get architecture of running Python interpreter on MacOS with Apple Silicon?](https://stackoverflow.com/questions/71548156/how-to-get-architecture-of-running-python-interpreter-on-macos-with-apple-silico)):

    python -c "import platform; print(platform.processor())"
      The output is as following:
      On an M1/M2 Mac --> arm
      On an older Mac --> i386

## Install `fenicsx` - 1/9/24, updated through 1/12/24

Create fenicsx environment. 

    conda create -n fenicsx-env

Install packages for Apple Silicon. This will automatically install the latest python version of python because python is a dependency of the specified packages.

    conda activate fenicsx-env
    conda install --override-channels -c conda-forge/osx-arm64 -c conda-forge/noarch fenics-dolfinx mpich pyvista
    
    which python
        /Users/nordin/opt/miniconda3/envs/fenicsx-env/bin/python
    python --version
        Python 3.12.1
    python -c "import platform; print(platform.processor())"
        arm

### Try to reproduce &rarr; fail

#### Summary

As noted below, the python version is for Apple Silicon (`arm`), but it fails with `FileNotFoundError: [Errno 2] No such file or directory: 'x86_64-apple-darwin13.4.0-clang'`, meaning that it is looking for an Intel C compiler, which it should not need.

Running `python diffusion_2D.py` in the conda environment `fenicsx-env` works perfectly fine. I do not know what is different between 1/9/24 and today, 1/12/24.

#### Conclusion

**Delete my Intel conda installation and start fresh with a new minconda set up, or do mamba.**

#### Terminal session

    conda create -n fenicsx-env-temp2
        Collecting package metadata (current_repodata.json): done
        Solving environment: done
    
        ==> WARNING: A newer version of conda exists. <==
          current version: 23.9.0
          latest version: 23.11.0
    
        Please update conda by running
    
            $ conda update -n base -c defaults conda
    
        Or to minimize the number of packages updated during conda update use
    
             conda install conda=23.11.0
    
        ## Package Plan ##
    
          environment location: /Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2
    
        Proceed ([y]/n)? y
    
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        #
        # To activate this environment, use
        #
        #     $ conda activate fenicsx-env-temp2
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
    
    conda activate fenicsx-env-temp2
    conda install --override-channels -c conda-forge/osx-arm64 -c conda-forge/noarch fenics-dolfinx mpich pyvista
        Collecting package metadata (current_repodata.json): done
        Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.
        Solving environment: unsuccessful attempt using repodata from current_repodata.json, retrying with next repodata source.
        Collecting package metadata (repodata.json): done
        Solving environment: done
    
        ## Package Plan ##
    
          environment location: /Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2
    
          added / updated specs:
            - fenics-dolfinx
            - mpich
            - pyvista
    
        The following NEW packages will be INSTALLED:
    
          aiohttp            conda-forge/osx-arm64::aiohttp-3.9.1-py312he37b823_0
          aiosignal          conda-forge/noarch::aiosignal-1.3.1-pyhd8ed1ab_0
          aom                conda-forge/osx-arm64::aom-3.7.1-h463b476_0
          attrs              conda-forge/noarch::attrs-23.2.0-pyh71513ae_0
          blosc              conda-forge/osx-arm64::blosc-1.21.5-hc338f07_0
          brotli             conda-forge/osx-arm64::brotli-1.1.0-hb547adb_1
          brotli-bin         conda-forge/osx-arm64::brotli-bin-1.1.0-hb547adb_1
          brotli-python      conda-forge/osx-arm64::brotli-python-1.1.0-py312h9f69965_1
          bzip2              conda-forge/osx-arm64::bzip2-1.0.8-h93a5062_5
          c-ares             conda-forge/osx-arm64::c-ares-1.25.0-h93a5062_0
          c-blosc2           conda-forge/osx-arm64::c-blosc2-2.12.0-ha57e6be_0
          ca-certificates    conda-forge/osx-arm64::ca-certificates-2023.11.17-hf0a4a13_0
          cairo              conda-forge/osx-arm64::cairo-1.18.0-hd1e100b_0
          cctools_osx-arm64  conda-forge/osx-arm64::cctools_osx-arm64-973.0.1-h62378fb_15
          certifi            conda-forge/noarch::certifi-2023.11.17-pyhd8ed1ab_0
          cffi               conda-forge/osx-arm64::cffi-1.16.0-py312h8e38eb3_0
          charset-normalizer conda-forge/noarch::charset-normalizer-3.3.2-pyhd8ed1ab_0
          clang              conda-forge/osx-arm64::clang-16.0.6-haab561b_4
          clang-16           conda-forge/osx-arm64::clang-16-16.0.6-default_hd209bcb_4
          clang_impl_osx-ar~ conda-forge/osx-arm64::clang_impl_osx-arm64-16.0.6-hc421ffc_8
          clang_osx-arm64    conda-forge/osx-arm64::clang_osx-arm64-16.0.6-h54d7cd3_8
          clangxx            conda-forge/osx-arm64::clangxx-16.0.6-default_h5c94ee4_4
          clangxx_impl_osx-~ conda-forge/osx-arm64::clangxx_impl_osx-arm64-16.0.6-hcd7bac0_8
          clangxx_osx-arm64  conda-forge/osx-arm64::clangxx_osx-arm64-16.0.6-h54d7cd3_8
          compiler-rt        conda-forge/osx-arm64::compiler-rt-16.0.6-h3808999_2
          compiler-rt_osx-a~ conda-forge/noarch::compiler-rt_osx-arm64-16.0.6-h3808999_2
          contourpy          conda-forge/osx-arm64::contourpy-1.2.0-py312h76e736e_0
          cycler             conda-forge/noarch::cycler-0.12.1-pyhd8ed1ab_0
          dav1d              conda-forge/osx-arm64::dav1d-1.2.1-hb547adb_0
          double-conversion  conda-forge/osx-arm64::double-conversion-3.3.0-h13dd4ca_0
          eigen              conda-forge/osx-arm64::eigen-3.4.0-h1995070_0
          expat              conda-forge/osx-arm64::expat-2.5.0-hb7217d7_1
          fenics-basix       conda-forge/osx-arm64::fenics-basix-0.7.0-py312hb23e587_1
          fenics-basix-pybi~ conda-forge/osx-arm64::fenics-basix-pybind11-abi-0.4.16-hfeba48c_1
          fenics-dolfinx     conda-forge/osx-arm64::fenics-dolfinx-0.7.2-py312hcb5ac4e_103
          fenics-ffcx        conda-forge/noarch::fenics-ffcx-0.7.0-pyh4af843d_0
          fenics-libbasix    conda-forge/osx-arm64::fenics-libbasix-0.7.0-hb1687fd_1
          fenics-libdolfinx  conda-forge/osx-arm64::fenics-libdolfinx-0.7.2-h58499c2_103
          fenics-ufcx        conda-forge/noarch::fenics-ufcx-0.7.0-h4af843d_0
          fenics-ufl         conda-forge/noarch::fenics-ufl-2023.2.0-pyhd8ed1ab_0
          ffmpeg             conda-forge/osx-arm64::ffmpeg-6.1.0-gpl_h032c140_102
          fftw               conda-forge/osx-arm64::fftw-3.3.10-mpi_mpich_h0cb5807_8
          font-ttf-dejavu-s~ conda-forge/noarch::font-ttf-dejavu-sans-mono-2.37-hab24e00_0
          font-ttf-inconsol~ conda-forge/noarch::font-ttf-inconsolata-3.000-h77eed37_0
          font-ttf-source-c~ conda-forge/noarch::font-ttf-source-code-pro-2.038-h77eed37_0
          font-ttf-ubuntu    conda-forge/noarch::font-ttf-ubuntu-0.83-h77eed37_1
          fontconfig         conda-forge/osx-arm64::fontconfig-2.14.2-h82840c6_0
          fonts-conda-ecosy~ conda-forge/noarch::fonts-conda-ecosystem-1-0
          fonts-conda-forge  conda-forge/noarch::fonts-conda-forge-1-0
          fonttools          conda-forge/osx-arm64::fonttools-4.47.2-py312he37b823_0
          freetype           conda-forge/osx-arm64::freetype-2.12.1-hadb7bae_2
          fribidi            conda-forge/osx-arm64::fribidi-1.0.10-h27ca646_0
          frozenlist         conda-forge/osx-arm64::frozenlist-1.4.1-py312he37b823_0
          gettext            conda-forge/osx-arm64::gettext-0.21.1-h0186832_0
          gl2ps              conda-forge/osx-arm64::gl2ps-1.4.2-h17b34a0_0
          glew               conda-forge/osx-arm64::glew-2.1.0-h9f76cd9_2
          glib               conda-forge/osx-arm64::glib-2.78.3-h9e231a4_0
          glib-tools         conda-forge/osx-arm64::glib-tools-2.78.3-h9e231a4_0
          gmp                conda-forge/osx-arm64::gmp-6.3.0-h965bd2d_0
          gnutls             conda-forge/osx-arm64::gnutls-3.7.9-hd26332c_0
          graphite2          conda-forge/osx-arm64::graphite2-1.3.13-h9f76cd9_1001
          gst-plugins-base   conda-forge/osx-arm64::gst-plugins-base-1.22.8-h09b4b5e_1
          gstreamer          conda-forge/osx-arm64::gstreamer-1.22.8-h551c6ff_1
          harfbuzz           conda-forge/osx-arm64::harfbuzz-8.3.0-h8f0ba13_0
          hdf4               conda-forge/osx-arm64::hdf4-4.2.15-h2ee6834_7
          hdf5               conda-forge/osx-arm64::hdf5-1.14.3-mpi_mpich_h754b83b_0
          hypre              conda-forge/osx-arm64::hypre-2.28.0-mpi_mpich_hd226f01_0
          icu                conda-forge/osx-arm64::icu-73.2-hc8870d7_0
          idna               conda-forge/noarch::idna-3.6-pyhd8ed1ab_0
          jsoncpp            conda-forge/osx-arm64::jsoncpp-1.9.5-hc021e02_1
          kahip              conda-forge/osx-arm64::kahip-3.16-py312h18d51ab_0
          kahip-python       conda-forge/osx-arm64::kahip-python-3.16-py312h2c784d2_0
          kiwisolver         conda-forge/osx-arm64::kiwisolver-1.4.5-py312h389731b_1
          krb5               conda-forge/osx-arm64::krb5-1.21.2-h92f50d5_0
          lame               conda-forge/osx-arm64::lame-3.100-h1a8c8d9_1003
          lcms2              conda-forge/osx-arm64::lcms2-2.16-ha0e7c42_0
          ld64_osx-arm64     conda-forge/osx-arm64::ld64_osx-arm64-609-ha4bd21c_15
          lerc               conda-forge/osx-arm64::lerc-4.0.0-h9a09cb3_0
          libadios2          conda-forge/osx-arm64::libadios2-2.9.2-mpi_mpich_h07a8d79_1
          libaec             conda-forge/osx-arm64::libaec-1.1.2-h13dd4ca_1
          libass             conda-forge/osx-arm64::libass-0.17.1-hf7da4fe_1
          libblas            conda-forge/osx-arm64::libblas-3.9.0-20_osxarm64_openblas
          libboost           conda-forge/osx-arm64::libboost-1.82.0-h72cdd8a_6
          libboost-devel     conda-forge/osx-arm64::libboost-devel-1.82.0-hf450f58_6
          libboost-headers   conda-forge/osx-arm64::libboost-headers-1.82.0-hce30654_6
          libbrotlicommon    conda-forge/osx-arm64::libbrotlicommon-1.1.0-hb547adb_1
          libbrotlidec       conda-forge/osx-arm64::libbrotlidec-1.1.0-hb547adb_1
          libbrotlienc       conda-forge/osx-arm64::libbrotlienc-1.1.0-hb547adb_1
          libcblas           conda-forge/osx-arm64::libcblas-3.9.0-20_osxarm64_openblas
          libclang           conda-forge/osx-arm64::libclang-15.0.7-default_hd209bcb_4
          libclang-cpp16     conda-forge/osx-arm64::libclang-cpp16-16.0.6-default_hd209bcb_4
          libclang13         conda-forge/osx-arm64::libclang13-15.0.7-default_ha49e599_4
          libcurl            conda-forge/osx-arm64::libcurl-8.5.0-h2d989ff_0
          libcxx             conda-forge/osx-arm64::libcxx-16.0.6-h4653b0c_0
          libdeflate         conda-forge/osx-arm64::libdeflate-1.19-hb547adb_0
          libedit            conda-forge/osx-arm64::libedit-3.1.20191231-hc8eb9b7_2
          libev              conda-forge/osx-arm64::libev-4.33-h93a5062_2
          libexpat           conda-forge/osx-arm64::libexpat-2.5.0-hb7217d7_1
          libffi             conda-forge/osx-arm64::libffi-3.4.2-h3422bc3_5
          libgfortran        conda-forge/osx-arm64::libgfortran-5.0.0-13_2_0_hd922786_1
          libgfortran5       conda-forge/osx-arm64::libgfortran5-13.2.0-hf226fd6_1
          libglib            conda-forge/osx-arm64::libglib-2.78.3-hb438215_0
          libhwloc           conda-forge/osx-arm64::libhwloc-2.9.3-default_h4394839_1009
          libiconv           conda-forge/osx-arm64::libiconv-1.17-h0d3ecfb_2
          libidn2            conda-forge/osx-arm64::libidn2-2.3.4-h1a8c8d9_0
          libjpeg-turbo      conda-forge/osx-arm64::libjpeg-turbo-3.0.0-hb547adb_1
          liblapack          conda-forge/osx-arm64::liblapack-3.9.0-20_osxarm64_openblas
          libllvm15          conda-forge/osx-arm64::libllvm15-15.0.7-h504e6bf_3
          libllvm16          conda-forge/osx-arm64::libllvm16-16.0.6-he79909e_2
          libnetcdf          conda-forge/osx-arm64::libnetcdf-4.9.2-nompi_hb2fb864_112
          libnghttp2         conda-forge/osx-arm64::libnghttp2-1.58.0-ha4dd798_1
          libogg             conda-forge/osx-arm64::libogg-1.3.4-h27ca646_1
          libopenblas        conda-forge/osx-arm64::libopenblas-0.3.25-openmp_h6c19121_0
          libopus            conda-forge/osx-arm64::libopus-1.3.1-h27ca646_1
          libpng             conda-forge/osx-arm64::libpng-1.6.39-h76d750c_0
          libpq              conda-forge/osx-arm64::libpq-16.1-h0f8b458_7
          libptscotch        conda-forge/osx-arm64::libptscotch-7.0.4-h5340af2_1
          libscotch          conda-forge/osx-arm64::libscotch-7.0.4-hc938e73_1
          libsodium          conda-forge/osx-arm64::libsodium-1.0.18-h27ca646_1
          libsqlite          conda-forge/osx-arm64::libsqlite-3.44.2-h091b4b1_0
          libssh2            conda-forge/osx-arm64::libssh2-1.11.0-h7a5bd25_0
          libtasn1           conda-forge/osx-arm64::libtasn1-4.19.0-h1a8c8d9_0
          libtheora          conda-forge/osx-arm64::libtheora-1.1.1-h3422bc3_1005
          libtiff            conda-forge/osx-arm64::libtiff-4.6.0-ha8a6c65_2
          libunistring       conda-forge/osx-arm64::libunistring-0.9.10-h3422bc3_0
          libvorbis          conda-forge/osx-arm64::libvorbis-1.3.7-h9f76cd9_0
          libvpx             conda-forge/osx-arm64::libvpx-1.13.1-hb765f3a_0
          libwebp-base       conda-forge/osx-arm64::libwebp-base-1.3.2-hb547adb_0
          libxcb             conda-forge/osx-arm64::libxcb-1.15-hf346824_0
          libxml2            conda-forge/osx-arm64::libxml2-2.11.6-h0d0cfa8_0
          libzip             conda-forge/osx-arm64::libzip-1.10.1-ha0bc3c6_3
          libzlib            conda-forge/osx-arm64::libzlib-1.2.13-h53f4e23_5
          llvm-openmp        conda-forge/osx-arm64::llvm-openmp-17.0.6-hcd81f8e_0
          llvm-tools         conda-forge/osx-arm64::llvm-tools-16.0.6-he79909e_2
          loguru             conda-forge/osx-arm64::loguru-0.7.2-py312h81bd7bf_1
          lz4-c              conda-forge/osx-arm64::lz4-c-1.9.4-hb7217d7_0
          matplotlib-base    conda-forge/osx-arm64::matplotlib-base-3.8.2-py312hba9b818_0
          metis              conda-forge/osx-arm64::metis-5.1.1-h965bd2d_2
          mpfr               conda-forge/osx-arm64::mpfr-4.2.1-h9546428_0
          mpi                conda-forge/osx-arm64::mpi-1.0-mpich
          mpi4py             conda-forge/osx-arm64::mpi4py-3.1.5-py312h8d05a6a_0
          mpich              conda-forge/osx-arm64::mpich-4.1.2-hd4b5bf3_101
          multidict          conda-forge/osx-arm64::multidict-6.0.4-py312h670c8ac_1
          mumps-include      conda-forge/osx-arm64::mumps-include-5.2.1-hce30654_14
          mumps-mpi          conda-forge/osx-arm64::mumps-mpi-5.2.1-hfea86b6_14
          munkres            conda-forge/noarch::munkres-1.1.4-pyh9f0ad1d_0
          mysql-common       conda-forge/osx-arm64::mysql-common-8.0.33-hf9e6398_6
          mysql-libs         conda-forge/osx-arm64::mysql-libs-8.0.33-he3dca8b_6
          ncurses            conda-forge/osx-arm64::ncurses-6.4-h463b476_2
          nettle             conda-forge/osx-arm64::nettle-3.9.1-h40ed0f5_0
          nlohmann_json      conda-forge/osx-arm64::nlohmann_json-3.11.2-h2e04ded_0
          nspr               conda-forge/osx-arm64::nspr-4.35-hb7217d7_0
          nss                conda-forge/osx-arm64::nss-3.96-h5ce2875_0
          numpy              conda-forge/osx-arm64::numpy-1.26.3-py312h8442bc7_0
          openh264           conda-forge/osx-arm64::openh264-2.4.0-h965bd2d_0
          openjpeg           conda-forge/osx-arm64::openjpeg-2.5.0-h4c1507b_3
          openssl            conda-forge/osx-arm64::openssl-3.2.0-h0d3ecfb_1
          p11-kit            conda-forge/osx-arm64::p11-kit-0.24.1-h29577a5_0
          packaging          conda-forge/noarch::packaging-23.2-pyhd8ed1ab_0
          parmetis           conda-forge/osx-arm64::parmetis-4.0.3-hefa2a9d_1005
          pcre2              conda-forge/osx-arm64::pcre2-10.42-h26f9a81_0
          petsc              conda-forge/osx-arm64::petsc-3.20.3-real_hccfcfac_100
          petsc4py           conda-forge/osx-arm64::petsc4py-3.20.3-real_hd567e68_100
          pillow             conda-forge/osx-arm64::pillow-10.2.0-py312hac22aec_0
          pip                conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0
          pixman             conda-forge/osx-arm64::pixman-0.43.0-hebf3989_0
          pkg-config         conda-forge/osx-arm64::pkg-config-0.29.2-hab62308_1008
          platformdirs       conda-forge/noarch::platformdirs-4.1.0-pyhd8ed1ab_0
          pooch              conda-forge/noarch::pooch-1.8.0-pyhd8ed1ab_0
          proj               conda-forge/osx-arm64::proj-9.3.1-h93d94ba_0
          pthread-stubs      conda-forge/osx-arm64::pthread-stubs-0.4-h27ca646_1001
          ptscotch           conda-forge/osx-arm64::ptscotch-7.0.4-heaa5b5c_1
          pugixml            conda-forge/osx-arm64::pugixml-1.14-h13dd4ca_0
          pybind11-abi       conda-forge/noarch::pybind11-abi-4-hd8ed1ab_3
          pycparser          conda-forge/noarch::pycparser-2.21-pyhd8ed1ab_0
          pyparsing          conda-forge/noarch::pyparsing-3.1.1-pyhd8ed1ab_0
          pysocks            conda-forge/noarch::pysocks-1.7.1-pyha2e5f31_6
          python             conda-forge/osx-arm64::python-3.12.1-hdf0ec26_1_cpython
          python-dateutil    conda-forge/noarch::python-dateutil-2.8.2-pyhd8ed1ab_0
          python_abi         conda-forge/osx-arm64::python_abi-3.12-4_cp312
          pyvista            conda-forge/noarch::pyvista-0.43.1-pyhd8ed1ab_0
          qt-main            conda-forge/osx-arm64::qt-main-5.15.8-h0a21348_18
          readline           conda-forge/osx-arm64::readline-8.2-h92ec313_1
          requests           conda-forge/noarch::requests-2.31.0-pyhd8ed1ab_0
          scalapack          conda-forge/osx-arm64::scalapack-2.2.0-hb170938_1
          scooby             conda-forge/noarch::scooby-0.9.2-pyhd8ed1ab_0
          scotch             conda-forge/osx-arm64::scotch-7.0.4-heaa5b5c_1
          setuptools         conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0
          sigtool            conda-forge/osx-arm64::sigtool-0.1.3-h44b9a77_0
          six                conda-forge/noarch::six-1.16.0-pyh6c4a22f_0
          slepc              conda-forge/osx-arm64::slepc-3.20.1-real_hadb8a15_100
          slepc4py           conda-forge/osx-arm64::slepc4py-3.20.1-real_hec853a8_100
          snappy             conda-forge/osx-arm64::snappy-1.1.10-h17c5cce_0
          sqlite             conda-forge/osx-arm64::sqlite-3.44.2-hf2abe2d_0
          suitesparse        conda-forge/osx-arm64::suitesparse-5.10.1-h88be0ae_2
          superlu            conda-forge/osx-arm64::superlu-5.2.2-hc615359_0
          superlu_dist       conda-forge/osx-arm64::superlu_dist-8.2.1-h6be7e34_0
          svt-av1            conda-forge/osx-arm64::svt-av1-1.7.0-hb765f3a_0
          tapi               conda-forge/osx-arm64::tapi-1100.0.11-he4954df_0
          tbb                conda-forge/osx-arm64::tbb-2021.11.0-h6aa02a4_0
          tbb-devel          conda-forge/osx-arm64::tbb-devel-2021.11.0-ha552a60_0
          tk                 conda-forge/osx-arm64::tk-8.6.13-h5083fa2_1
          tzdata             conda-forge/noarch::tzdata-2023d-h0c530f3_0
          urllib3            conda-forge/noarch::urllib3-2.1.0-pyhd8ed1ab_0
          utfcpp             conda-forge/osx-arm64::utfcpp-4.0.5-hce30654_0
          vtk                conda-forge/osx-arm64::vtk-9.2.6-qt_py312h1234567_220
          vtk-base           conda-forge/osx-arm64::vtk-base-9.2.6-qt_py312h1234567_220
          vtk-io-ffmpeg      conda-forge/osx-arm64::vtk-io-ffmpeg-9.2.6-qt_py312h1234567_220
          wheel              conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0
          wslink             conda-forge/noarch::wslink-1.12.4-pyhd8ed1ab_0
          x264               conda-forge/osx-arm64::x264-1!164.3095-h57fd34a_2
          x265               conda-forge/osx-arm64::x265-3.5-hbc6ce65_3
          xorg-libxau        conda-forge/osx-arm64::xorg-libxau-1.0.11-hb547adb_0
          xorg-libxdmcp      conda-forge/osx-arm64::xorg-libxdmcp-1.1.3-h27ca646_0
          xz                 conda-forge/osx-arm64::xz-5.2.6-h57fd34a_0
          yaml               conda-forge/osx-arm64::yaml-0.2.5-h3422bc3_2
          yarl               conda-forge/osx-arm64::yarl-1.9.3-py312he37b823_0
          zeromq             conda-forge/osx-arm64::zeromq-4.3.5-h965bd2d_0
          zfp                conda-forge/osx-arm64::zfp-0.5.5-hcfdfaf5_8
          zlib               conda-forge/osx-arm64::zlib-1.2.13-h53f4e23_5
          zlib-ng            conda-forge/osx-arm64::zlib-ng-2.0.7-h1a8c8d9_0
          zstd               conda-forge/osx-arm64::zstd-1.5.5-h4f39d0f_0
    
        Proceed ([y]/n)? y
    
        Downloading and Extracting Packages:
    
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
    
    which python
        /Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/bin/python
    python --version
        Python 3.12.1
    python -c "import platform; print(platform.processor())"
        arm
    
    python -c 'import dolfinx; print(f"DOLFINx version: {dolfinx.__version__} based on GIT commit: {dolfinx.git_commit_hash} of https://github.com/FEniCS/dolfinx/")'
        DOLFINx version: 0.7.2 based on GIT commit:  of https://github.com/FEniCS/dolfinx/
    
    python diffusion_2D.py
        Traceback (most recent call last):
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/spawn.py", line 57, in spawn
            proc = subprocess.Popen(cmd, env=env)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/subprocess.py", line 1026, in __init__
            self._execute_child(args, executable, preexec_fn, close_fds,
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/subprocess.py", line 1950, in _execute_child
            raise child_exception_type(errno_num, err_msg, err_filename)
        FileNotFoundError: [Errno 2] No such file or directory: 'x86_64-apple-darwin13.4.0-clang'
    
        The above exception was the direct cause of the following exception:
    
        Traceback (most recent call last):
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/unixccompiler.py", line 185, in _compile
            self.spawn(compiler_so + cc_args + [src, '-o', obj] + extra_postargs)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/ccompiler.py", line 1041, in spawn
            spawn(cmd, dry_run=self.dry_run, **kwargs)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/spawn.py", line 63, in spawn
            raise DistutilsExecError(
        distutils.errors.DistutilsExecError: command 'x86_64-apple-darwin13.4.0-clang' failed: No such file or directory
    
        During handling of the above exception, another exception occurred:
    
        Traceback (most recent call last):
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/cffi/ffiplatform.py", line 48, in _build
            dist.run_command('build_ext')
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/dist.py", line 963, in run_command
            super().run_command(command)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/dist.py", line 988, in run_command
            cmd_obj.run()
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/command/build_ext.py", line 88, in run
            _build_ext.run(self)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/command/build_ext.py", line 345, in run
            self.build_extensions()
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/command/build_ext.py", line 467, in build_extensions
            self._build_extensions_serial()
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/command/build_ext.py", line 493, in _build_extensions_serial
            self.build_extension(ext)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/command/build_ext.py", line 249, in build_extension
            _build_ext.build_extension(self, ext)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/command/build_ext.py", line 548, in build_extension
            objects = self.compiler.compile(
                      ^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/ccompiler.py", line 600, in compile
            self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/setuptools/_distutils/unixccompiler.py", line 187, in _compile
            raise CompileError(msg)
        distutils.errors.CompileError: command 'x86_64-apple-darwin13.4.0-clang' failed: No such file or directory
    
        During handling of the above exception, another exception occurred:
    
        Traceback (most recent call last):
          File "/Users/nordin/Documents/Projects/2024_projects/doflinx_2D_diffusion/diffusion_2D.py", line 24, in <module>
            V = fem.FunctionSpace(domain, ("Lagrange", 1))
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/dolfinx/fem/function.py", line 581, in FunctionSpace
            return functionspace(mesh, element, form_compiler_options, jit_options)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/dolfinx/fem/function.py", line 541, in functionspace
            (ufcx_element, ufcx_dofmap), module, code = jit.ffcx_jit(mesh.comm, ufl_e,
                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/dolfinx/jit.py", line 56, in mpi_jit
            return local_jit(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/dolfinx/jit.py", line 206, in ffcx_jit
            r = ffcx.codegeneration.jit.compile_elements([ufl_object], options=p_ffcx, **p_jit)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/ffcx/codegeneration/jit.py", line 154, in compile_elements
            raise e
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/ffcx/codegeneration/jit.py", line 145, in compile_elements
            impl = _compile_objects(decl, elements, names, module_name, p, cache_dir,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/ffcx/codegeneration/jit.py", line 284, in _compile_objects
            ffibuilder.compile(tmpdir=cache_dir, verbose=True, debug=cffi_debug)
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/cffi/api.py", line 725, in compile
            return recompile(self, module_name, source, tmpdir=tmpdir,
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/cffi/recompiler.py", line 1564, in recompile
            outputfilename = ffiplatform.compile('.', ext,
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/cffi/ffiplatform.py", line 20, in compile
            outputfilename = _build(tmpdir, ext, compiler_verbose, debug)
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File "/Users/nordin/opt/miniconda3/envs/fenicsx-env-temp2/lib/python3.12/site-packages/cffi/ffiplatform.py", line 54, in _build
            raise VerificationError('%s: %s' % (e.__class__.__name__, e))
        cffi.VerificationError: CompileError: command 'x86_64-apple-darwin13.4.0-clang' failed: No such file or directory

## Alternatively, 

