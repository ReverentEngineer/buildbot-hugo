from buildbot.process.buildstep import ShellMixin, LoggingBuildStep
from twisted.internet import defer

class Hugo(ShellMixin, LoggingBuildStep):
    """BuildStep for buildbot that runs huge.
    """

    DEFAULT_HUGO = 'hugo'

    def __init__(self, source=None, destination=None, hugo=DEFAULT_HUGO, clean=True, **kwargs):
        self.source = source
        self.detination = destination
        self.hugo = hugo
        self.clean = True
        kwargs = self.setupShellMixin(kwargs, prohibitArgs=['command'])
        super(Hugo, self).__init__(**kwargs)

    @defer.inlineCallbacks
    def run(self):
        """Runs hugo"""
        command = [ self.hugo ]
        if self.clean:
            command.append('--cleanDestinationDir')

        if self.source:
            command.append('--source')
            command.append(self.source)
        
        if self.destination:
            command.append('--destination')
            command.append(self.destination)
