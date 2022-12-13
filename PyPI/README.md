# Add library to PyPI

```bash
python setup.py bdist_wheel
```

```bash
dist\image_regist-0.0.1-py3-none-any.whl
```

```bash
pip install dist\image_regist-0.0.5-py3-none-any.whl
pip uninstall dist\image_regist-0.0.5-py3-none-any.whl
```

```bash
pip install D:\Code\Mandiri\Project-root\image-regist\dist\image_regist-0.0.4-py3-none-any.whl
pip uninstall D:\Code\Mandiri\Project-root\image-regist\dist\image_regist-0.0.4-py3-none-any.whl
```

pypi test

```bash
python -m twine upload -r testpypi -u mufis73 -p Libpython01 dist/*
```

pypi

```bash
python -m twine upload -u mufis73 -p Libpython01 dist\*
```

```bash
pip install image-regist
pip uninstall image-regist
```
