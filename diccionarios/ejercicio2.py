datosUsuario = {}
datosUsuario['nombre'] = input('Dame nombre:');
datosUsuario['edad'] = int(input('Dame edad:'));
datosUsuario['direccion'] = input('Dame direccion:');
datosUsuario['telefono'] = input('Dame telefono:');

print(datosUsuario.get('nombre')+' tiene '+str(datosUsuario.get('edad'))+' años,'
      +' vive en '+datosUsuario.get('direccion')+ ' y su número de telefono es '+ datosUsuario.get('telefono'))