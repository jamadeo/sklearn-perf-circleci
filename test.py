from pathlib import Path


import pytest
import sklearn


path = Path(sklearn.__file__).parent / 'manifold' / 'tests' / 'test_t_sne.py'


pytest.main(['--verbose', str(path)])
