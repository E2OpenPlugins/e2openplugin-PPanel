from distutils.core import setup

pkg = 'Extensions.PPanel'
setup (name = 'enigma2-plugin-extensions-ppanel',
       version = '0.1',
       description = 'PPanel',
       package_dir = {pkg: 'plugin'},
       packages = [pkg],
       data_files = [('/etc/ppanel', ['plugin/data/PPanel_tutorial.xml'])]
      )
