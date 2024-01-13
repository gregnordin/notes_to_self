

# 1/12/24 quick notes

## Problem

My conda installation on my Apple Silicon macbook pro is for Intel x86 architecture. Until I can take the time to completely wipe it and start over, how can I create ARM -specific conda environments?

## Solution

See last case below.

## Only `conda create`

Creating a fresh conda environment does not include a python instance:

    conda create -n temp
        Retrieving notices: ...working... done
        Collecting package metadata (current_repodata.json): done
        Solving environment: done
    
        ## Package Plan ##
    
          environment location: /Users/nordin/opt/miniconda3/envs/temp
    
        Proceed ([y]/n)? y
    
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        #
        # To activate this environment, use
        #
        #     $ conda activate temp
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
    
    conda activate temp
    which python
    
    python --version
        bash: python: command not found
    
    # Delete environment
    conda deactivate
    conda env remove -n temp

## `conda create` with python &rarr; `i386`

Specifying only `python` includes a recent version of python:

    conda create -n temp python
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
    
          environment location: /Users/nordin/opt/miniconda3/envs/temp
    
          added / updated specs:
            - python
    
        The following packages will be downloaded:
    
            package                    |            build
            ---------------------------|-----------------
            ca-certificates-2023.12.12 |       hecd8cb5_0         127 KB
            expat-2.5.0                |       hcec6c5f_0         140 KB
            openssl-3.0.12             |       hca72f7f_0         4.5 MB
            pip-23.3.1                 |  py312hecd8cb5_0         2.8 MB
            python-3.12.0              |       hd58486a_0        14.2 MB
            setuptools-68.2.2          |  py312hecd8cb5_0         1.2 MB
            tzdata-2023d               |       h04d1e81_0         117 KB
            wheel-0.41.2               |  py312hecd8cb5_0         131 KB
            xz-5.4.5                   |       h6c40b1e_0         366 KB
            ------------------------------------------------------------
                                                   Total:        23.6 MB
    
        The following NEW packages will be INSTALLED:
    
          bzip2              pkgs/main/osx-64::bzip2-1.0.8-h1de35cc_0
          ca-certificates    pkgs/main/osx-64::ca-certificates-2023.12.12-hecd8cb5_0
          expat              pkgs/main/osx-64::expat-2.5.0-hcec6c5f_0
          libcxx             pkgs/main/osx-64::libcxx-14.0.6-h9765a3e_0
          libffi             pkgs/main/osx-64::libffi-3.4.4-hecd8cb5_0
          ncurses            pkgs/main/osx-64::ncurses-6.4-hcec6c5f_0
          openssl            pkgs/main/osx-64::openssl-3.0.12-hca72f7f_0
          pip                pkgs/main/osx-64::pip-23.3.1-py312hecd8cb5_0
          python             pkgs/main/osx-64::python-3.12.0-hd58486a_0
          readline           pkgs/main/osx-64::readline-8.2-hca72f7f_0
          setuptools         pkgs/main/osx-64::setuptools-68.2.2-py312hecd8cb5_0
          sqlite             pkgs/main/osx-64::sqlite-3.41.2-h6c40b1e_0
          tk                 pkgs/main/osx-64::tk-8.6.12-h5d9f67b_0
          tzdata             pkgs/main/noarch::tzdata-2023d-h04d1e81_0
          wheel              pkgs/main/osx-64::wheel-0.41.2-py312hecd8cb5_0
          xz                 pkgs/main/osx-64::xz-5.4.5-h6c40b1e_0
          zlib               pkgs/main/osx-64::zlib-1.2.13-h4dc903c_0
    
        Proceed ([y]/n)? y
    
        Downloading and Extracting Packages:
    
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        #
        # To activate this environment, use
        #
        #     $ conda activate temp
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
    
    conda activate temp
    which python
        /Users/nordin/opt/miniconda3/envs/temp/bin/python
    python --version
        Python 3.12.0
    python -c "import platform; print(platform.processor())"
    	i386
    
    conda deactivate
    conda env remove -n temp

