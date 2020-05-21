from pathlib import Path


import pytest
import sklearn


path = Path(sklearn.__file__) / 'sklearn' / 'maniforld' / 'tests' / 'test_t_sne.py'


pytest.main([str(path)])
