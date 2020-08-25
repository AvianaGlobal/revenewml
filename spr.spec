# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['spr.py'],
             binaries = [
                ('C:\\Users\\MichaelJohnson\\venv37\\xgboost\\*.dll', 'xgboost/lib'),
                ('C:\\Users\\MichaelJohnson\\repos\\revenewml\\venv\\scripts\\*.dll', '.'),
                ('C:\\Windows\\System32\\vcruntime140.dll', '.'),
             ],
             datas=[
                ('LICENSE', '.'),
                ('config.ini', '.'),
                ('RevenewML/preprocessing/sql/*.sql', 'RevenewML/preprocessing/sql'),
                ('RevenewML/savedmodels/*.dat', 'RevenewML/savedmodels'),
             ],
             hiddenimports=[
                'colored',
                'IPython',
                'numpy',
                'matplotlib',
                'psutil',
                'pyodbc',
                'pywin32',
                'tdqm',
                'pkg_resources.py2_warn',
                'scipy',
                'scipy.special.cython_special',
                'sklearn.utils._cython_blas',
                'sklearn.neighbors.typedefs',
                'sklearn.neighbors.quad_tree',
                'sklearn.tree._utils',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='spr',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='spr')
