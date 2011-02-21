import argparse

class Management(object):

    #{{{def __init__(self):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._initSubCommands()
    #}}}

    #{{{def _initSubCommands(self):
    def _initSubCommands(self):
        self.subparsers = self.parser.add_subparsers(title='subcommands',
                                    help='additional help')
        for attr in dir(self):
            if not attr.startswith('do'):
                continue
            _attr = attr[2:]
            try:
                _help = getattr(self, attr).__doc__
                _help = _help.split('\n')[0] if _help else None
            except IndexError:
                _help = None
            subcmd = _attr.lower()
            subparser = self.subparsers.add_parser(subcmd, help=_help)
            subparser.set_defaults(func=getattr(self,attr))
            setattr(self, "parser_%s" % subcmd, subparser)
            # setup arg of parser
            try:
                fn = getattr(self, "_setArgs%s" % _attr)
                if callable(fn):    fn()
            except AttributeError:
                pass
    #}}}

    #{{{def run(self, args):
    def run(self, args):
        if not args:
            args = ['-h']
        args = self.parser.parse_args(args)
        args.func(args)
    #}}}
pass
