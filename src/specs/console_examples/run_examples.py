from cStringIO import StringIO
from should_dsl import should_be
import subprocess


bowling_game_output = open('bowling_game_output').read()
bowling_game_pending_output = open('bowling_game_pending_output').read()
bowling_game_without_colors_output = open('bowling_game_without_colors_output').read()
calculator_output = open('calculator_output').read()
bowling_and_calculator_output = bowling_game_output + '\n\n' + calculator_output

INPUTS_AND_OUTPUTS = [('pycukes specs/bowling_game.story',
                            bowling_game_output),
                      ('pycukes specs/bowling_game.story specs/calculator.story',
                            bowling_and_calculator_output),
                      ('pycukes',
                            bowling_and_calculator_output),
                      ('pycukes --specs-dir=features',
                            ''),
                      ('pycukes --specs-dir=specs_dir1',
                            bowling_game_output),
                      ('pycukes --specs-dir=specs_dir1 --steps-dir=steps_dir1',
                            bowling_game_pending_output),
                      ('pycukes specs/bowling_game.story --no-colors',
                            bowling_game_without_colors_output),]

def run_examples():
    exceptions = []
    for input_command, expected_output in INPUTS_AND_OUTPUTS:
        print '\t', input_command,
        try:
            out = subprocess.Popen(input_command,
                                   stdout=subprocess.PIPE,
                                   shell=True).communicate()[0]
            out |should_be.equal_to| expected_output
            print '- OK'
        except AssertionError, e:
            print '- FAIL'
            print e

if __name__ == '__main__':
    print '-'*80
    print 'Running console examples'
    run_examples()
