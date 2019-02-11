"""Class to manage interaction with databases."""


class BackyardDB:
    """Class to manage interaction with databases."""

    findings = set()

    def __init__(self):
        """Initialize the class instance."""

    def add(self, finding):
        """Add entry."""
        if finding is None:
            return
        if not isinstance(finding, Finding):
            raise TypeError("%s has to be of type 'Finding'" % finding)
        print("Adding %s" % finding)
        self.findings.add(finding)

    def remove(self, finding):
        """Remove entry."""
        print("Removing %s" % finding)
        self.findings.remove(finding)

    def update(self, finding, update):
        """Update entry."""
        print("Updating %s" % finding)
        self.remove(finding)
        self.add(update)


class Finding:
    """A class to abstract findings."""

    _name = None
    _asset = None
    _description = None

    def __init__(self, name, asset, description):
        """Initialize the finding."""
        self._name = name
        self._asset = asset
        self._description = description

    def __repr__(self):
        """Represent unambiguous finding description."""
        return '<name %r>' % self._name
