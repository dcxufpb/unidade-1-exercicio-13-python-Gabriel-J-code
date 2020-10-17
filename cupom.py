# coding: utf-8
def isEmpty(string):
	if (string == None) or (string == ""):
		return True
	return False
	
class Endereco:

	def __init__(self, logradouro, numero, complemento, bairro, municipio, estado, cep):
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.estado = estado
		self.cep = cep

	def dados_endereco(self):

		self.validar_campos_obrigatorios()
		
		_numero = "s/n" if not self.numero else str(self.numero)

		_complemento = " " + self.complemento if not isEmpty(self.complemento) else ""	

		_bairro = self.bairro + " - " if not isEmpty(self.bairro) else ""

		_cep = "CEP:" + self.cep if not isEmpty(self.cep) else ""

		dados = "%s, %s%s\n" %(self.logradouro,_numero,_complemento)
		dados += "%s%s - %s\n" % (_bairro,self.municipio,self.estado)
		dados += "%s" % (_cep)
		return dados

	def validar_campos_obrigatorios(self):
		if isEmpty(self.logradouro):
			raise Exception("O campo logradouro do endereço é obrigatório")
			
		if isEmpty(self.municipio):
			raise Exception("O campo município do endereço é obrigatório")

		if isEmpty(self.estado):
			raise Exception("O campo estado do endereço é obrigatório")


class Loja:

	def __init__(self, nome_loja, endereco, telefone, observacao, cnpj,	inscricao_estadual):
		self.nome_loja = nome_loja
		self.endereco = endereco
		self.telefone = telefone
		self.observacao = observacao
		self.cnpj = cnpj
		self.inscricao_estadual = inscricao_estadual
		self.vendas = []

	def vender(self, datahora, ccf, coo):
		nova_venda = Venda(self, datahora, ccf, coo)
		self.vendas.append(nova_venda)
		return nova_venda
		

	def dados_loja(self):
		self.validar_campos_obrigatorios()		

		_telefone = "Tel " + self.telefone if not isEmpty(self.telefone) else ""

		_telefone = " " + _telefone if not isEmpty(self.endereco.cep) and not isEmpty(self.telefone) else _telefone

		_observacao = self.observacao if not isEmpty(self.observacao) else ""

		nota = self.nome_loja + "\n"		
		nota += "%s%s\n" % (self.endereco.dados_endereco(),_telefone)
		nota += "%s\n" % (_observacao)
		nota += "CNPJ: %s\n" %(self.cnpj)
		nota += "IE: %s" % (self.inscricao_estadual)

		return nota 

	def validar_campos_obrigatorios(self):
		if type(self.endereco) != Endereco:
			raise Exception("O campo Endereco da loja está invalido")

		if isEmpty(self.nome_loja):
			raise Exception("O campo nome da loja é obrigatório")		

		if isEmpty(self.cnpj):
			raise Exception("O campo CNPJ da loja é obrigatório")	

		if isEmpty(self.inscricao_estadual):
			raise Exception("O campo inscrição estadual da loja é obrigatório")

import datetime

class Venda:
	def __init__(self,loja,datahora,ccf,coo):
		self.loja=loja
		self.datahora = datahora
		self.ccf = ccf
		self.coo = coo

	def dados_venda(self):
		self.validar_campos_obrigatorios()
		texto_data = self.datahora.strftime("%d/%m/%Y")
		texto_hora = self.datahora.time().strftime("%H:%M:%S")		

		return '''{data} {hora}V CCF:{ccf} COO:{coo}'''.format(data=texto_data, hora=texto_hora, ccf='%s'%self.ccf, coo='%s'%self.coo)
	
	def validar_campos_obrigatorios(self): 
		if type(self.loja) != Loja:
			raise Exception("O campo loja da venda não é valido")
		if type(self.datahora) != datetime.datetime:
			raise Exception("O campo data e hora da venda não é valido")
		if isEmpty(self.ccf):
			raise Exception("O campo ccf da venda não é valido")
		if isEmpty(self.coo):
			raise Exception("O campo coo da venda não é valido")	
		
	
	# Implemente aqui
