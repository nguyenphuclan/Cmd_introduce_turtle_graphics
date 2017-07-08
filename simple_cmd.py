import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    # Doan gioi thieu, co the ghi de: cmdloop(intro = 'please')
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
	# Dau nhac dong lenh 
    prompt = '(turtle) '
    file = None
    # Ve duong phan cach duoi help-message 
    ruler = '='

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        forward(*parse(arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        right(*parse(arg))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        left(*parse(arg))
    def do_goto(self, arg):
        'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
        goto(*parse(arg))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        home()
    def do_setpos(self, arg):
	    'Thiet lap vi tri ban dau: SETPOS 10 20'
	    setpos(*parse(arg))
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        circle(*parse(arg))
    def do_shearfactor(self, arg):
        'Lat cat cua hinh: SHEARFACTOR 0.5'
        shearfactor(*parse(arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % position())
    def do_seth(self, arg):
        'Thiet lap huong ban dau con rua: SETH 90'
        seth(*parse(arg))
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (heading(),))
    def do_color(self, arg):
        'Set the color:  COLOR BLUE'
        color(arg.lower())
    def do_shape(self, arg):
        'Tao hinh dang: SHAPE TURTLE/CIRCLE/ARROW/SQUARE/TRIANGLE/CLASSIC'
        shape(arg.lower())
    def do_delay(self, arg):
        'Tao do tre: DELAY 10'
        delay(*parse(arg))
    def do_back(self, arg):
        'Di lui: BACK 10'
        back(*parse(arg))
    def do_clear(self, arg):
        'Xoa dau vet: CLEAR'
        clear()
    def do_speed(self, arg):
        'Tao toc do di chuyen 1->10: SPEED 3'
        speed(*parse(arg))
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        reset()
    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.close()
        bye()
        return True

    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        # Danh sach dong lenh theo thu tu 
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def emptyline(self):
        return
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()