## `conda create` with `CONDA_SUBDIR` set &rarr; `arm`

    CONDA_SUBDIR=osx-arm64 conda create -n temp python
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
    
          environment location: /Users/nordin/opt/miniconda3/envs/temp
    
          added / updated specs:
            - python
    
        The following packages will be downloaded:
    
            package                    |            build
            ---------------------------|-----------------
            bzip2-1.0.8                |       h620ffc9_4         109 KB
            ca-certificates-2023.12.12 |       hca03da5_0         127 KB
            expat-2.5.0                |       h313beb8_0         144 KB
            libcxx-14.0.6              |       h848a8c0_0         965 KB
            libffi-3.4.4               |       hca03da5_0         120 KB
            ncurses-6.4                |       h313beb8_0         884 KB
            openssl-3.0.12             |       h1a28f6b_0         4.3 MB
            pip-23.3.1                 |  py312hca03da5_0         2.8 MB
            python-3.12.0              |       h99e199e_0        14.0 MB
            readline-8.2               |       h1a28f6b_0         353 KB
            setuptools-68.2.2          |  py312hca03da5_0         1.2 MB
            sqlite-3.41.2              |       h80987f9_0         1.1 MB
            tk-8.6.12                  |       hb8d0fd4_0         2.9 MB
            wheel-0.41.2               |  py312hca03da5_0         133 KB
            xz-5.4.5                   |       h80987f9_0         366 KB
            zlib-1.2.13                |       h5a0b063_0          82 KB
            ------------------------------------------------------------
                                                   Total:        29.5 MB
    
        The following NEW packages will be INSTALLED:
    
          bzip2              pkgs/main/osx-arm64::bzip2-1.0.8-h620ffc9_4
          ca-certificates    pkgs/main/osx-arm64::ca-certificates-2023.12.12-hca03da5_0
          expat              pkgs/main/osx-arm64::expat-2.5.0-h313beb8_0
          libcxx             pkgs/main/osx-arm64::libcxx-14.0.6-h848a8c0_0
          libffi             pkgs/main/osx-arm64::libffi-3.4.4-hca03da5_0
          ncurses            pkgs/main/osx-arm64::ncurses-6.4-h313beb8_0
          openssl            pkgs/main/osx-arm64::openssl-3.0.12-h1a28f6b_0
          pip                pkgs/main/osx-arm64::pip-23.3.1-py312hca03da5_0
          python             pkgs/main/osx-arm64::python-3.12.0-h99e199e_0
          readline           pkgs/main/osx-arm64::readline-8.2-h1a28f6b_0
          setuptools         pkgs/main/osx-arm64::setuptools-68.2.2-py312hca03da5_0
          sqlite             pkgs/main/osx-arm64::sqlite-3.41.2-h80987f9_0
          tk                 pkgs/main/osx-arm64::tk-8.6.12-hb8d0fd4_0
          tzdata             pkgs/main/noarch::tzdata-2023d-h04d1e81_0
          wheel              pkgs/main/osx-arm64::wheel-0.41.2-py312hca03da5_0
          xz                 pkgs/main/osx-arm64::xz-5.4.5-h80987f9_0
          zlib               pkgs/main/osx-arm64::zlib-1.2.13-h5a0b063_0
    
        Proceed ([y]/n)? y
    
        Downloading and Extracting Packages:
    
        Preparing transaction: done
        Verifying transaction: done
        Executing transaction: done
        #
        # To activate this environment, use
        #
        #     $ conda activate temp
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate
    
    conda activate temp
    which python
        /Users/nordin/opt/miniconda3/envs/temp/bin/python
    python -c "import platform; print(platform.processor())"
        arm
    python --version
        Python 3.12.0
    
    conda deactivate
    conda env remove -n temp