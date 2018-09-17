"""
For testing console programs using pytest.
"""

import subprocess
import os

expected = """
--- FROM USER ---
antranig,1
cwen,5
david.horwitz,4
gopal.ramasammycook,1
gsilver,3
louis,3
ray,1
rjlowe,2
stephen.marquard,2
wagnermr,1
zqian,4
--- FROM HOST ---
caret.cam.ac.uk,1
gmail.com,1
iupui.edu,8
media.berkeley.edu,4
uct.ac.za,6
umich.edu,7
--- TO USER ---
source,27
--- TO HOST ---
collab.sakaiproject.org,27
"""

def test_output():
    '''Test output.'''
    # use Popen to launch the Python script
    sp = subprocess.Popen(['python', 'fromto.py'], bufsize=1,
         universal_newlines=True,
         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # enter the inputs
    stdout, stderr = sp.communicate('')
    # check outputs
    assert stdout.strip() == expected.strip()
    assert stderr == ''

if __name__ == '__main__':
    test_output()
