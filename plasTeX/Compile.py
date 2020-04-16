#!/usr/bin/env python

import os, sys, string, glob
import importlib
import plasTeX
from plasTeX.TeX import TeX
from plasTeX.ConfigManager import *
from plasTeX.Logging import getLogger, updateLogLevels

log = getLogger()

def run(filename: str, config: ConfigManager):
    if config['logging']:
        updateLogLevels(config['logging'])

    # Create document instance that output will be put into
    document = plasTeX.TeXDocument(config=config)

    # Instantiate the TeX processor and parse the document
    tex = TeX(document, myfile=filename)

    # Send log message to file "jobname.log" instead of console
    if config['files']['log']:
        tex.fileLogging()

    # Populate variables for use later
    if config['document']['title']:
        document.userdata['title'] = config['document']['title']

    jobname = document.userdata['jobname'] = tex.jobname
    cwd = document.userdata['working-dir'] = os.getcwd()

    # Load aux files for cross-document references
    pauxname = '%s.paux' % jobname
    rname = config['general']['renderer']
    for dirname in [cwd] + config['general']['paux-dirs']:
        for fname in glob.glob(os.path.join(dirname, '*.paux')):
            if os.path.basename(fname) == pauxname:
                continue
            document.context.restore(fname, rname)

    # Parse the document
    tex.parse()

    # Set up TEXINPUTS to include the current directory for the renderer
    os.environ['TEXINPUTS'] = '%s%s%s%s' % (os.getcwd(), os.pathsep,
                                         os.environ.get('TEXINPUTS',''), os.pathsep)

    # Change to specified directory to output to
    outdir = config['files']['directory']
    if outdir:
        outdir = string.Template(outdir).substitute({'jobname':jobname})
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        log.info('Directing output files to directory: %s.' % outdir)
        os.chdir(outdir)

    # Load renderer
    try:
        rmodule = importlib.import_module('plasTeX.Renderers.'+rname)
    except ImportError as msg:
        log.error('Could not import renderer "%s".  Make sure that it is installed correctly, and can be imported by Python.' % rname)
        raise msg

    # Write expanded source file
    #sourcefile = '%s.source' % jobname
    #open(sourcefile,'w').write(document.source.encode('utf-8'))

    # Write XML dump
    if config['general']['xml']:
        outfile = '%s.xml' % jobname
        with open(outfile,'w',encoding='utf-8') as f:
            f.write(document.toXML())

    # Apply renderer
    rmodule.Renderer().render(document)

    os.chdir(cwd)
    print()