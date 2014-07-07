# encoding: utf-8
"""
gites.pivot.db

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from datetime import datetime

import argparse
import os
import paramiko
import subprocess


def main():
    desc = 'Get pivot database archive'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p', dest='path', help=u'dump location',
                        default='/var/www/pivotweb')
    parser.add_argument('-s', dest='server', help=u'ssh server',
                        default='pivot.interne.gitesdewallonie.be')
    parser.add_argument('-u', dest='user', help=u'ssh user',
                        default='pivot')

    args = parser.parse_args()
    pivot_archive = PivotArchive(args.path, args.server, args.user)
    return pivot_archive.get()


class PivotArchive(object):

    def __init__(self, path, server, user):
        self.path = path
        self.server = server
        self.user = user
        self.ssh = paramiko.SSHClient()

    def get(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.server, username=self.user)
        return self.scp_last_file()

    def scp_last_file(self):
        last_file = self.get_last_file()
        c_args = ['scp', '{0}@{1}:{2}/{3}'.format(self.user, self.server,
                                                  self.path, last_file),
                  '/tmp/pivot/']
        if os.path.exists('/tmp/pivot') is False:
            os.mkdir('/tmp/pivot')
        proc = subprocess.Popen(c_args, stdout=subprocess.PIPE)
        proc.communicate()
        archive = '/tmp/pivot/{0}'.format(last_file)
        if os.path.exists(archive) is False:
            raise ValueError('Missing file {0}'.format(archive))
        return archive

    def get_last_file(self):
        cmd = 'ls -alrt {0}'.format(self.path)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = stdout.read().splitlines()
        if len(result) < 3:
            raise ValueError('invalid result')
        last_file = result[-2].split(' ')[-1]
        date = datetime.strptime(last_file.split('-')[-1], '%Y%m%d%H%M.tar.gz')
        if datetime.now().date() != date.date():
            raise ValueError('invalid date')
        return last_file
