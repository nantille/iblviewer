from setuptools import setup, find_packages

setup(
    name = 'iblviewer', 
    version='2.0.0',   
    description='An interactive GPU-accelerated 3D viewer based on VTK',
    url='https://github.com/int-brain-lab/iblviewer',
    author='Nicolas Antille',
    author_email='nicolas.antille@gmail.com',
    license='MIT',
    packages=find_packages(include=['iblviewer','iblviewer.*']),
    install_requires=['numpy',
                      'matplotlib',
                      'pandas',
                      'pynrrd',
                      'trimesh',
                      'k3d',
                      'vtk>=9.0',
                      #'ibllib>=1.6.0',
                      'vedo>=2021.0.3',
                      'ipyvtklink',
                      ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.8',
    ],
)