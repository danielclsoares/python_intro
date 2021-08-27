def mi_p_me(milhas):
  metros = milhas*1609.34
  print( metros , "metros")
  return metros

def me_p_mi(metros):
  milhas = metros/1609.34
  print (milhas , "milhas")
  return milhas

def h_p_s(horas):
  segundos = horas*3600
  print(segundos , 'segundos')
  return segundos

def s_p_h(segundos):
  horas = segundos/3600
  print(horas , 'horas')
  return horas

print(me_p_mi(10000)/s_p_h(43.5*60), "milhas/hora")
