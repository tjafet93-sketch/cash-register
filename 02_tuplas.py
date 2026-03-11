# las tuplas son similares a las listas , pero son inmutables.
# lo que significa de que no se pueden modificar despues de su creacion. 
# se definen utilizando parentesis() en lugar de corchetes.
roles_del_sistema= ("adminitrsdor", "usiario", "invitado")
print(roles_del_sistema)

roles_del_sistema.append("superusuario") #esto genera un error, ya que las tuplas son inmutables