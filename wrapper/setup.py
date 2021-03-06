from distutils.core import setup, Extension

import os, sys

libraries = ['OpenVG']
extra_objects = list()

if sys.platform.startswith('darwin'):
	os.environ['LDFLAGS'] = '-g -framework GLUT -framework OpenGL -framework Cocoa'

elif sys.platform.startswith('linux'):
	libraries.extend(['glut', 'GL', 'GLU'])

	extra_objects.extend([
		'../src/libOpenVG_la-shArrays.o',
		'../src/libOpenVG_la-shContext.o',
		'../src/libOpenVG_la-shExtensions.o',
		'../src/libOpenVG_la-shGeometry.o',
		'../src/libOpenVG_la-shImage.o',
		'../src/libOpenVG_la-shPaint.o',
		'../src/libOpenVG_la-shParams.o',
		'../src/libOpenVG_la-shPath.o',
		'../src/libOpenVG_la-shPipeline.o',
		'../src/libOpenVG_la-shVectors.o',
		'../src/libOpenVG_la-shVgu.o'])

 
pyshiva_module = Extension('pyshiva',
	include_dirs = ['../include'],
	sources = ['wrapper.c','pyShivamodule.c'],
	libraries = libraries,
	extra_objects = extra_objects)

setup (name = 'pyshiva',
        version = '1.0',
        description = 'Test package for pyShiva',
        ext_modules = [pyshiva_module])
