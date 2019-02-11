"""Collection of tests."""
import pytest

import dblib.lib


f0 = dblib.lib.Finding('CD spook', 'my_PC', 'The CD drive is missing.')
f1 = dblib.lib.Finding('Unplugged', 'my_PC', 'The power cord is unplugged.')
f2 = dblib.lib.Finding('Monitor switched off', 'my_PC', 'The monitor is switched off.')


def test_add_remove():
    """Test function."""
    db = dblib.lib.BackyardDB()

    # regular cases
    db.add(f0)
    assert f0 in db.findings
    assert len(db.findings) == 1
    db.add(f1)
    assert f1 in db.findings
    assert len(db.findings) == 2
    db.add(f2)
    assert f2 in db.findings
    assert len(db.findings) == 3
    db.add(None)
    assert len(db.findings) == 3
    db.remove(f1)
    assert f1 not in db.findings
    assert len(db.findings) == 2
    # test exceptions
    with pytest.raises(TypeError):
        db.add(1)


def test_update():
    """Test function."""
    db = dblib.lib.BackyardDB()
    db.add(f0)
    db.add(f1)
    db.update(f1, f2)
    assert f2 in db.findings
    assert len(db.findings) == 2
