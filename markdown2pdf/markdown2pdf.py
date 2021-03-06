#!/usr/bin/env python

import argparse
import os

import misaka
import weasyprint


def convert_md_2_pdf(filename, output=None, theme=None):
    with open(filename, 'r') as mdfile:
        html = misaka.html(mdfile.read(), extensions=['autolink', 'tables'])

    if not output:
        output = '.'.join([filename.rsplit('.')[0], 'pdf'])

    if not os.path.exists(theme):
        theme = os.path.join(
            os.environ['VIRTUAL_ENV'],  # <= might not exist
            os.path.dirname(__file__),
            'themes/' + theme + '.css',
        )
    weasyprint.HTML(string=html).write_pdf(output, stylesheets=[theme])


def main():
    parser = argparse.ArgumentParser(
        description='Convert markdown file to pdf')
    parser.add_argument('filename', help='Markdown file name')
    parser.add_argument(
        '--theme',
        help='Set the theme, default is GitHub flavored.',
        default='github'
    )
    parser.add_argument(
        '--output',
        help='''
            The output file name. If not set, the name will
            be same as the input file but with ".pdf".
        '''
    )
    args = parser.parse_args()
    convert_md_2_pdf(**dict(args._get_kwargs()))
